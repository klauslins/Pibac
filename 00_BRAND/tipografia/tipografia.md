---
tipo: marca
cliente: pibac
titulo: Tipografia
usar_quando: for escolher fonte, tamanho ou hierarquia de texto numa peca
status: rascunho
atualizado: 2026-09-17
---

# Tipografia — PIBAC

> **Fonte da verdade:** [`../tokens/tokens.json`](../tokens/tokens.json), bloco `fonte`.
> **Arquivos:** `primaria/`, `secundaria/`, `textos/` — nesta mesma pasta.
> **Status:** ativo desde 16/10/2026.

---

## As famílias

Duas, e cada uma tem uma função que a outra não cobre.

| Registro | Família | Token | Quando |
|---|---|---|---|
| **Anúncio** | **Archivo Expanded**, Bold e Black | `fonte.familia.display` | Convite, chamada de culto, evento. **Sempre caixa alta** |
| **Afirmação e apoio** | **Montserrat**, Light a Bold | `fonte.familia.texto` | Frase pastoral, versículo, legenda, endereço, crédito |

Ambas são do **Google Fonts, licença OFL** — livres para impresso, web e
projeção, e instalam em qualquer máquina da equipe.

```
Archivo:    https://fonts.google.com/specimen/Archivo
Montserrat: https://fonts.google.com/specimen/Montserrat
```

> **A Archivo é variável, com eixo de largura.** O que se quer aqui é a largura
> **Expanded** (`wdth` em 125) no peso 700–900. No CSS:
> `font-family: Archivo; font-variation-settings: 'wdth' 125; font-weight: 900`.
> Se a máquina só tiver a estática, o nome do arquivo é `Archivo Expanded Black`.

---

## A regra que decide qual usar

> ## Caixa alta convida. Caixa baixa acolhe.

Não é escolha estética — é a intenção da peça.

| A peça está… | Registro | Exemplo |
|---|---|---|
| **Chamando** alguém para vir | Archivo, **CAIXA ALTA** | "HOJE TEM CULTO", "VENHA DOMINGO ÀS 18H" |
| **Consolando, ensinando, afirmando** | Montserrat, **caixa baixa** | "Deus muda o medo", "Uma igreja não é só um lugar" |

**Nunca misture os dois registros no mesmo quadro.** Peça que mistura perde a
intenção: vira anúncio com cara de devocional, ou devocional com cara de
anúncio.

---

## Escala

Já vem definida nos tokens — escala modular de razão 1.25, de `xs` a `5xl`.
É encanamento, não identidade: pode trocar, mas troque no `tokens.json`.

| Token | Tamanho | Uso sugerido |
|---|---|---|
| `fonte.tamanho.5xl` | 3.815rem | Capa de carrossel, título de evento |
| `fonte.tamanho.4xl` | 3.052rem | Título de post |
| `fonte.tamanho.3xl` | 2.441rem | Subtítulo |
| `fonte.tamanho.2xl` | 1.953rem | Destaque dentro do texto |
| `fonte.tamanho.xl` | 1.563rem | Intertítulo |
| `fonte.tamanho.lg` | 1.25rem | Corpo grande, legenda de story |
| `fonte.tamanho.md` | 1rem | Corpo |
| `fonte.tamanho.sm` | 0.875rem | Apoio |
| `fonte.tamanho.xs` | 0.75rem | Crédito, rodapé, obrigatoriedade |

**Entrelinha:**

| Token | Valor | Para |
|---|---|---|
| `colada` | **0.92** | **Display em caixa alta.** As linhas quase se tocam — é isso que forma o bloco sólido de texto |
| `apertada` | 1.1 | Título em caixa baixa |
| `media` | 1.35 | Corpo |
| `solta` | 1.6 | Texto longo |

A entrelinha colada é o detalhe que mais separa uma peça de igreja bem
tipografada de uma amadora. Linha solta em caixa alta gigante parece erro.

---

## Hierarquia — a regra de ouro

<!-- PREENCHER com as decisões da marca. A estrutura abaixo é o que costuma
     funcionar; confirme ou troque. -->

Numa peça, **um só elemento manda**. Se tudo está grande, nada está.

```
TÍTULO        display, 5xl/4xl, entrelinha apertada
  SUBTÍTULO   texto, xl, peso medio
    CORPO     texto, md, entrelinha media
      APOIO   texto, sm ou xs, cor texto.suave
```

---

## Versículo — o caso especial desta marca

A igreja publica Escritura com frequência, e é o texto que mais escorrega no
design. Decisões a tomar:

<!-- PREENCHER -->

| Questão | Decisão |
|---|---|
| Versículo usa display ou texto? | |
| Itálico? Aspas? | |
| Onde entra a referência (livro, capítulo, versículo)? | |
| Tamanho da referência em relação ao versículo | |
| Qual versão da Bíblia, e ela aparece na peça? | #CONFIRMAR — ver `AGENTS.md` §2.10 |

> [!CAUTION]
> Referência bíblica **sempre completa e conferida**. "Jeremias 29:11" sem
> conferir vira erro impresso que não se corrige. Ver `AGENTS.md` §2.10.

---

## Texto projetado no culto

O projetor é o pior meio técnico da igreja e o de maior audiência.

<!-- PREENCHER depois de testar no equipamento real, não na tela do computador. -->

| Questão | Decisão |
|---|---|
| Tamanho mínimo legível do fundo da igreja | |
| Quantas linhas por slide de letra | |
| Peso mínimo (fonte fina some no projetor) | |
| Alinhamento | |

---

## Onde ficam os arquivos

```
tipografia/
├── primaria/     família de display — .otf, .ttf, .woff2
├── secundaria/   família de texto
└── textos/       pesos e variantes soltas, se houver
```

Nomes minúsculos, sem acento: `nomedafonte-bold.woff2`.
Fontes ficam no **Git comum**, não no LFS — são pequenas e nunca mudam.
