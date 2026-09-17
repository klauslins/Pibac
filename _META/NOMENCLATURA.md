---
tipo: documentacao
cliente: pibac
titulo: Nomenclatura
usar_quando: nomear ou renomear qualquer arquivo
status: ativo
atualizado: 2026-09-14
fonte: _AKZA/docs/NOMENCLATURA.md
---

# Nomenclatura — Como nomear qualquer arquivo

> Padrão Akza v1.0. Referência completa.
> Para o resumo, veja [`GUIA-RAPIDO.md`](GUIA-RAPIDO.md).

---

## O padrão

```
[tipo]-[assunto]-[variacao]-v[N].[ext]
   │       │          │        │    │
   │       │          │        │    └─ sempre minúscula: .png, .ai, .mp4
   │       │          │        └────── versão numerada, começa em v1
   │       │          └─────────────── opcional: cor, formato, direção de arte
   │       └────────────────────────── do que se trata, em kebab-case
   └────────────────────────────────── categoria da peça
```

**Só `tipo`, `assunto` e `vN` são obrigatórios.** `variacao` entra quando existe
mais de uma versão da mesma peça convivendo.

---

## Regras invioláveis

| Regra | ✅ | ❌ |
|---|---|---|
| Apenas minúsculas | `post-lancamento-v1.png` | `Post-Lancamento-V1.png` |
| Sem acentos | `tema-do-post` | `antecipação-de-riscos` |
| Sem espaços — use hífen | `guia-de-conteudo` | `guia de conteudo` |
| Sem `_`, `()`, `[]`, `#`, `&` | `logo-h-oficial-v1` | `LOGO (HORIZONTAL)_v1` |
| Versão numerada, nunca "final" | `v1`, `v2`, `v3` | `final`, `FINAL2`, `agora-vai` |
| Hífen simples, nunca duplo | `post-tema-v1` | `post--tema-v1` |

> [!IMPORTANT]
> **Por que tanto rigor?** Os scripts de automação leem os nomes dos arquivos
> para saber o que fazer com cada peça: qual rede social, qual dimensão, qual
> versão é a mais recente. Um espaço ou acento faz o script quebrar ou, pior,
> processar o arquivo errado silenciosamente.

---

## Tipos válidos

### Peças digitais
| Tipo | Uso | Exemplo |
|---|---|---|
| `post` | Post de feed (1:1 ou 4:5) | `post-tema-do-post-v1.png` |
| `carrossel` | Post de múltiplas páginas | `carrossel-tema-do-carrossel-p1-v1.png` |
| `story` | Story (9:16) | `story-bastidores-captacao-v1.jpg` |
| `reels` | Reels / Shorts / TikTok (9:16) | `reels-porta-voz-apresentacao-v1.mp4` |
| `thumbnail` | Capa de vídeo do YouTube | `thumbnail-tema-do-video-v1.jpg` |
| `banner` | Banner de site ou anúncio | `banner-trafego-pago-colorido-v1.jpg` |

### Marca
| Tipo | Uso | Exemplo |
|---|---|---|
| `logo-h` | Logotipo horizontal | `logo-h-oficial-v1.svg` |
| `logo-v` | Logotipo vertical | `logo-v-preto-v1.svg` |
| `simbolo` | Símbolo isolado | `simbolo-bronze-branco-v1.svg` |

### Impressos
| Tipo | Uso | Exemplo |
|---|---|---|
| `outdoor` | Outdoor / painel | `outdoor-local-v3.pdf` |
| `card` | Cartão de visita | `card-nome-pessoa-frente-v1.pdf` |
| `timbrado` | Papel timbrado | `timbrado-PIB-Aguas-Claras-v1.docx` |

### Texto
| Tipo | Uso | Exemplo |
|---|---|---|
| `roteiro` | Roteiro de vídeo | `roteiro-tema-do-video-v1.docx` |
| `copy` | Legenda / texto de anúncio | `copy-instagram-setembro-v1.md` |
| `briefing` | Briefing de campanha | `briefing-trafego-pago-set-2026.md` |
| `calendario` | Calendário editorial | `calendario-mar-mai-2026.pdf` |

---

## Variações

### Cor e fundo
`colorido` · `oficial` · `branco` · `preto` · `cinza` · `bronze-branco` ·
`bronze-azul` · `fundo-azul` · `fundo-escuro` · `fundo-branco` · `preto-fundo-bronze`

### Formato e direção
`h` (horizontal) · `v` (vertical) · `1x1` · `4x5` · `9x16` · `16x9`

### Página (carrosséis)
`p1` · `p2` · `p3` … — sempre antes do `vN`:
```
carrossel-tema-do-carrossel-p1-v2.png
carrossel-tema-do-carrossel-p2-v2.png
```

---

## Datas e períodos

Sempre **do maior para o menor** — assim a ordenação alfabética vira ordenação
cronológica automaticamente.

| Granularidade | Formato | Exemplo |
|---|---|---|
| Dia | `YYYY-MM-DD` | `post-data-comemorativa-2026-09-22-v1.png` |
| Mês (pasta) | `YYYY-MM` | `03_CONTENT/roteiros/2026-09/` |
| Trimestre (pasta) | `YYYY-QN` | `02_PLANNING/calendario/2026-Q3/` |
| Campanha | `slug-mes-ano` | `04_PRODUCTION/campanha-mes-ano/` |

```
✅ calendario-2026-09.pdf        → ordena certo
❌ calendario-set-2026.pdf       → "abr" vem antes de "set" no alfabeto
❌ calendario-09-2026.pdf        → mistura anos ao ordenar
```

---

## Nomes de pasta

| Nível | Regra | Exemplo |
|---|---|---|
| Pastas raiz numeradas | `NN_MAIUSCULA` | `04_PRODUCTION` |
| Todo o resto | `kebab-case` minúsculo | `linhas-editoriais/` |
| Campanhas | `assunto-mes-ano` | `lancamento-conteudo-set-2026/` |
| Prefixo `_` | Pastas de sistema, fora do fluxo | `_META/`, `_PUBLISH-READY/`, `_fontes/` |

O `_` faz a pasta ordenar antes ou depois das demais e sinaliza visualmente
"isto não é etapa do fluxo".

---

## Versionamento no nome

**`v1` é o começo, sempre.** Não existe arquivo sem versão.

Suba a versão quando a mudança é **conceitual** — outra proposta, outra direção,
uma revisão que o cliente pediu e quer comparar lado a lado.

Ajuste pequeno (kerning, typo, 2px de margem)? **Mantenha o `vN`** e deixe o Git
registrar o histórico.

```
post-tema-v1.png  →  cliente pede outra abordagem  →  post-tema-v2.png  ✅
post-tema-v1.png  →  corrigiu um typo              →  post-tema-v1.png  ✅
```

> [!WARNING]
> **Nunca** use `final`, `FINAL`, `final2`, `aprovado`, `ok`, `novo`, `atual`.
> Aprovação é um **status no `manifest.json`**, não um pedaço do nome do arquivo.
> Um arquivo chamado `aprovado` hoje pode ser reprovado amanhã — e aí o nome mente.

---

## Casos especiais

**Arquivos de terceiros (fontes, licenças):** mantenha o nome original quando ele
carrega significado técnico. `Inter_18pt-SemiBold.ttf` → `inter-18pt-semibold.ttf`
(normaliza) mas **não** vire `fonte-1.ttf` (perde a informação).

**Documentos com versão do cliente:** se o cliente manda `Contrato V.3.docx`,
normalize para `contrato-v3.docx` — a numeração dele vira a sua.

**Múltiplos idiomas:** sufixo ISO antes do `vN` → `post-tema-en-v1.png`

---

## Ferramentas

```bash
# Simula a renomeação — não altera nada
python3 _META/automacao/rename-assets.py --dry-run 05_EXPORTS/campanha/

# Aplica
python3 _META/automacao/rename-assets.py 05_EXPORTS/campanha/

# Recursivo (subpastas)
python3 _META/automacao/rename-assets.py --recursive 05_EXPORTS/

# Verifica o projeto inteiro contra o padrão
python3 _META/automacao/validar-projeto.py
```

---

## Isenções

A regra de minúsculas não se aplica a:

- **Nomes canônicos da indústria** — `README.md`, `AGENTS.md`, `CHANGELOG.md`, `LICENSE`
- **`00_BRAND/tipografia/`** — nome de arquivo de fonte tem significado técnico
- **`_META/` e `.github/`** — documentação e configuração seguem convenção própria
- **Artefatos de ferramenta** — arquivos cujo nome é definido por um programa e está referenciado dentro dos próprios arquivos. Hoje: `*.dc.html` e `canvas.json` (canvas do Claude Design). Renomear quebra a edição.

Se aparecer uma ferramenta nova com convenção própria, acrescente em `SUFIXOS_FERRAMENTA` ou `NOMES_FERRAMENTA` no `validar-projeto.py` — e registre aqui. **Não** renomeie o artefato para satisfazer a regra.
