---
tipo: marca
cliente: pibac
titulo: Grafismos
usar_quando: for montar a arte de um post, story ou slide e precisar da anatomia da peca
status: rascunho
atualizado: 2026-09-17
---

# Grafismos e anatomia da peça — PIBAC

> **Status:** a definir.
> Grafismo é o que faz uma peça ser reconhecida como da igreja **antes** de
> alguém ler o nome dela. É a diferença entre "um card de evento" e "um card da
> PIBAC".

---

## Os elementos

<!-- PREENCHER quando existirem. Cada grafismo entra nesta pasta como .svg,
     nome minúsculo e versionado: grafismo-nome-v1.svg -->

| Elemento | Arquivo | O que é | Onde usar |
|---|---|---|---|
| | | | |

---

## Anatomia do post

<!-- PREENCHER: onde cada coisa fica no quadrado. Sem isso, cada peça inventa
     um layout e o feed nunca parece de uma igreja só. -->

```
┌─────────────────────────────┐
│  logo                       │  ← posição, tamanho, versão
│                             │
│  TÍTULO                     │  ← display, qual tamanho
│  subtítulo                  │
│                             │
│  [ elemento gráfico ]       │
│                             │
│  data · hora · local        │  ← a informação que NUNCA pode faltar
└─────────────────────────────┘
```

> [!IMPORTANT]
> **A regra que vale para toda peça de igreja:** se a peça convida para alguma
> coisa, ela precisa de **o que é, que dia, que horas e onde** — legível sem dar
> zoom. Card lindo sem endereço é card que não cumpriu a função.

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

<!-- PREENCHER: que tipo de foto representa esta igreja. -->

| Questão | Decisão |
|---|---|
| Tratamento (cor, contraste, filtro) | |
| O que a foto mostra | |
| O que a foto **não** mostra | |

> [!CAUTION]
> **Criança em foto só com autorização de imagem assinada** — `AGENTS.md` §2.8.
> Vale para EBD Infantil, Coral Infantil, EMR e Juventude Farol. As autorizações
> ficam em [`../../01_STRATEGY/_fontes/autorizacoes-de-imagem/`](../../01_STRATEGY/_fontes/autorizacoes-de-imagem/).
> Sem autorização registrada, a foto não sai de `06_MEDIA/`.
>
> E lembre: **o repositório é público.** Foto commitada aqui é foto publicada.
