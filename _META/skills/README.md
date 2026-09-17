---
tipo: skill
cliente: pibac
titulo: Skills do projeto
usar_quando: quiser saber quais agentes de IA existem neste repositorio e onde eles moram
status: ativo
atualizado: 2026-09-17
---

# Skills do projeto

## `comunicacao-pibac`

O agente oficial de comunicação e conteúdo da igreja: tom de voz, fidelidade
bíblica, padrão de cada canal e as regras que ele não pode violar.

**Onde mora:** [`.claude/skills/comunicacao-pibac/`](../../.claude/skills/comunicacao-pibac/)

Ela fica em `.claude/skills/` e não aqui porque esse é o caminho que o Claude
Code lê sozinho — colocada em `_META/skills/`, ela seria só um arquivo parado.
Este README existe para quem procurar pelo caminho do padrão organizacional.

```
.claude/skills/comunicacao-pibac/
├── SKILL.md                      identidade, tom, regras e roteador
└── references/
    ├── canais.md                 Story, legenda, carrossel, Reels, roteiro, WhatsApp, evento
    ├── sermoes.md                sermão, transcrição, resumir × criar, revisão bíblica
    ├── ministerios.md            tom por frente, missões, aniversário
    └── producao-visual.md        direção de foto e vídeo, depoimento, briefing, prompts de IA
```

**Como usar:**

- **No Claude Code, dentro deste repositório:** carrega sozinha quando o pedido
  é de conteúdo da igreja. Para chamar na mão: `/comunicacao-pibac`
- **Em outra ferramenta** (ChatGPT, Gemini, outro assistente): cole o conteúdo
  do `SKILL.md` como instrução do sistema. Se a tarefa for específica, cole
  junto o `references/` correspondente

**Ao alterar:** o `SKILL.md` carrega sempre que a skill dispara, então ele
precisa continuar enxuto. Detalhe de canal, de sermão, de ministério ou de
produção visual vai para o `references/` — é isso que mantém o agente rápido e
o contexto limpo.
