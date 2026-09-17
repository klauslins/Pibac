---
tipo: guia-de-pasta
cliente: pibac
titulo: 07_IMPRESSOS
usar_quando: precisar saber o que vai, e o que nao vai, em 07_IMPRESSOS/
status: ativo
atualizado: 2026-09-10
---

# 07_IMPRESSOS — Peças físicas

> **O que vai para a gráfica.** Arte final com especificação de impressão, não
> arquivo de tela.

## O que vai aqui

| Subpasta | O que guarda |
|---|---|
| `cartao-visita/` | Cartão de visita, frente e verso |
| `timbrado/` | Papel timbrado, envelope, pasta |
| `outdoor/` | Outdoor, painel, banner de rua |

Peça impressa nova que não se encaixa nessas três? Crie a pasta em kebab-case:
`folder/`, `adesivo/`, `bandeira/`.

## O que a gráfica precisa

| Item | Padrão |
|---|---|
| Formato | `.pdf` vetorial *(ou `.eps` se a gráfica pedir)* |
| Cor | **CMYK** — nunca RGB |
| Sangria | 3 mm além do corte |
| Marca de corte | Incluída |
| Fonte | Convertida em curvas |
| Resolução de imagem | 300 dpi no tamanho final |

> [!WARNING]
> **RGB na gráfica sai com outra cor.** O azul da tela não é o azul do papel.
> Converta para CMYK e, quando a cor for crítica para a marca, especifique o
> Pantone — a referência está em [`00_BRAND/cores/`](../00_BRAND/cores/).

## Como nomear

```
cartao-visita/card-nome-pessoa-frente-v1.pdf
cartao-visita/card-nome-pessoa-verso-v1.pdf
outdoor/outdoor-local-v3.pdf
timbrado/timbrado-cliente-v1.docx
```

## Antes de mandar imprimir

- [ ] CMYK, sangria de 3 mm, marca de corte
- [ ] Fonte em curvas
- [ ] Imagem a 300 dpi
- [ ] Texto revisado por outra pessoa — reimpressão custa dinheiro
- [ ] Exigência legal do segmento conferida *(campanha eleitoral: nome, número,
      partido, CNPJ, gráfica e tiragem)*
- [ ] Prova digital aprovada pelo cliente

📖 [`_META/checklist-entrega.md`](../_META/checklist-entrega.md)
