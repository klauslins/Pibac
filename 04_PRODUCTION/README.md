---
tipo: guia-de-pasta
cliente: pibac
titulo: 04_PRODUCTION
usar_quando: precisar saber o que vai, e o que nao vai, em 04_PRODUCTION/
status: ativo
atualizado: 2026-09-10
---

# 04_PRODUCTION — Arte em andamento

> **A oficina.** Arquivo editável, trabalho em progresso, versão que ainda vai
> mudar. Nada aqui é publicável.

## Como se organiza

Duas coisas convivem nesta pasta:

| | O que é |
|---|---|
| `templates/` | Bases reutilizáveis por formato — o ponto de partida |
| `campanha-mes-ano/` | **Você cria.** Uma pasta por campanha, com o trabalho real |

### Templates disponíveis

`post-feed-1x1/` · `carrossel-1x1/` · `story-9x16/` · `reels-9x16/` ·
`thumbnail-16x9/` · `cartao-visita/` · `outdoor-14x4/`

Template é base, não entregável: duplique para a pasta da campanha e trabalhe lá.
Editar o template direto quebra a próxima campanha.

### Criando uma campanha

```
04_PRODUCTION/lancamento-conteudo-set-2026/
├── fontes/      arquivo editável: .ai, .psd, .fig
└── previas/     JPG leve para aprovação interna
```

Nome da pasta: `assunto-mes-ano`, minúsculo e com hífen.

## O que NÃO vai aqui

| Isso | Vai em |
|---|---|
| Export final aprovado | `05_EXPORTS/` |
| Logo original da marca | `00_BRAND/` *(não edite lá — traga cópia)* |
| Foto bruta de câmera | `06_MEDIA/fotos/originais/` *(fora do Git)* |
| Arquivo acima de 100 MB | `08_MASTERS/` *(fora do Git)* |

## Como nomear

```
fontes/post-tema-do-post-v1.ai
fontes/carrossel-tema-p1-v2.psd
previas/post-tema-do-post-v1.jpg
```

Suba `v1` → `v2` quando a mudança é **conceitual** (outra proposta, outra
direção). Ajuste de kerning ou typo mantém o `vN` — o Git guarda o histórico.

## Subindo arquivo aqui

`.ai`, `.psd`, `.fig`, `.eps` vão para **Git LFS**.

- **Terminal / GitHub Desktop:** normal, o LFS é transparente
- **Arrastar no site do GitHub:** ⚠️ não use para arquivo de design — fura o LFS
- **Acima de 100 MB:** o GitHub recusa. Vai para `08_MASTERS/`, fora do Git,
  indexado em `_META/automacao/manifest.json`

📖 [`_META/PIPELINE.md`](../_META/PIPELINE.md) · [`_META/NOMENCLATURA.md`](../_META/NOMENCLATURA.md)
