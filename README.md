---
tipo: visao-geral
cliente: pibac
titulo: "Primeira Igreja Batista em Águas Claras"
usar_quando: quiser a visao geral do projeto, sendo gente
status: ativo
atualizado: 2026-09-10
---

# Primeira Igreja Batista em Águas Claras — Projeto de Comunicação

> **Igreja:** Primeira Igreja Batista em Águas Claras (PIBAC)
> **Site:** pibaguasclaras.org.br · **Instagram:** [@pib.aguasclaras](https://www.instagram.com/pib.aguasclaras)
> **Estrutura:** padrão organizacional Akza v1.5

Repositório com os ativos, textos e materiais de comunicação da PIBAC.

> [!CAUTION]
> **Este repositório é público.** Tudo que entra aqui fica visível para qualquer
> pessoa, e o histórico do Git guarda para sempre — apagar num commit seguinte
> não remove. Antes de cada `git add`, releia as regras 8 e 9 do
> [`AGENTS.md`](AGENTS.md): **nenhuma foto de criança sem autorização** e
> **nenhum dado pessoal de membro** (telefone, endereço, pedido de oração,
> situação de saúde ou financeira).
>
> Se um dia entrar material que não pode ser público, o caminho é tornar o
> repositório privado — não é apagar o arquivo.

---

## 🚀 Primeiro acesso (leia antes de tudo)

Este repositório usa **Git LFS** para arquivos de design. Sem ele, você baixa
ponteiros de texto no lugar dos arquivos `.ai`, `.eps` e `.pdf`.

```bash
# 1. Instale o Git LFS (uma vez por computador)
brew install git-lfs && git lfs install

# 2. Clone
git clone https://github.com/klauslins/Pibac.git
cd Pibac
git lfs pull   # baixa os arquivos de design de verdade
```

> [!WARNING]
> **Já clonou sem o LFS?** Rode `git lfs pull`.
> O LFS aqui é o do próprio GitHub, com **cota gratuita de 1 GB** de
> armazenamento e 1 GB de tráfego por mês. Vídeo bruto e master de impressão
> não entram no Git — vão para `06_MEDIA/` e `08_MASTERS/`, fora do versionamento.

---

## 🧭 A igreja em 30 segundos

Igreja batista de Águas Claras, filiada à Convenção Batista Brasileira (CBB) e à
Convenção Batista do Planalto Central (CBPC). Nasceu em **14/12/2002** como
trabalho missionário de porta em porta no Residencial Araucárias e hoje reúne a
comunidade na Rua Jerivá, nº 5. Organiza a vida em torno de discipulado — PGM,
EBD, UDF e TADEL como degraus da mesma caminhada — sob a visão de **"ser uma
igreja de verdadeiros discípulos discipuladores"**. Pastor presidente:
**Pr. Moisés Gonçalves**, empossado em 31/10/2020.

| | |
|---|---|
| **Segmento** | Igreja evangélica batista — Convenção Batista Brasileira (CBB), Águas Claras/DF |
| **Público** | #CONFIRMAR — morador de Águas Claras e entorno, em frentes a mapear: membros, visitantes, famílias com filhos, juventude |
| **Tom** | #CONFIRMAR — *proposta:* acolhedor, claro e próximo. Sem jargão de seminário e sem jargão de marketing |
| **Aprovações** | #CONFIRMAR |

### Agenda fixa

| Dia | Atividade | Horário |
|---|---|---|
| Quarta | Manhã de Oração · Culto de Oração | 8h–10h · 19h30 |
| Sábado | Embaixadores e Mensageiras do Rei | 9h–11h |
| Domingo | Escola Bíblica Dominical · Culto de Celebração | 9h–11h30 · 18h–20h |

📖 Contexto completo: [`01_STRATEGY/briefing-cliente.md`](01_STRATEGY/briefing-cliente.md)

---

## 🗂️ Onde fica cada coisa

```
00_BRAND/        Identidade visual — logo, tipografia, cores.  ⚠️ FONTE DA VERDADE
01_STRATEGY/     Diagnóstico, manifesto, personas, linhas editoriais
02_PLANNING/     Calendário editorial, briefings de campanha, pautas
03_CONTENT/      Roteiros, copies, scripts de vídeo (o texto antes da arte)
04_PRODUCTION/   Arquivos editáveis em andamento (.ai, .psd, .fig) por campanha
05_EXPORTS/      Entregáveis finais prontos por canal (web, print, social)
06_MEDIA/        Banco de mídia — fotos, vídeos e áudios de captação
07_IMPRESSOS/    Peças para impressão física (cartão, timbrado, outdoor)
08_MASTERS/      Masters gigantes (>100 MB). Fora do Git — só no SSD 🚫
_META/           Documentação, automação e metadados do projeto
```

**A lógica do fluxo:** a numeração acompanha a ordem real do trabalho —
estratégia (01) vira planejamento (02), que vira texto (03), que vira arte (04),
que vira entregável (05). `00_BRAND` vem antes de tudo porque governa tudo.

### As três regras que não se quebram

1. **`00_BRAND/` é imutável.** Nada é alterado, movido ou renomeado ali sem aprovação de branding.
2. **Só se publica de `05_EXPORTS/_PUBLISH-READY/`.** Qualquer outra pasta é trabalho em andamento.
3. **Nomes sem acento, sem espaço, sem maiúscula.** Um espaço quebra a automação inteira.

---

## 📋 Como nomear arquivos

**Padrão:** `[tipo]-[assunto]-[variacao]-v[N].[ext]`

```
post-tema-do-post-colorido-v2.png
reels-porta-voz-apresentacao-v1.mp4
logo-h-oficial-v1.svg
```

| Regra | ✅ Certo | ❌ Errado |
|---|---|---|
| Só minúsculas | `post-lancamento-v1.png` | `Post-Lancamento-V1.png` |
| Sem acento | `informacao` | `informação` |
| Hífen, nunca espaço | `guia-conteudo` | `guia conteudo` |
| Versão numerada | `v1`, `v2`, `v3` | `final`, `FINAL2` |

📖 Regras completas: [`_META/NOMENCLATURA.md`](_META/NOMENCLATURA.md)

---

## 🔄 O fluxo de trabalho

```
  ROTEIRO/COPY         ARTE                REVISÃO           PUBLICAÇÃO
  03_CONTENT/    →  04_PRODUCTION/   →   05_EXPORTS/   →   _PUBLISH-READY/
```

📖 Detalhes: [`_META/PIPELINE.md`](_META/PIPELINE.md)

---

## 📱 Cobertura de culto

O material mais usado da semana. Duas peças, com funções diferentes:

| Arquivo | Para quê |
|---|---|
| [`manual-stories-culto.md`](01_STRATEGY/guia-de-conteudo/manual-stories-culto.md) | **O manual.** O porquê, o padrão e o que é regra. Lê-se uma vez |
| [`_modelo-cobertura-culto.md`](03_CONTENT/roteiros/_modelo-cobertura-culto.md) | **O roteiro.** Uma página, em ordem de acontecimento, para usar com o celular na mão |

A cada culto, copie o roteiro para
`03_CONTENT/roteiros/[ano-mes]/roteiro-cobertura-[aaaa-mm-dd].md`, preencha o
cabeçalho e vá marcando. O que sobra no fim da semana é um registro do que foi
gravado — e do que faltou.

---

## 🎨 Design System

A identidade visual mora em [`00_BRAND/`](00_BRAND/) e o índice é
[`00_BRAND/design-system.md`](00_BRAND/design-system.md). **Leia antes de abrir
qualquer arquivo de arte.**

| Arquivo | Para quê |
|---|---|
| [`00_BRAND/design-system.md`](00_BRAND/design-system.md) | **Comece por aqui.** Índice e fundamentos |
| [`00_BRAND/preview.html`](00_BRAND/preview.html) | O sistema aplicado — abra no navegador |
| [`00_BRAND/cores/paleta.md`](00_BRAND/cores/paleta.md) | Cores, papéis e contraste conferido |
| [`00_BRAND/tipografia/tipografia.md`](00_BRAND/tipografia/tipografia.md) | Famílias, escala e o caso do versículo |
| [`00_BRAND/logo/logo.md`](00_BRAND/logo/logo.md) | Versões, respiro, tamanho mínimo, proibições |
| [`00_BRAND/grafismos/grafismos.md`](00_BRAND/grafismos/grafismos.md) | Anatomia do post e formatos |
| [`00_BRAND/tokens/`](00_BRAND/tokens/) | JSON, CSS, SCSS e preset Tailwind |

```bash
# regenera CSS, SCSS e Tailwind a partir de 00_BRAND/tokens/tokens.json
python3 _META/automacao/gerar-tokens.py
```

> [!IMPORTANT]
> **Nunca escreva um hex à mão.** A fonte da verdade é o `tokens.json`. Precisa
> de um valor novo? Adicione lá e regenere — a mudança chega em todos os canais
> de uma vez.
>
> Enquanto houver `null` no `tokens.json`, o script **se recusa a gerar** e
> lista o que falta. É de propósito: melhor não ter o arquivo do que ter o
> arquivo com valor chutado.

---

## 🤖 Trabalhando com IA

Duas camadas, com funções diferentes:

| | Para quê |
|---|---|
| [`AGENTS.md`](AGENTS.md) | **As regras.** Contexto da igreja e o que nenhum agente pode violar. Lido automaticamente por Claude Code, Cursor e similares |
| [`.claude/skills/comunicacao-pibac/`](.claude/skills/comunicacao-pibac/) | **O agente de comunicação.** Tom de voz, fidelidade bíblica e o padrão de cada canal. Carrega sozinho quando o pedido é de conteúdo |

No Claude Code, dentro deste repositório, a skill dispara sozinha — ou chame na
mão com `/comunicacao-pibac`. Em outra ferramenta, cole o `SKILL.md` como
instrução do sistema. Detalhes em [`_META/skills/README.md`](_META/skills/README.md).

---

## 📚 Documentação

| Arquivo | Para quê |
|---|---|
| [`_META/GUIA-RAPIDO.md`](_META/GUIA-RAPIDO.md) | **Comece por aqui** se você é novo no time |
| [`_META/NOMENCLATURA.md`](_META/NOMENCLATURA.md) | Como nomear qualquer arquivo |
| [`_META/PIPELINE.md`](_META/PIPELINE.md) | Como funciona a automação |
| [`_META/VERSIONAMENTO.md`](_META/VERSIONAMENTO.md) | Como usar Git neste projeto |
| [`_META/checklist-entrega.md`](_META/checklist-entrega.md) | Checklist antes de entregar |
| [`_META/CHANGELOG.md`](_META/CHANGELOG.md) | Histórico do projeto |

---

## 📊 Status

| Fase | Status |
|---|---|
| Repositório criado | ✅ 17/09/2026 |
| Briefing | 🟡 parcial — levantado do site, falta onboarding |
| Cobertura de culto | ✅ manual e roteiro prontos para uso |
| Design system | 🟡 esqueleto pronto — decisões de cor e tipografia pendentes |
| Identidade visual | ⏳ `00_BRAND/logo/` vazio, aguardando os vetores originais |
| Estratégia de conteúdo | ⏳ |
| Produção | ⏳ |
| Publicação | ⏳ |

> [!IMPORTANT]
> **Os três próximos passos, nesta ordem:**
> 1. Reunião de onboarding para fechar os `#CONFIRMAR` do
>    [`briefing`](01_STRATEGY/briefing-cliente.md) — principalmente **quem aprova
>    publicação** e **qual a forma oficial do nome** ("em" ou "de" Águas Claras).
> 2. Conseguir os arquivos originais da marca (`.ai`/`.svg`) e colocá-los em
>    `00_BRAND/`. Até lá, nada de arte.
> 3. Aprovar o modelo de autorização de uso de imagem — a igreja produz conteúdo
>    com crianças toda semana.
