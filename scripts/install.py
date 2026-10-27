#!/usr/bin/env python3
"""Install this Codex setup globally while preserving unrelated user config."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shlex
import shutil
import sys
import tempfile
from typing import Iterable

if sys.version_info < (3, 11):
    raise SystemExit("Este instalador requer Python 3.11 ou superior.")

import tomllib


ROOT = pathlib.Path(__file__).resolve().parents[1]
HOME_DIR = pathlib.Path.home()
CODEX_HOME_DIR = pathlib.Path(os.environ.get("CODEX_HOME") or HOME_DIR / ".codex").expanduser()
SKILLS_HOME_DIR = HOME_DIR / ".agents" / "skills"
BACKUP_STAMP = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
BEGIN_MARKER = "<!-- BEGIN codex-config-felipeness managed instructions -->"
END_MARKER = "<!-- END codex-config-felipeness managed instructions -->"

def backup_path(path: pathlib.Path) -> pathlib.Path:
    candidate = path.with_name(f"{path.name}.backup.{BACKUP_STAMP}")
    suffix = 1
    while candidate.exists():
        candidate = path.with_name(f"{path.name}.backup.{BACKUP_STAMP}.{suffix}")
        suffix += 1
    return candidate


def paths_equal(source: pathlib.Path, target: pathlib.Path) -> bool:
    if source.is_file() and target.is_file():
        return source.read_bytes() == target.read_bytes()
    if source.is_dir() and target.is_dir():
        source_files = sorted(p.relative_to(source) for p in source.rglob("*") if p.is_file())
        target_files = sorted(p.relative_to(target) for p in target.rglob("*") if p.is_file())
        return source_files == target_files and all(
            (source / relative).read_bytes() == (target / relative).read_bytes()
            for relative in source_files
        )
    return False


def install_copy(source: pathlib.Path, target: pathlib.Path, force: bool) -> None:
    if target.exists():
        if paths_equal(source, target):
            print(f"Already installed: {target}")
            return
        if not force:
            print(f"Preserved existing, different file: {target}")
            return
        backup = backup_path(target)
        if target.is_dir():
            shutil.copytree(target, backup)
            shutil.rmtree(target)
        else:
            shutil.copy2(target, backup)
            target.unlink()
        print(f"Backed up {target} to {backup}")

    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)
    print(f"Installed: {target}")


def atomic_write(path: pathlib.Path, content: str, backup_existing: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and backup_existing:
        backup = backup_path(path)
        shutil.copy2(path, backup)
        print(f"Backed up {path} to {backup}")
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = pathlib.Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(mode)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def managed_instructions(existing: str, template: str) -> str:
    block = f"{BEGIN_MARKER}\n{template.rstrip()}\n{END_MARKER}"
    marker_pattern = re.compile(
        rf"(?s){re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}"
    )
    if marker_pattern.search(existing):
        merged = marker_pattern.sub(lambda _: block, existing, count=1)
    elif existing.strip():
        merged = existing.rstrip() + "\n\n" + block + "\n"
    else:
        merged = block + "\n"
    return merged


def table_headers(lines: list[str]) -> list[tuple[int, str]]:
    headers = []
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("[") or stripped.startswith("[["):
            continue
        close = stripped.find("]")
        if close < 0:
            continue
        table_name = stripped[1:close].strip()
        if table_name:
            headers.append((index, table_name))
    return headers


def setting_line_pattern(key: str) -> re.Pattern[str]:
    return re.compile(rf"^\s*{re.escape(key)}\s*=")


def replace_simple_assignment(line: str, key: str, value: str) -> str:
    assignment = re.compile(rf"^(\s*){re.escape(key)}\s*=.*$")
    if assignment.match(line):
        return assignment.sub(lambda match: f"{match.group(1)}{key} = {value}", line)
    return line


def merge_table(
    text: str,
    table: str,
    settings: dict[str, str],
    required_overrides: Iterable[str] = (),
) -> str:
    lines = text.splitlines()
    headers = table_headers(lines)
    table_header = next((index for index, name in headers if name == table), None)
    override_keys = set(required_overrides)

    # Refuse inline tables instead of risking a lossy rewrite of user settings.
    inline_table = re.compile(rf"^\s*{re.escape(table)}\s*=")
    if table_header is None and any(inline_table.match(line) for line in lines):
        raise ValueError(
            f"{table} is defined as an inline TOML table; merge its keys manually to preserve formatting."
        )

    if table_header is None:
        child_header = next(
            (index for index, name in headers if name.startswith(table + ".")), None
        )
        block = [f"[{table}]"]
        block.extend(f"{key} = {value}" for key, value in settings.items())
        block.append("")
        if child_header is None:
            if lines and lines[-1].strip():
                lines.append("")
            lines.extend(block)
        else:
            before = lines[:child_header]
            if before and before[-1].strip():
                before.append("")
            lines = before + block + lines[child_header:]
        return "\n".join(lines).rstrip() + "\n"

    section_end = next(
        (index for index, _ in headers if index > table_header), len(lines)
    )
    present_keys: set[str] = set()
    for index in range(table_header + 1, section_end):
        line = lines[index]
        for key, value in settings.items():
            if setting_line_pattern(key).match(line):
                present_keys.add(key)
                if key in override_keys:
                    lines[index] = replace_simple_assignment(line, key, value)

    missing = [
        f"{key} = {value}"
        for key, value in settings.items()
        if key not in present_keys
    ]
    if missing:
        insertion = section_end
        before = lines[:insertion]
        if before and before[-1].strip():
            before.append("")
        lines = before + missing + [""] + lines[insertion:]
    return "\n".join(lines).rstrip() + "\n"


def merge_root(
    text: str,
    settings: dict[str, str],
    required_overrides: Iterable[str] = (),
) -> str:
    lines = text.splitlines()
    headers = table_headers(lines)
    root_end = headers[0][0] if headers else len(lines)
    override_keys = set(required_overrides)
    present_keys: set[str] = set()
    for index in range(root_end):
        for key, value in settings.items():
            if setting_line_pattern(key).match(lines[index]):
                present_keys.add(key)
                if key in override_keys:
                    lines[index] = replace_simple_assignment(lines[index], key, value)

    missing = [f"{key} = {value}" for key, value in settings.items() if key not in present_keys]
    if not missing:
        return "\n".join(lines).rstrip() + "\n"
    before = lines[:root_end]
    if before and before[-1].strip():
        before.append("")
    after = lines[root_end:]
    spacer = [""] if after else []
    return "\n".join(before + missing + spacer + after).rstrip() + "\n"


def merge_config(text: str) -> str:
    # the LLM Gateway only accepts the "default" tier ("fast" and "auto" are rejected), so it always wins;
    # reasoning effort is only a default and keeps whatever the user already chose.
    merged = merge_root(
        text,
        {"model_reasoning_effort": '"medium"', "service_tier": '"default"'},
        required_overrides={"service_tier"},
    )
    merged = merge_table(
        merged,
        "agents",
        {"max_concurrent_threads_per_session": "4"},
    )
    merged = merge_table(merged, "features", {"hooks": "true"}, required_overrides={"hooks"})
    tomllib.loads(merged)
    return merged


def merged_hook_config(target: pathlib.Path, command: str, command_windows: str) -> str:
    if target.exists():
        data = json.loads(target.read_text(encoding="utf-8"))
    else:
        data = {"description": "Codex lifecycle hooks.", "hooks": {}}
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError("hooks.json has an invalid top-level 'hooks' value.")
    pre_tool_use = hooks.setdefault("PreToolUse", [])
    if not isinstance(pre_tool_use, list):
        raise ValueError("hooks.json 'PreToolUse' must be an array.")

    for group in pre_tool_use:
        if not isinstance(group, dict):
            continue
        handlers = group.get("hooks", [])
        if any(
            isinstance(handler, dict)
            and "felipeness_pre_tool_guard.py" in str(handler.get("command", ""))
            for handler in handlers
        ):
            return json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    pre_tool_use.append(
        {
            "matcher": "Bash",
            "hooks": [
                {
                    "type": "command",
                    "command": command,
                    "commandWindows": command_windows,
                    "timeout": 2,
                    "statusMessage": "Checking risky shell commands",
                }
            ],
        }
    )
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def preflight(config_path: pathlib.Path, hooks_path: pathlib.Path) -> tuple[str, str]:
    config_text = config_path.read_text(encoding="utf-8") if config_path.exists() else ""
    tomllib.loads(config_text)
    merged_config = merge_config(config_text)

    hook_script_path = CODEX_HOME_DIR / "hooks" / "felipeness_pre_tool_guard.py"
    posix_command = f"python3 {shlex.quote(str(hook_script_path))}"
    windows_path = str(hook_script_path).replace("'", "''")
    windows_command = f"py -3 '{windows_path}'"
    merged_hooks = merged_hook_config(hooks_path, posix_command, windows_command)
    json.loads(merged_hooks)
    return merged_config, merged_hooks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", "-f", action="store_true", help="Back up and replace conflicting skill/agent files.")
    args = parser.parse_args()

    config_path = CODEX_HOME_DIR / "config.toml"
    hooks_path = CODEX_HOME_DIR / "hooks.json"
    CODEX_HOME_DIR.mkdir(parents=True, exist_ok=True)

    try:
        merged_config, merged_hooks = preflight(config_path, hooks_path)
    except (OSError, json.JSONDecodeError, tomllib.TOMLDecodeError, ValueError) as error:
        print(f"Install aborted before changing files: {error}", file=sys.stderr)
        return 2

    for skill in sorted((ROOT / ".agents" / "skills").iterdir()):
        if skill.is_dir():
            install_copy(skill, SKILLS_HOME_DIR / skill.name, args.force)

    for agent in sorted((ROOT / ".codex" / "agents").glob("*.toml")):
        install_copy(agent, CODEX_HOME_DIR / "agents" / agent.name, args.force)

    install_copy(
        ROOT / ".codex" / "hooks" / "pre_tool_guard.py",
        CODEX_HOME_DIR / "hooks" / "felipeness_pre_tool_guard.py",
        args.force,
    )

    instructions_path = CODEX_HOME_DIR / "AGENTS.md"
    existing_instructions = (
        instructions_path.read_text(encoding="utf-8") if instructions_path.exists() else ""
    )
    template = (ROOT / "config" / "AGENTS.md").read_text(encoding="utf-8")
    instructions = managed_instructions(existing_instructions, template)
    if instructions != existing_instructions:
        atomic_write(instructions_path, instructions)
        print(f"Installed global instructions: {instructions_path}")
    else:
        print(f"Global instructions are current: {instructions_path}")

    current_config = config_path.read_text(encoding="utf-8") if config_path.exists() else ""
    if current_config != merged_config:
        atomic_write(config_path, merged_config)
        print(f"Installed Codex settings: {config_path}")
    else:
        print(f"Codex settings are current: {config_path}")

    current_hooks = hooks_path.read_text(encoding="utf-8") if hooks_path.exists() else ""
    if current_hooks != merged_hooks:
        atomic_write(hooks_path, merged_hooks)
        print(f"Installed global hooks: {hooks_path}")
    else:
        print(f"Global hooks are current: {hooks_path}")

    print("\nRestart Codex to load the new instructions, skills, and agents.")
    print("Open /hooks to inspect and trust the new shell guard before expecting it to run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
