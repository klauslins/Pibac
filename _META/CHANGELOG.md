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

### Adicionado — 18/09/2026
- `06_MEDIA/equipamento.md` — versão simples do manual de equipamento do
  ministério de mídia: os dois equipamentos, qual usar em cada bloco do culto,
  rotina de retirada e devolução e um responsável único
- Registrado que a **Tamron 17-70 f/2.8 é lente de APS-C**: na A7 IV, que é
  full-frame, a câmera entra em modo recorte. A foto sai com ~15 MP em vez de
  33 MP e a grande-angular se perde (17mm se comportam como ~25mm), o que torna
  o plano aberto do templo cheio difícil com esse conjunto

### Organizado — 17/09/2026
- **Acervo de fotos migrado para `06_MEDIA/fotos/originais/`** — 2.542 arquivos,
  19 GB, que estavam em `Pibac/` na raiz do SSD em pastas numeradas de 2 a 15
- Cada sessão virou `aaaa-mm-dd-evento`, com a data lida do EXIF
  `DateTimeOriginal`. A data do arquivo não serve: o cartão era descarregado de
  madrugada, às vezes no dia seguinte, o que fazia duas sessões de domingo
  parecerem de segunda-feira
- O horário de captura confirmou o que cada pasta é: 18h–20h é Culto de
  Celebração; a pasta `10` era **EBD** (9h28–10h15), não culto
- A pasta `11` tinha três datas misturadas e foi separada por captura
- 115 fotos soltas na raiz de `culto de domingo/` eram o culto de **31/05**
- 103 itens sem valor de acervo (export de Photoshop, projeto de After Effects,
  PNG com nome sem significado) foram para `_a-triar/`. **Nada foi apagado**
- `migracao-2026-09-17.csv` registra origem e destino de cada um dos 403
  movimentos, para que tudo seja reversível
- PSD de 176 MB para `08_MASTERS/` (acima de 100 MB, fora do Git); molde de vídeo
  de Missões para `04_PRODUCTION/missoes/fontes/`

### Adicionado — 17/09/2026
- **Skill `comunicacao-pibac`** em `.claude/skills/` — o agente oficial de
  comunicação da igreja, a partir do prompt mestre de 30 seções. Carrega sozinha
  no Claude Code quando o pedido é de conteúdo
- Estruturada em camadas: o `SKILL.md` traz identidade, tom, fidelidade bíblica,
  como responder a quem produz em tempo real e o roteador; o detalhe de cada
  frente fica em `references/` (canais, sermões, ministérios, produção visual) e
  só entra em contexto quando a tarefa pede
- O que o prompt mestre não trazia e foi ligado às regras do repositório:
  autorização de imagem de menores, dado pessoal de membro, a marca que não se
  gera por IA e a pendência do nome oficial ("em" ou "de" Águas Claras)
- A direção de cobertura de **culto** aponta para o manual e o roteiro que já
  existem, em vez de duplicar; os cinco blocos de direção visual ficam para
  **eventos**
- **Manual de Stories para cobertura de culto**, a partir do
  `Guia de Stories — Missão e Mídia` (15 páginas, PDF). Os três "modelos" do
  original eram a mesma sequência com redação diferente — viraram **uma**
  sequência de seis blocos, com as variações preservadas onde são úteis
  (falas de abertura e de encerramento)
- `03_CONTENT/roteiros/_modelo-cobertura-culto.md` — o roteiro de uso, uma
  página, em ordem de acontecimento e com horário relativo à hora do culto. É
  copiado a cada culto e preenchido durante
- Acrescentado ao original o que faltava e que aqui é obrigatório: **autorização
  de imagem no bloco Kids**, com a alternativa de registro sem identificar
  ninguém, e o caminho do arquivo depois do culto até `_PUBLISH-READY/`
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
