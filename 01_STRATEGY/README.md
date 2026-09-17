---
tipo: guia-de-pasta
cliente: pibac
titulo: 01_STRATEGY
usar_quando: precisar saber o que vai, e o que nao vai, em 01_STRATEGY/
status: ativo
atualizado: 2026-09-10
---

# 01_STRATEGY — Estratégia e posicionamento

> **O porquê antes do quê.** Aqui mora a inteligência do projeto: quem é o
> cliente, com quem ele fala, o que ele defende e em que tom.

Esta é a pasta que mais alimenta contexto — tanto para quem entra no time quanto
para agentes de IA. Documento bem escrito aqui economiza retrabalho em todas as
outras pastas.

## O que vai aqui

| Subpasta | O que guarda |
|---|---|
| `diagnostico/` | Análise inicial: onde a marca está, o que não funciona |
| `manifesto/` | O que a marca defende, em texto próprio para citar |
| `personas/` | Para quem falamos — dor, linguagem, canal |
| `linhas-editoriais/` | Os pilares de conteúdo e o peso de cada um |
| `guia-de-conteudo/` | Tom de voz, o que dizer, o que nunca dizer |
| `biografias/` | Bio do porta-voz por canal, com contagem de caractere |
| `_fontes/` | Material bruto que embasou o resto: pesquisa, dado, print |

Na raiz: [`briefing-cliente.md`](briefing-cliente.md) — o documento de entrada do
projeto. Se ele está incompleto, todo o resto está apoiado em suposição.

## O que NÃO vai aqui

| Isso | Vai em |
|---|---|
| Briefing de uma campanha específica | `02_PLANNING/briefings/` |
| Legenda, roteiro, copy | `03_CONTENT/` |
| Calendário editorial | `02_PLANNING/calendario/` |

A diferença: **01 é o que vale o ano inteiro. 02 é o que vale este mês.**

## Formato

Markdown (`.md`) sempre que possível — versiona bem, dá para ver o que mudou
entre versões e a IA consegue ler. PDF do cliente entra em `_fontes/` como
recebido, e o que importa dele é transcrito para markdown.

```
diagnostico-inicial-v1.md
persona-servidor-publico-v1.md
guia-de-conteudo-v2.md
```

> [!IMPORTANT]
> **Dado sem fonte não entra.** Número, percentual, lei ou citação vai com a
> origem em `_fontes/`. Se não deu para confirmar, marque `#CONFIRMAR` — é melhor
> um vazio sinalizado do que um dado errado que vira outdoor.

📖 [`_META/NOMENCLATURA.md`](../_META/NOMENCLATURA.md)
