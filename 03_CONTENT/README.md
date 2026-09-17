---
tipo: guia-de-pasta
cliente: pibac
titulo: 03_CONTENT
usar_quando: precisar saber o que vai, e o que nao vai, em 03_CONTENT/
status: ativo
atualizado: 2026-09-10
---

# 03_CONTENT — Texto, antes da arte

> **A palavra vem primeiro.** Roteiro, legenda e copy nascem aqui e só depois
> viram arte em `04_PRODUCTION/`.

Separar texto de arte permite revisar e aprovar o conteúdo sem esperar o design
— e evita refazer peça inteira porque a legenda mudou.

## O que vai aqui

| Subpasta | O que guarda |
|---|---|
| `copy/social/` | Legenda de post, story, carrossel |
| `copy/ads/` | Texto de anúncio pago |
| `copy/email/` | E-mail marketing, newsletter |
| `roteiros/` | Roteiro de vídeo, uma pasta por mês: `2026-09/` |
| `scripts-video/` | Script técnico: plano, corte, trilha, legenda |

**Roteiro × script:** o roteiro é o que se diz; o script é como se filma e monta.

## O que NÃO vai aqui

| Isso | Vai em |
|---|---|
| A arte com o texto aplicado | `04_PRODUCTION/` |
| O vídeo editado | `06_MEDIA/videos/editados/` |
| Tom de voz e o que nunca dizer | `01_STRATEGY/guia-de-conteudo/` |

## Como nomear

```
copy/social/copy-instagram-setembro-v1.md
roteiros/2026-09/roteiro-tema-do-video-v1.docx
scripts-video/script-reels-bastidores-v1.md
```

Markdown é preferível para copy — o Git mostra exatamente qual palavra mudou
entre `v1` e `v2`, o que não acontece com `.docx`.

📖 [`_META/NOMENCLATURA.md`](../_META/NOMENCLATURA.md) · [`_META/PIPELINE.md`](../_META/PIPELINE.md)
