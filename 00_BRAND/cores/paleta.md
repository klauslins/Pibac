---
tipo: marca
cliente: pibac
titulo: Paleta
usar_quando: precisar decidir ou conferir qual cor usar numa peca
status: rascunho
atualizado: 2026-09-17
---

# Paleta — PIBAC

> **Fonte da verdade:** [`../tokens/tokens.json`](../tokens/tokens.json).
> Este documento **explica** as cores; o `tokens.json` as **define**. Se os dois
> divergirem, o `tokens.json` está certo.
> **Status:** a definir.

---

## As cores

<!-- PREENCHER: uma linha por cor. O papel é o que importa — sem ele, todo mundo
     usa a cor bonita para tudo e o sistema morre na terceira peça. -->

| | Nome | Hex | Token | Papel |
|---|---|---|---|---|
| | **A definir** | `#______` | `cor.marca.primaria` | |
| | | `#______` | `cor.marca.secundaria` | |
| | | `#______` | `cor.marca.apoio` | |

**Neutras** — `cor.neutra.clara`, `cor.neutra.media`, `cor.neutra.escura`: a
escada do fundo ao texto.

---

## Proporção

<!-- PREENCHER. Sem regra de proporção, a peça vira colcha de retalhos. -->

Uma regra que funciona bem e vale como ponto de partida: **60 / 30 / 10** —
60% da área numa cor de fundo, 30% na secundária, 10% na cor de apoio.

---

## Contraste conferido

Preencha rodando cada par em [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/).
**Só entra aqui o que foi medido** — nada de "parece legível".

| Texto | Sobre | Razão | Corrido (4.5:1) | Grande (3:1) |
|---|---|---|---|---|
| | | | | |

### Combinações proibidas

<!-- PREENCHER com o que reprovou no teste. Escrever o que NÃO pode vale mais
     que escrever o que pode: é o que o time consulta na hora da dúvida. -->

---

## Cor no projetor

O culto é o maior "canal" da igreja e o pior meio técnico: projetor lava cor,
perde contraste e esquenta o branco.

<!-- PREENCHER depois de testar no projetor da igreja, não na tela do Mac. -->

| Situação | Decisão |
|---|---|
| Fundo de slide de letra de música | |
| Cor de texto no slide | |
| Cor que **não** funciona projetada | |

---

## Como usar no código

```bash
python3 _META/automacao/gerar-tokens.py
```

Gera `tokens.css`, `tokens.scss` e `tailwind.preset.js` a partir do
`tokens.json`. No CSS as variáveis saem como `--pibac-cor-marca-primaria`.

> [!CAUTION]
> **Nunca copie um hex daqui para o código.** Se a cor mudar, o `tokens.json`
> muda e tudo se atualiza junto — menos o hex que alguém colou na mão.
