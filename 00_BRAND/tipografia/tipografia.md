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
> **Status:** a definir.

---

## As famílias

<!-- PREENCHER. Duas famílias resolvem 95% dos casos: uma de display para
     título, uma de texto para o resto. Três já é uma a mais. -->

| Papel | Família | Token | Onde usar |
|---|---|---|---|
| **Display** | A definir | `fonte.familia.display` | Título, chamada, capa de carrossel |
| **Texto** | A definir | `fonte.familia.texto` | Corpo, legenda, interface, slide |

> [!IMPORTANT]
> **Licença.** Antes de adotar, verifique se a licença cobre uso da igreja —
> impresso, redes, site e projeção. Fonte do Google Fonts resolve isso de saída
> (SIL Open Font License) e ainda funciona em qualquer computador do time.
> Registre a licença aqui:
>
> | Família | Licença | Pode: impresso / web / projeção |
> |---|---|---|
> | | | |

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

**Entrelinha:** `apertada` (1.1) para título, `media` (1.35) para corpo,
`solta` (1.6) para texto longo.

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
