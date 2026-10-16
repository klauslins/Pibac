---
tipo: design-system
cliente: pibac
titulo: Design System
usar_quando: for desenhar qualquer peca da igreja — comece por aqui
status: rascunho
atualizado: 2026-09-17
---

# Design System — PIBAC

> **Versão** 1.0 · **Criado em** 17/09/2026 · **Paleta fechada em** 16/10/2026
> **Status:** cor e tipografia decididas e geradas. Falta o vetor do logotipo.

Este é o sistema que faz post, story, informativo, slide de culto, banner e
impresso parecerem a mesma igreja. Ele não é o gosto de quem desenhou a peça da
semana: é a decisão registrada, que sobrevive à troca de quem desenha.

> [!IMPORTANT]
> **A regra que sustenta tudo:** a fonte da verdade é
> [`tokens/tokens.json`](tokens/tokens.json). Nunca escreva um hex à mão em CSS,
> em slide ou em arquivo de arte. Decidiu uma cor? Ela entra no `tokens.json` e o
> script regenera CSS, SCSS e Tailwind de uma vez:
>
> ```bash
> python3 _META/automacao/gerar-tokens.py
> ```
>
> Enquanto houver `null` no `tokens.json`, o script **recusa gerar** e lista o
> que falta. É de propósito: melhor não ter arquivo do que ter arquivo com valor
> chutado.

---

## Por onde começar

| Você quer… | Leia |
|---|---|
| Saber qual cor usar | [`cores/paleta.md`](cores/paleta.md) |
| Escrever um título | [`tipografia/tipografia.md`](tipografia/tipografia.md) |
| Aplicar o logo | [`logo/logo.md`](logo/logo.md) |
| Montar a arte de um post | [`grafismos/grafismos.md`](grafismos/grafismos.md) |
| Codar site, landing ou e-mail | [`tokens/`](tokens/) |
| Ver tudo aplicado | [`preview.html`](preview.html) — abra no navegador |

---

## A marca em uma frase

<!-- PREENCHER: uma frase que diga o que o sistema visual precisa comunicar.
     Não o que a igreja é — o que o DESIGN tem que fazer sentir.
     Ex. de estrutura: "[qualidade central] — [três palavras concretas].
     O sistema carrega isso: [decisão de cor], [decisão de tipo], [decisão de foto]." -->

**O azul da igreja, em registro calmo.** O logotipo não mudou — mudou o que está
em volta dele. O sistema abre o mesmo azul em cinco tons de baixa saturação,
sobre fundo de areia quente, com terra como detalhe. A marca aparece porque é a
coisa mais saturada da página, não porque grita.

> [!NOTE]
> A visão da igreja — *"ser uma igreja de verdadeiros discípulos discipuladores"* —
> e a tensão de marca descrita em [`../AGENTS.md`](../AGENTS.md) §1 valem para o
> design tanto quanto para o texto. Os três desvios lá listados (virar mural de
> avisos, importar o tom do marketing, transcrever o púlpito) têm equivalente
> visual: **card de evento genérico**, **estética de anúncio** e **slide de
> sermão publicado como post**.

---

## Fundamentos

### Logo
**A definir.** Qual assinatura é a principal, em que versão, com que respiro
mínimo. Detalhes e proibições em [`logo/logo.md`](logo/logo.md).

Enquanto o vetor original não estiver em `logo/`, **nenhuma peça nova é
produzida** e a marca não é redesenhada nem regerada — nem por IA, nem por
vetorização automática de um PNG.

### Cor
Sete cores, derivadas do matiz 202° do próprio logotipo. `#007CC2` é a marca e
só ela é saturada; `#242D33` carrega todo o texto; `#A68A69` é detalhe e **nunca**
texto pequeno. Tabela de contraste medida em [`cores/paleta.md`](cores/paleta.md).

**Preto e dourado não fazem parte do sistema** — são o tema de 19 anos de 2026,
e vivem em [`../02_PLANNING/briefings/19-anos-2026.md`](../02_PLANNING/briefings/19-anos-2026.md).

### Tipografia
Duas famílias, uma regra: **caixa alta convida, caixa baixa acolhe.**
**Archivo Expanded** Black para anúncio em caixa alta; **Montserrat** para
afirmação em caixa baixa e todo o apoio. As duas do Google Fonts, licença livre.
Detalhes em [`tipografia/tipografia.md`](tipografia/tipografia.md) e a anatomia
da peça em [`grafismos/grafismos.md`](grafismos/grafismos.md).

### Escalas
Já vêm decididas nos tokens, porque são encanamento e não identidade:
espaçamento, raio de canto, tamanhos de fonte e entrelinha seguem uma escala
modular padrão. **Pode mudar** — se mudar, mude no `tokens.json`.

---

## Acessibilidade — o que não é questão de gosto

Contraste não é preferência estética, é o que decide se a pessoa **consegue ler**.
No culto, o projetor lava a cor; no celular, a pessoa lê no sol. A régua é a
WCAG 2.1:

| Onde | Contraste mínimo |
|---|---|
| Texto corrido | **4.5:1** |
| Texto grande (≥ 24px, ou ≥ 19px em negrito) | **3:1** |
| Ícone e borda que carregam informação | **3:1** |
| Slide projetado no culto | mire em **7:1** — projetor perde contraste |

Confira cada par de cores em [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/)
e **registre o resultado** em [`cores/paleta.md`](cores/paleta.md). Uma combinação
que reprova não vira "usa com cuidado": vira proibida, escrita como proibida.

E nunca use **só cor** para diferenciar informação — quem não distingue as duas
cores perde o dado. Some ícone, texto ou posição.

---

## Estado do sistema

| Peça | Status |
|---|---|
| Paleta | ✅ 16/10/2026 — 7 cores, contraste medido |
| Tipografia | ✅ Montserrat |
| Tokens gerados | ✅ 50 tokens em `tokens.css`, `.scss` e Tailwind |
| `preview.html` | ✅ abra no navegador |
| Logo em PNG alta resolução | 🟡 provisório, extraído do site |
| **Logo em vetor** | ⏳ **o que ainda falta** — sem ele não há impresso grande |
| Anatomia da peça | ✅ 16/10/2026 — os dois registros e a estrutura do quadro |
| Grafismos em arquivo | ⏳ extrair a onda e o bloco do vetor, no Illustrator |
