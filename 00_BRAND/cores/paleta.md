---
tipo: marca
cliente: pibac
titulo: Paleta
usar_quando: precisar decidir ou conferir qual cor usar numa peca
status: ativo
atualizado: 2026-10-16
---

# Paleta — PIBAC

> **Fonte da verdade:** [`../tokens/tokens.json`](../tokens/tokens.json).
> Este documento **explica** as cores; o `tokens.json` as **define**. Se os dois
> divergirem, o `tokens.json` está certo.

---

## De onde ela vem

A paleta nasce do **azul do próprio logotipo** — matiz 202°. A referência
escolhida pela igreja (coastal, neutra) usa azuis de matiz 211°: **nove graus de
diferença, a mesma família**. O que separava os dois era só saturação — 100% no
logo, 20–56% na referência.

Por isso o sistema não trocou o azul da igreja por outro. Ele **abriu o azul da
igreja em cinco tons**, no registro calmo da referência, e manteve o logotipo
intocado como o ponto mais saturado de tudo. É assim que a marca aparece sem
gritar: tudo em volta é sóbrio.

A cor **terra** entra como contraponto quente, e é **cor de detalhe** — foi essa
a decisão.

---

## As cores

| | Nome | Hex | Token | Papel |
|---|---|---|---|---|
| 🔵 | **Marca** | `#007CC2` | `cor.marca.primaria` | **A cor principal da igreja.** Bloco, fundo, barra, título grande — nunca texto corrido |
| 💧 | **Azul claro** | `#AFD4E9` | `cor.marca.clara` | Fundo de respiro, bloco claro |
| 🩵 | **Azul médio** | `#7A97A8` | `cor.marca.media` | Apoio, divisória, estado desativado |
| 🟦 | **Azul profundo** | `#475E6B` | `cor.marca.profunda` | Fundo escuro, barra, rodapé |
| 🟤 | **Terra** | `#A68A69` | `cor.marca.apoio` | **Detalhe:** fio, ícone, selo, número grande |
| ⬜ | **Areia** | `#EFEAE4` | `cor.neutra.areia` | O fundo claro padrão, quente |
| ⬛ | **Tinta** | `#242D33` | `cor.neutra.tinta` | **Todo o texto.** Quase-preto azulado, no matiz da marca |

Completam o conjunto `cor.neutra.media` `#ABB7C4` (borda, separador) e
`cor.texto.suave` `#5C727F` (legenda, crédito).

> [!IMPORTANT]
> **Decidido em 16/10/2026: a cor principal da igreja é `#007CC2`.**
>
> | | Valor | Origem |
> |---|---|---|
> | **Cor principal do sistema** | **`#007CC2`** | decisão da igreja |
> | Logotipo em tela | `#009BDB` | o SVG, exportado pelo Illustrator |
> | Logotipo no arquivo | `CMYK 100/0/0/0` | ciano de escala |
>
> Os dois ainda não batem, e isso tem consequência visível: numa peça que use a
> cor do sistema ao lado do logotipo, os azuis ficam diferentes.
>
> **O que resolve:** exportar do Illustrator uma versão do logotipo em
> `#007CC2`, para uso em tela. O arquivo em ciano continua valendo para gráfica,
> onde a cor é `CMYK 100/0/0/0`.
>
> Até isso acontecer, não encoste a cor do sistema no logotipo.

> [!NOTE]
> **A cor `tinta` não veio da referência — foi derivada.** A paleta escolhida não
> tinha nenhuma cor escura o bastante para texto corrido: a melhor delas chegava
> a 7:1 e as outras reprovavam. Sem um quase-preto, o sistema não teria onde
> escrever. Ela é o azul da marca levado a 17% de luminosidade, então pertence à
> família.

---

## Proporção — a cor principal manda

Com `#007CC2` como cor principal, a regra deixa de ser "um acento de 10%".

### Cada peça escolhe um dominante

Marca **ou** areia. Nunca as duas disputando o mesmo quadro — é isso que faz
uma peça parecer decidida e a outra parecer indecisa.

| A peça é… | Dominante | Como fica |
|---|---|---|
| **Convite, chamada, evento** | **Marca** `#007CC2` | Fundo azul, texto **branco** e grande |
| **Texto, informação, reflexão** | **Areia** `#EFEAE4` | Fundo claro, marca nos títulos e blocos |
| **Slide de culto, rodapé, barra** | **Azul profundo** `#475E6B` | Fundo escuro, texto areia |

Dentro da peça, como referência: **~50% o dominante · ~35% o par · ~10% os azuis
de apoio · ~5% terra.** O terra continua sendo detalhe — ele nunca cresce.

> [!CAUTION]
> **Sobre a cor principal, o texto é branco puro. Só ele.**
>
> | Texto sobre `#007CC2` | Contraste | Corpo | Título grande |
> |---|---|---|---|
> | **Branco `#FFFFFF`** | 4,50:1 | ✅ | ✅ |
> | Areia `#EFEAE4` | 3,77:1 | ❌ | ✅ |
> | Tinta `#242D33` | 3,11:1 | ❌ | ✅ |
>
> O reflexo natural é usar a areia em cima do azul, porque ela é a cor clara do
> sistema. **Reprova para texto corrido.** Em bloco de marca: branco, e de
> preferência grande.
>
> Isso é só para a cor principal. Sobre o **azul profundo** a areia funciona bem
> (5,70:1) — é lá que ela é a cor de texto certa.

## Contraste conferido

Medido com a régua da WCAG 2.1. **Só entra aqui o que foi medido.**

| Cor | Sobre branco | Sobre areia | Texto corrido? | Texto grande? |
|---|---|---|---|---|
| **Tinta** `#242D33` | 14,02:1 | 11,72:1 | ✅ | ✅ |
| **Azul profundo** `#475E6B` | 6,82:1 | 5,70:1 | ✅ | ✅ |
| **Texto suave** `#5C727F` | 5,04:1 | 4,21:1 | ✅ sobre branco | ✅ |
| **Marca** `#007CC2` | 4,50:1 | 3,77:1 | ⚠️ raspando | ✅ |
| **Terra** `#A68A69` | 3,25:1 | 2,72:1 | ❌ | ✅ só sobre branco |
| **Azul médio** `#7A97A8` | 3,08:1 | 2,57:1 | ❌ | ⚠️ |
| **Azul claro** `#AFD4E9` | 1,57:1 | 1,31:1 | ❌ | ❌ |

### Combinações proibidas

- **Terra como texto pequeno**, sobre qualquer fundo claro. Ele é detalhe — fio,
  ícone, selo, número grande. Legenda em terra não se lê.
- **Azul claro ou azul médio como texto**, em qualquer tamanho de corpo.
- **Marca (`#007CC2`) em texto corrido.** 4,50:1 passa no papel e falha na vida:
  some no projetor e no celular ao sol. Título grande sim, parágrafo não.
- **Texto branco sobre a marca.** 4,50:1 — reprova para corpo. Sobre azul
  profundo, sim.

---

## Cor no projetor

O culto é o maior "canal" da igreja e o pior meio técnico: o projetor lava a cor
e come o contraste.

| Situação | Decisão |
|---|---|
| Fundo de slide de letra | **Azul profundo** `#475E6B` ou tinta — nunca areia |
| Cor do texto no slide | **Areia** `#EFEAE4` sobre o escuro. Mira em 7:1 |
| Cor que **não** funciona projetada | Azul claro e terra: somem na luz ambiente |

> Teste no projetor da igreja antes de fechar qualquer arte de culto, não na
> tela do computador.

---

## O que NÃO é da marca

> [!IMPORTANT]
> **Preto e dourado não fazem parte deste sistema.** Eles são a paleta do **tema
> de 19 anos de 2026** e vivem em
> [`../../02_PLANNING/briefings/19-anos-2026.md`](../../02_PLANNING/briefings/19-anos-2026.md).
>
> A diferença importa: o tema troca todo ano, a marca não. Misturar os dois faz
> com que, em 2027, metade do sistema fique errada sozinha.

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
