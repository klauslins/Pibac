---
tipo: marca
cliente: pibac
titulo: Grafismos e anatomia da peca
usar_quando: for montar a arte de um post, story ou slide e precisar da anatomia da peca
status: ativo
atualizado: 2026-10-16
---

# Grafismos e anatomia da peça — PIBAC

> Grafismo é o que faz uma peça ser reconhecida como da igreja **antes** de
> alguém ler o nome dela.

---

## A anatomia que funciona

Estas regras saíram da análise de onze peças de referência escolhidas pela
igreja. O que chama atenção não é a fonte que elas usam — é o que **todas**
fazem igual.

### 1. O texto é o protagonista, não a legenda da foto

Nas peças de anúncio, o texto ocupa **entre metade e dois terços da altura do
quadro**. Ele começa colado no topo e desce por cima da imagem.

Isso é o oposto do reflexo natural, que é escolher a foto bonita e espremer o
texto num canto. Aqui a foto é **fundo**; a frase é a peça.

### 2. Entrelinha colada

Use o token `fonte.entrelinha.colada` (**0.92**). As linhas quase se tocam, e é
isso que forma um bloco sólido de texto em vez de linhas soltas.

É o detalhe que mais separa uma peça bem tipografada de uma amadora. Caixa alta
gigante com entrelinha larga parece erro.

### 3. A foto é dessaturada

Preto e branco, ou com a cor puxada bem para baixo. Nenhuma das referências usa
foto com cor saturada sob o texto — e o motivo é prático: **foto viva disputa
com a tipografia e as duas perdem.**

### 4. O texto é branco ou creme. Nunca cor de marca

Sobre foto, o texto é `cor.texto.invertido` (areia) ou branco puro. A cor da
marca **não vira texto em cima de foto** — ela não tem contraste para isso
(`#007CC2` dá 4,50:1 no melhor caso, e sobre foto é pior ainda).

Cor de marca aparece em bloco chapado, não em letra sobre imagem.

### 5. Alinhado à esquerda, sangrando até a margem

Texto centralizado enfraquece o bloco. Alinhe à esquerda e deixe a última linha
correr até perto da borda.

---

## Onde vai cada informação

```
┌─────────────────────────────────────┐
│ ENDEREÇO · HORÁRIO        ← topo, pequeno, caixa alta, Montserrat Light
│                                     │
│  CHAMADA                            │
│  EM CAIXA                 ← Archivo Expanded Black, entrelinha 0.92
│  ALTA GIGANTE                       │
│                                     │
│  subtítulo                ← Montserrat, bem menor, opcional
│                                     │
│         [ foto dessaturada ]        │
│                                     │
│ logo                   arraste →    │ ← rodapé: marca pequena, nunca competindo
└─────────────────────────────────────┘
```

**A informação que nunca pode faltar numa peça de convite:** o que é, que dia,
que horas, onde. Nas referências ela vive no **topo**, pequena e discreta — não
no meio, não disputando com a chamada.

---

## O logotipo na peça

Pequeno, num canto, **nunca competindo com o texto**. Ele assina, não anuncia.

Arquivos em [`../logo/`](../logo/). Sobre foto escura, use a versão branca.

---

## Os dois registros

Decididos em [`../tipografia/tipografia.md`](../tipografia/tipografia.md), e
valem aqui tanto quanto lá:

> **Caixa alta convida. Caixa baixa acolhe.**

Peça que chama para vir → Archivo, caixa alta, texto gigante.
Peça que consola ou ensina → Montserrat, caixa baixa, mais respiro, menos peso.

**Nunca os dois no mesmo quadro.**

---

## Elementos gráficos próprios

| Elemento | Arquivo | De onde vem |
|---|---|---|
| **Onda** | *a extrair* | As três ondas do símbolo do logotipo, isoladas |
| **Bloco com cruz** | *a extrair* | O quadrado vazado do símbolo |

> [!NOTE]
> **A matéria-prima já existe e ninguém precisa inventar nada.** O símbolo da
> PIBAC tem dois elementos que funcionam sozinhos: as **ondas** (água, batismo,
> e o nome do bairro) e o **bloco com a cruz vazada**. Extrair os dois do vetor
> dá à igreja um repertório gráfico que é dela, sem desenhar nada novo.
>
> Depende do mesmo passo que o resto: exportar do Illustrator.

---

## Formatos e zonas de segurança

| Peça | Dimensão | Zona segura |
|---|---|---|
| Post feed (quadrado) | 1080 × 1080 | 60 px de margem |
| Post feed (retrato) | 1080 × 1350 | centro 1080 × 1080 sobrevive ao corte |
| Story / Reels | 1080 × 1920 | 250 px no topo e 300 px embaixo ficam cobertos pela interface |
| Slide de culto | 1920 × 1080 | 80 px de margem — projetor corta borda |
| Capa de vídeo | 1280 × 720 | |

As specs por canal ficam em
[`../../_META/automacao/pipeline-config.json`](../../_META/automacao/pipeline-config.json).

---

## Foto

| Questão | Decisão |
|---|---|
| Tratamento | Dessaturada ou preto e branco quando houver texto por cima |
| O que mostra | Gente da igreja, momento real, sem pose |
| O que **não** mostra | Criança sem autorização — ver abaixo |

> [!CAUTION]
> **Criança em foto só com autorização de imagem assinada** — `AGENTS.md` §2.8.
> Vale para EBD Infantil, Coral Infantil, EMR e Juventude Farol. As autorizações
> ficam em [`../../01_STRATEGY/_fontes/autorizacoes-de-imagem/`](../../01_STRATEGY/_fontes/autorizacoes-de-imagem/).
> Sem autorização registrada, a foto não sai de `06_MEDIA/`.
>
> E lembre: **o repositório é público.** Foto commitada aqui é foto publicada.
