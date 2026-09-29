# Preferências globais para Codex

Use estas instruções como base pessoal e ajuste-as ao projeto atual.

## Colaboração

- Responda em português brasileiro por padrão; use outro idioma quando solicitado ou quando o projeto exigir.
- Entenda o estado do repositório antes de propor mudanças. Para tarefas simples, aja diretamente; para trabalho amplo ou ambíguo, estruture uma abordagem curta e avance nas partes independentes.
- Preserve a intenção e o escopo pedidos. Não transforme uma preferência em obrigação quando isso aumentar a complexidade sem benefício claro.
- Explique limitações técnicas com precisão e ofereça uma alternativa viável.

## Código

- Priorize legibilidade e baixo custo cognitivo. Leia o fluxo de cima para baixo e use nomes que expressem intenção.
- Prefira funções coesas, fluxo explícito, composição e tipos que evitem estados inválidos.
- Evite `any` em TypeScript, erros silenciosamente ignorados, abstrações prematuras e duplicação que possa ser removida sem acoplamento.
- I/O externo deve ter timeout e tratamento de erro compatível com a operação. Não exponha segredos em logs, exemplos ou histórico.
- Siga os padrões e ferramentas que já existem no repositório antes de introduzir dependências ou convenções novas.

## Engenharia e Git

- Para mudanças grandes, descubra critérios de aceitação, dependências e caminhos de validação antes de implementar.
- Escolha verificações proporcionais à mudança e ao pedido. Informe o que executou e o que ficou sem verificação.
- Quando o repositório usar branches temáticas, prefira `tipo/TICKET-descricao-curta` com Jira ou `tipo/descricao-curta` sem ticket (`feat`, `fix`, `chore`, `refactor`, `docs`, `test`, `perf`, `ci`).
- Prefira Conventional Commits (`feat:`, `fix:`, `docs:` etc.) quando não houver padrão local diferente; use escopo com ticket se a equipe exigir, assunto em minúsculas e primeira linha de até 72 caracteres.
- Em PRs sujeitos a Jira, inclua o link da issue; sem issue, use a indicação de ausência que a equipe adotou.
- Em respostas a code review, responda cada observação no contexto dela e cite a mensagem do commit quando necessário, não o hash isolado.
- Não inclua marca de ferramenta de IA em commits sem necessidade ou pedido explícito.
- Crie commits, faça push, abra PR ou publique conteúdo somente quando isso fizer parte explícita do pedido.

## Revisão

- Priorize bugs, regressões, segurança, perda de dados e falta de cobertura relevante.
- Ao revisar, apresente achados reproduzíveis primeiro, com arquivo e linha. Separe riscos reais de preferências de estilo.
- Não altere o código durante uma revisão, a menos que a pessoa também peça correções.
