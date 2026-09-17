---
tipo: guia-de-pasta
cliente: pibac
titulo: 05_EXPORTS
usar_quando: precisar saber o que vai, e o que nao vai, em 05_EXPORTS/
status: ativo
atualizado: 2026-09-10
---

# 05_EXPORTS — Entregáveis finais

> **O que vai ao ar.** Arquivo achatado, no formato certo, pronto para o
> destino.

> [!IMPORTANT]
> **Só se publica de `_PUBLISH-READY/`.** Qualquer outra pasta — inclusive aqui
> na raiz — é trabalho em revisão. Essa é a regra que impede peça errada de ir ao
> ar.

## Como se organiza

```
05_EXPORTS/
├── _PUBLISH-READY/           aprovado, pode publicar  ✅
└── campanha-mes-ano/         exports em revisão
    ├── social/instagram/
    ├── social/tiktok/
    ├── print/
    └── web/
```

Você cria a pasta da campanha com o mesmo nome usado em `04_PRODUCTION/` — assim
dá para atravessar do editável ao entregável sem procurar.

## O caminho de uma peça

```
03_CONTENT      04_PRODUCTION       05_EXPORTS         _PUBLISH-READY
  texto     →      arte        →     export       →      aprovado
                                                          ↓
                                                       publicado
```

Peça só atravessa para `_PUBLISH-READY/` **depois da aprovação do cliente**.

## Formato por destino

| Destino | Formato |
|---|---|
| Instagram, feed | `.png` ou `.jpg`, 1080×1350 (4:5) ou 1080×1080 (1:1) |
| Story, Reels, TikTok | `.mp4` ou `.jpg`, 1080×1920 (9:16) |
| YouTube, capa | `.jpg`, 1280×720 (16:9) |
| Impressão | `.pdf` com marca de corte e sangria, CMYK |
| Web | `.webp` otimizado |

## Como nomear

```
_PUBLISH-READY/post-tema-do-post-v2.png
campanha-set-2026/social/instagram/carrossel-tema-p1-v1.png
campanha-set-2026/print/outdoor-local-v3.pdf
```

> [!WARNING]
> **Nunca** `final`, `aprovado` ou `ok` no nome. Aprovação é status no
> `manifest.json` — um arquivo chamado "aprovado" hoje pode ser reprovado amanhã,
> e aí o nome mente.

📖 [`_META/checklist-entrega.md`](../_META/checklist-entrega.md) · [`_META/PIPELINE.md`](../_META/PIPELINE.md)
