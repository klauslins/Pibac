---
tipo: changelog
cliente: pibac
titulo: CHANGELOG
usar_quando: saber o que ja foi feito e quando
status: ativo
atualizado: 2026-09-17
---

# CHANGELOG — Primeira Igreja Batista em Águas Claras

Histórico de mudanças estruturais e entregas do projeto.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Não publicado]

### Adicionado — 17/09/2026
- **Esqueleto do design system em `00_BRAND/`**, para o Klaus preencher com as
  decisões de design. Nenhuma cor, fonte ou medida de marca foi decidida aqui
- `design-system.md`, `cores/paleta.md`, `tipografia/tipografia.md`,
  `logo/logo.md` e `grafismos/grafismos.md` — as seções e as perguntas, em branco
- `tokens/tokens.json` — fonte da verdade no formato W3C Design Tokens. Cor,
  família tipográfica e sombra estão em `null`; escalas de tamanho, espaço,
  entrelinha e raio já vêm preenchidas por serem encanamento, não identidade
- `_META/automacao/gerar-tokens.py` — gera `tokens.css`, `tokens.scss` e
  `tailwind.preset.js` a partir do JSON. **Recusa gerar enquanto houver `null`**
  e lista o que falta, em vez de produzir arquivo com valor chutado. Os grupos de
  cor do preset Tailwind saem do próprio JSON, sem lista fixa no script
- `preview.html` — lê as variáveis do `tokens.css` e mostra o sistema aplicado;
  enquanto não houver tokens, explica o que fazer
- `AGENTS.md`: duas regras absolutas novas — §2.11 nenhum hex à mão, §2.12 a
  marca não é redesenhada nem gerada por IA

### Planejado
- Reunião de onboarding — fechar os `#CONFIRMAR` do briefing
- Identidade visual original (`.ai`/`.svg`) em `00_BRAND/`
- Modelo de autorização de uso de imagem aprovado pela diretoria
- Linhas editoriais e calendário de conteúdo

---

## [1.0.0] — 2026-09-17

### Adicionado
- Projeto criado a partir do **Padrão Organizacional Akza v1.5**
- Estrutura de pastas `00_BRAND` a `08_MASTERS` + `_META`
- Repositório Git local com Git LFS configurado *(ainda sem remoto)*
- Scripts de automação em `_META/automacao/`
- `01_STRATEGY/_fontes/autorizacoes-de-imagem/` — arquivo das autorizações de
  uso de imagem, exigidas antes de qualquer captação com crianças
- `AGENTS.md` adaptado ao contexto de igreja: visão e missão oficiais, agenda
  fixa, ministérios, assuntos de nomenclatura da PIBAC, tensão de marca e três
  regras absolutas novas (§2.8 imagem de menores, §2.9 dado pessoal de membro,
  §2.10 conferência de referência bíblica)
- `01_STRATEGY/briefing-cliente.md` preenchido com o que o site oficial
  documenta — história, visão, missão, pastor, agenda, ministérios e contatos

### Pendente de confirmação com a liderança
- Quem aprova publicação
- Forma oficial do nome: "em" ou "de" Águas Claras (o site usa as duas)
- Tom de voz, diferencial e público — há proposta escrita, falta validação
- Versão da Bíblia adotada nas peças
- Arquivos originais da marca
