# Codex config by FelipeNess

Configuração pessoal de Codex baseada nos workflows de [claude-config-felipeness](https://github.com/Felipeness/claude-config-felipeness). O projeto separado da statusline nativa está em [statuslinecodex](https://github.com/Felipeness/statuslinecodex).

O port mantém as preferências de engenharia, os fluxos de investigação, implementação, revisão e skills por domínio. Onde o Codex oferece uma interface diferente, usa a extensão nativa em vez de imitar comandos do Claude Code.

## O que foi portado

| Claude Code | Versão Codex | Compatibilidade |
|---|---|---|
| `CLAUDE.md` global | [`config/AGENTS.md`](config/AGENTS.md) | Instruções globais e portáveis |
| Skills | [`.agents/skills/`](.agents/skills/) | Skills descobertas automaticamente e invocáveis por `$nome-da-skill` |
| Slash commands | Skills de workflow | `/review`, `/investigate` e similares viram skills explícitas, sem depender de comandos customizados do Claude |
| Hooks para Bash e edições | [`.codex/hooks.json`](.codex/hooks.json) | Inclui um guard opcional e restrito para comandos destrutivos |
| Ralph loops | Skills `ralph-*` | Ciclos limitados no mesmo fluxo, sem runner externo ou execução infinita |
| Análise com muitos agentes | [`.codex/agents/`](.codex/agents/) | Quatro agentes focados e somente leitura, acionados por uma skill de análise |
| Plugins, MCPs e settings privados do Claude | Provisionamento manual | Integrações podem exigir ferramentas, contas ou credenciais; não são instaladas nem habilitadas implicitamente |

Opções como `skipDangerousModePermissionPrompt`, `skipAutoPermissionPrompt` e o modo de permissão do Claude não são copiadas para reduzir as proteções do Codex. Também não há lint/typecheck automático a cada edição: os comandos variam por projeto e devem seguir os critérios de validação da tarefa.

## Instalação

O instalador requer Python 3.11 ou superior.

No macOS/Linux:

```bash
./install.sh
```

No Windows PowerShell:

```powershell
./install.ps1
```

O instalador copia skills para `~/.agents/skills`, agentes para `$CODEX_HOME/agents`, adiciona as instruções à `$CODEX_HOME/AGENTS.md`, mescla preferências gerais a `$CODEX_HOME/config.toml` (incluindo `service_tier = "auto"` e `model_reasoning_effort = "medium"`, veja abaixo) e instala o guard em `$CODEX_HOME/hooks.json`. Configurações preexistentes são preservadas. Use `--force` / `-Force` para fazer backup e substituir skills/agentes com conflito.

Reinicie o Codex para carregar as skills e os agentes. A statusline nativa e o editor offline ficam no [repositório statuslinecodex](https://github.com/Felipeness/statuslinecodex). O Codex exige que hooks novos sejam revisados e confiados em `/hooks` antes de executá-los. A instalação global do hook não pula essa revisão.

### Modelo, esforço e service tier

| Chave | Valor | Por quê |
|---|---|---|
| `service_tier` | `"auto"` | Via LLM Gateway o tier `fast` é recusado e o Codex mostra aviso a cada chamada. O instalador sempre grava `auto`, mesmo se já houver outro valor |
| `model_reasoning_effort` | `"medium"` | `high`/`xhigh` deixam o Codex bem mais lento e gastam mais token sem ganho no dia a dia. Só é gravado se você ainda não escolheu um nível |

As duas chaves ficam no topo do `config.toml`, antes da primeira tabela `[...]`; abaixo de uma tabela o TOML as trata como parte dela e o Codex ignora. O provider (`model`, `model_provider`, `[model_providers.*]`) não é instalado por aqui, ele depende de cada empresa: siga o manual interno de configuração do Codex.

## Workflows e skills

| Skill | Uso |
|---|---|
| `investigate`, `planning` | Mapear estado, restrições e opções antes de propor uma abordagem |
| `new-feature` | Planejar e implementar uma feature com escopo claro |
| `code-review` | Revisar alterações por bugs, segurança e riscos; sem editar por padrão |
| `review-staged` | Revisar somente o diff staged |
| `ultrathink-review` | Revisão profunda de design e qualidade |
| `codebase-analysis` | Análise ampla com agentes focados quando trouxer valor |
| `debugging` | Reproduzir, localizar causa raiz e corrigir bugs |
| `refactoring` | Refatorar preservando comportamento e escopo |
| `ralph-implement`, `ralph-review`, `ralph-test` | Ciclos iterativos limitados por objetivo e critério de parada |
| `ralph-debug`, `ralph-refactor`, `ralph-docs` | Ciclos especializados de depuração, refatoração e documentação |
| `ralph-migrate`, `ralph-perf`, `ralph-cancel` | Migração, otimização e encerramento de um ciclo |
| `code-quality`, `typescript`, `react`, `go` | Padrões de implementação por domínio |
| `api-design`, `architecture-patterns`, `functional-programming` | APIs, arquitetura e programação funcional |
| `observability` | Logs, métricas, tracing e tratamento de falhas |
| `figma-to-code`, `figma-code-connect` | Implementação e mapeamento de designs Figma |
| `writing`, `copywriting`, `code-review-comments`, `trim-pr-description`, `fp-audit` | Documentação, copy, comentários de revisão, descrição de PR e auditoria funcional |
| `pr-jira-review`, `mirror-pr`, `open-pr` | Fluxos opcionais de Jira e GitHub; ações externas só quando solicitadas |

Skills são carregadas quando relevantes. Use `$nome-da-skill` para invocá-las diretamente. Não é necessário copiar as skills para usar este repositório localmente.

## Hooks e agentes

O hook [`pre_tool_guard.py`](.codex/hooks/pre_tool_guard.py) bloqueia um conjunto curto de comandos de alto risco, como `git reset --hard`, `git clean -f`, force push, remoção da raiz e `curl | sh`. Ele é um guardrail local, não substitui permissões ou revisão do comando. Para uma operação legítima que coincida com uma regra, edite ou desative o hook depois de revisar o comando.

Hooks locais são carregados apenas para projetos confiáveis. Revise a definição pelo `/hooks` antes de confiá-la. O Codex tem eventos diferentes dos hooks `TaskCreated`, `TaskCompleted` e `TeammateIdle` do Claude Code; esses comportamentos foram levados para skills em vez de fingir equivalência.

Os agentes personalizados em `.codex/agents/` fazem exploração, revisão de qualidade, revisão de segurança e análise de testes em modo somente leitura. `codebase-analysis` usa delegação em tarefas amplas; para perguntas pequenas, a própria sessão pode analisar o repositório sem abrir agentes.

## Fontes

- [Codex: Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md)
- [Codex: Customization overview](https://learn.chatgpt.com/docs/customization/overview.md)
- [Codex: Hooks](https://learn.chatgpt.com/docs/hooks.md)
- [Codex: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md)
- [Codex: Configuration reference](https://developers.openai.com/codex/config-file/config-reference.md)
- [Codex: Sample configuration](https://learn.chatgpt.com/docs/config-file/config-sample.md)
