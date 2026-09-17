---
tipo: design-system
cliente: pibac
titulo: Design System
usar_quando: for desenhar qualquer peca da igreja — comece por aqui
status: rascunho
atualizado: 2026-09-17
---

# Design System — PIBAC

> **Versão** 0.1 (esqueleto) · **Criado em** 17/09/2026
> **Status:** as pastas e os arquivos existem, as **decisões de design não**.
> Nada aqui foi inventado — o que falta está em branco, não preenchido por suposição.

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

**A definir.** Escreva isto **depois** de decidir cor e tipografia, não antes:
a frase é o resumo das decisões, não o briefing delas.

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
**A definir.** Quantas cores, qual a primária, qual o papel de cada uma.
Registre em [`cores/paleta.md`](cores/paleta.md) e nos tokens.

### Tipografia
**A definir.** Uma família para título, uma para texto — e a licença de cada uma.
Registre em [`tipografia/tipografia.md`](tipografia/tipografia.md).

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
| Logo em vetor | ⏳ falta o arquivo original |
| Paleta | ⏳ |
| Tipografia | ⏳ |
| Grafismos | ⏳ |
| Tokens gerados (`tokens.css`, `.scss`, Tailwind) | 🔒 bloqueado até a paleta e a tipografia existirem |
| `preview.html` | ⏳ mostra o sistema assim que os tokens forem gerados |
