---
tipo: marca
cliente: pibac
titulo: Logo
usar_quando: for aplicar, redimensionar ou exportar a marca da igreja
status: rascunho
atualizado: 2026-09-17
---

# Logo — PIBAC

> **Status:** 🟢 **vetor oficial no repositório.**

## O que temos

`horizontal/ai/logo-h-oficial-v1.ai` — o arquivo original do Illustrator, com os
**dois modelos** na mesma prancheta.

| Modelo | Arquivo PNG | Quando usar |
|---|---|---|
| **Sigla** — símbolo + `PIBAC` | `logo-h-sigla-v1.png` · 5654×1622 | Espaço curto, uso interno, quando a igreja já é conhecida no contexto |
| **Nome completo** — símbolo + `PRIMEIRA IGREJA BATISTA DE ÁGUAS CLARAS` | `logo-h-completo-v1.png` · 5504×1622 | Institucional, impresso, primeira apresentação da igreja |

Os PNG foram **exportados do próprio vetor**, com transparência. O
`logo-h-branco-v1.png` ainda é o da web — trocar por export do Illustrator.

### Os SVG — os dois prontos

| Arquivo | Paths | Estado |
|---|---|---|
| `logo-h-sigla-v1.svg` | 47 | ✅ texto em contorno |
| `logo-h-completo-v1.svg` | 38 | ✅ texto em contorno |

Nenhum dos dois depende de fonte instalada: o texto virou vetor. Renderizam
igual em qualquer máquina, que é o que um logotipo em SVG precisa fazer.

> **O que estava errado antes:** o primeiro SVG saiu com o texto vivo, chamando
> `font-family: Nexa-Heavy`. Em máquina sem essa fonte, o nome da igreja
> aparecia em serifa — e nem a máquina da agência tem a Nexa Heavy. O conserto
> foi **Tipo → Criar contornos** (`⇧⌘O`) antes de exportar.
>
> Vale para qualquer SVG de marca daqui para a frente: **texto sempre em
> contorno.**

**A fonte do wordmark é Nexa Heavy** — geométrica, da Fontfabric. Fica
registrado porque é o que permite refazer a assinatura se um dia for preciso.

**O modelo de sigla ainda não tem SVG.**

> **Cor:** no arquivo o azul é **`CMYK 100/0/0/0`**, ciano de escala — e é assim
> que vai para a gráfica. Em tela o SVG carrega **`#009BDB`**, enquanto a cor
> principal do sistema é **`#007CC2`**. **Falta exportar do Illustrator uma
> versão do logotipo em `#007CC2` para uso em tela.**

## Ainda falta

- **Uma versão em `#007CC2`** para tela — é o que fecha a divergência de cor
- **`.svg` do modelo de sigla** e **`.eps`** para gráfica
- As versões **vertical** e **símbolo isolado**
- A versão **branca/monocromática** saída do vetor, não da web

## A regra que vem antes de todas

> [!CAUTION]
> **A marca não é redesenhada, nem redigitada, nem regerada — por ninguém, e
> muito menos por IA.** Vetorizar automaticamente um PNG, "melhorar" a curva de
> uma letra ou recriar o símbolo "igualzinho" produz um arquivo que **parece** a
> marca e não é. Se o original não existe, o caminho é procurá-lo, não refazê-lo.
>
> Onde procurar: quem fez a identidade, a gráfica que imprimiu o último material,
> a secretaria, o pastor, arquivos antigos de papel timbrado em `.pdf`
> (frequentemente têm o vetor embutido e recuperável).

---

## Versões

| Versão | Pasta | Quando usar |
|---|---|---|
| **Horizontal** | `horizontal/` | Padrão. Cabeçalho, rodapé, timbrado, banner largo |
| **Vertical** | `vertical/` | Espaço estreito e alto — story, totem, camiseta |
| **Símbolo** | `simbolo/` | Foto de perfil, favicon, selo, marca d'água |

Cada uma em quatro formatos:

```
horizontal/
├── ai/    editável original (Illustrator)   → Git LFS
├── eps/   para gráfica                      → Git LFS
├── svg/   para web — o que o site usa
└── png/   fundo transparente, para quem não abre vetor
```

**Nomes:** `logo-h-oficial-v1.svg`, `logo-v-branco-v1.png`, `simbolo-oficial-v1.svg`.
Minúsculas, sem acento, versão numerada. Nunca `final`.

---

## Variações de cor

<!-- PREENCHER quando a marca chegar. -->

| Variação | Arquivo | Usar sobre |
|---|---|---|
| Oficial (colorida) | | |
| Branca | | fundo escuro ou foto escura |
| Preta / monocromática | | impressão 1 cor, fax, carimbo |

---

## Respiro e tamanho mínimo

<!-- PREENCHER. Medir a partir do próprio logo, não chutar. -->

**Respiro (área de proteção):** a definir — a medida costuma ser derivada de um
elemento do próprio logo (a altura da inicial, a largura do símbolo). Nada entra
nessa área: nem texto, nem foto, nem borda.

**Tamanho mínimo:**

| Meio | Mínimo |
|---|---|
| Digital | a definir (px de largura) |
| Impresso | a definir (mm de largura) |

Abaixo do mínimo, use o **símbolo** no lugar da assinatura completa.

---

## Proibições

<!-- PREENCHER com o que já viu acontecer com esta marca. A lista abaixo é a
     base universal; acrescente os erros específicos. -->

- Distorcer — esticar ou achatar. Redimensionar **sempre** proporcional
- Trocar a cor da marca por uma fora da paleta
- Aplicar sobre foto de fundo agitado sem tarja ou sem a versão branca
- Adicionar sombra, contorno, brilho ou gradiente
- Rotacionar
- Redigitar o nome da igreja numa fonte parecida e chamar de logo
- Usar um PNG de baixa resolução esticado — se só existe PNG pequeno, procure o vetor

---

## Assinatura com as convenções

A igreja integra a **Convenção Batista Brasileira (CBB)** e a **Convenção
Batista do Planalto Central (CBPC)**, e o site as exibe.

<!-- PREENCHER: em que peças os selos aparecem, em que tamanho, em que posição,
     e se há arte oficial fornecida por elas. -->

| Questão | Decisão |
|---|---|
| Em quais peças os selos entram | |
| Posição e tamanho | |
| Temos a arte oficial das convenções | #CONFIRMAR |
