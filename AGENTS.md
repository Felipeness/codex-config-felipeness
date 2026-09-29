# Instruções deste repositório

Este repositório distribui preferências pessoais e workflows reutilizáveis para Codex. Preserve compatibilidade com o formato oficial de skills, `AGENTS.md`, `config.toml` e hooks.

- Não instale nem altere arquivos em `~/.codex`, `~/.agents` ou outro projeto enquanto estiver editando este repositório, a menos que a tarefa peça isso.
- Mantenha exemplos portáveis; se uma regra vier de um ambiente Superlogica/Jira, identifique-a como opcional e específica.
- Não prometa recursos que o Codex não documenta. Em particular, a statusline nativa usa identificadores configuráveis, sem renderer customizado por comando.
- Skills devem ser curtas, específicas e progressivas. Instruções compartilhadas ficam em `config/AGENTS.md`; não replique blocos longos em cada skill.
- Use nomes e código em inglês, documentação padrão em português brasileiro.
- Revise scripts de instalação e hooks com foco em preservar arquivos preexistentes e limitar efeitos colaterais.
