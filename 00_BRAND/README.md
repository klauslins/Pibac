---
tipo: guia-de-pasta
cliente: pibac
titulo: 00_BRAND
usar_quando: precisar saber o que vai, e o que nao vai, em 00_BRAND/
status: ativo
atualizado: 2026-09-10
---

# 00_BRAND — Identidade visual

> **Fonte da verdade da marca.** Se um logo, cor ou fonte está em desacordo com
> outra pasta, esta aqui é a que vale.
>
> 📖 **Comece por [`design-system.md`](design-system.md)** — é o índice de tudo
> que está aqui. Para ver o sistema aplicado, abra [`preview.html`](preview.html)
> no navegador.

> [!WARNING]
> **Pasta imutável.** Nada aqui é alterado, movido ou renomeado sem aprovação
> explícita de branding. Se você precisa de uma variação que não existe, ela é
> criada em `04_PRODUCTION/` — não editando o original daqui.

## O que vai aqui

Os arquivos oficiais da marca, do jeito que o cliente aprovou: logotipo em todas
as versões, tipografia licenciada, especificação de cor e mockups de aplicação.

| Subpasta | O que guarda |
|---|---|
| `logo/horizontal/` | Logotipo deitado — `ai/`, `eps/`, `png/`, `svg/` |
| `logo/vertical/` | Logotipo empilhado — mesmas quatro extensões |
| `logo/simbolo/` | Símbolo isolado, sem texto — mesmas quatro extensões |
| `cores/` | Paleta oficial: hex, RGB, CMYK, Pantone |
| `tipografia/primaria/` | Fonte de título, com a licença junto |
| `tipografia/secundaria/` | Fonte de apoio |
| `tipografia/textos/` | Fonte de corpo de texto |
| `mockups/` | Aplicações da marca para apresentação |

**Por que quatro extensões do mesmo logo:** `svg` para web e telas, `ai` para
edição, `eps` para a gráfica, `png` para uso rápido com fundo transparente.
A gráfica quase sempre pede `eps` ou `pdf` vetorial — não mande `png`.

## O que NÃO vai aqui

| Isso | Vai em |
|---|---|
| Arte criada usando a marca | `04_PRODUCTION/` |
| Peça pronta para publicar | `05_EXPORTS/` |
| Foto do cliente | `06_MEDIA/fotos/tratadas/` |
| Manual da marca em PDF | Aqui mesmo, na raiz desta pasta |

## Como nomear

```
logo-h-oficial-v1.svg        logo horizontal, versão oficial
logo-v-preto-v1.eps          logo vertical, versão preta
simbolo-branco-v1.png        símbolo isolado, branco
```

Arquivo de fonte é exceção: mantém o nome técnico original
(`Sora-SemiBold.ttf`), porque ele identifica o peso e a família.

## Subindo arquivo aqui

`.ai`, `.eps` e `.psd` vão para **Git LFS** automaticamente.

- **Terminal:** normal — `git add`, `git commit`, `git push`. O LFS é transparente.
- **GitHub Desktop:** normal também, ele respeita o LFS.
- **Arrastar no site do GitHub:** ⚠️ **não faça com arquivo de design.** O upload
  web ignora o LFS e sobe o binário cru, inchando o repositório para sempre.

📖 [`_META/NOMENCLATURA.md`](../_META/NOMENCLATURA.md) · [`_META/GUIA-RAPIDO.md`](../_META/GUIA-RAPIDO.md)
