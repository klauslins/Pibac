---
tipo: documentacao
cliente: pibac
titulo: Guia Rápido
usar_quando: for a primeira vez neste projeto, ou precisar do resumo de como tudo funciona
status: ativo
atualizado: 2026-09-14
fonte: _AKZA/docs/GUIA-RAPIDO.md
---

# Guia Rápido — Comece por aqui

> Para quem acabou de entrar no projeto. Leitura de 5 minutos.
> Não precisa saber Git nem programar para usar este repositório.

---

## O que é isto?

Uma pasta organizada com **tudo** da comunicação da Primeira Igreja Batista em Águas Claras:
logo, documentos de estratégia, roteiros, artes, vídeos e peças prontas.

A organização segue um padrão da Akza que é **igual em todos os clientes**.
Aprendeu num, sabe usar em todos.

---

## A ideia em uma frase

> **Os números das pastas seguem a ordem em que o trabalho acontece.**

```
00_BRAND       →  a marca (vem antes de tudo, governa tudo)
01_STRATEGY    →  o que a marca defende
02_PLANNING    →  o que vamos fazer e quando
03_CONTENT     →  o texto (roteiro, legenda)
04_PRODUCTION  →  a arte sendo feita
05_EXPORTS     →  a peça pronta
06_MEDIA       →  fotos e vídeos brutos
07_IMPRESSOS   →  o que vai pra gráfica
08_MASTERS     →  arquivos gigantes
_META          →  manuais e automação
```

Se você está com um arquivo na mão e não sabe onde colocar, pergunte:
**"em que etapa do trabalho isso está?"** A resposta é a pasta.

---

## Preciso fazer X. Onde vou?

| Quero... | Vá para |
|---|---|
| Pegar o logo | `00_BRAND/logo/` |
| Pegar a fonte da marca | `00_BRAND/tipografia/` |
| Entender o cliente | `01_STRATEGY/briefing-cliente.md` |
| Ver o calendário de posts | `02_PLANNING/calendario/` |
| Escrever um roteiro | `03_CONTENT/roteiros/[ano-mês]/` |
| Escrever legenda de post | `03_CONTENT/copy/social/` |
| Trabalhar numa arte | `04_PRODUCTION/[campanha]/fontes/` |
| Salvar a arte finalizada | `05_EXPORTS/[campanha]/social/` |
| Pegar algo pronto pra postar | `05_EXPORTS/_PUBLISH-READY/` |
| Jogar as fotos da captação | `06_MEDIA/fotos/originais/` |
| Mandar algo pra gráfica | `07_IMPRESSOS/` |

---

## As 3 regras

### 1. Não mexa em `00_BRAND/`
É a identidade visual oficial. Se precisar alterar, fale com o responsável de branding.
Copie o arquivo para onde precisar — não mova nem edite o original.

### 2. Só se publica de `_PUBLISH-READY/`
Uma peça em `05_EXPORTS/campanha/social/` pode parecer pronta, mas ainda não foi
aprovada. **Só o que está em `05_EXPORTS/_PUBLISH-READY/` vai pro ar.**

### 3. Nome de arquivo: minúscula, sem acento, sem espaço

```
✅ post-tema-do-post-v1.png
❌ Post Antecipação de Riscos FINAL.png
```

**Por que isso importa:** os scripts que redimensionam as peças para cada rede
social leem os nomes dos arquivos. Um espaço ou acento faz o script parar.
Não é frescura — é o que permite automatizar.

E **nunca** use `final`. Sempre `v1`, `v2`, `v3`. Todo mundo já viu um
`logo_final_FINAL_v2_agora_vai.ai` — o padrão existe pra isso não acontecer.

---

## Como nomear (o padrão)

```
[tipo]-[assunto]-[variação]-v[número].[extensão]
```

**Exemplos reais deste projeto:**
```
post-tema-do-post-colorido-v2.png
reels-porta-voz-apresentacao-v1.mp4
logo-h-oficial-v1.svg          ← h = horizontal
logo-v-preto-v1.svg            ← v = vertical
outdoor-local-v3.pdf
```

**Errou o nome?** Não renomeie um por um:
```bash
python3 _META/automacao/rename-assets.py --dry-run 05_EXPORTS/minha-campanha/
```
Isso **mostra** o que ele faria, sem mexer em nada. Se estiver bom, rode de novo
sem o `--dry-run`.

---

## Fluxo de uma peça, do início ao fim

```
1. ROTEIRO      03_CONTENT/roteiros/2026-09/roteiro-tema-v1.docx
       ↓
2. ARTE         04_PRODUCTION/setembro-2026/fontes/post-tema-v1.ai
       ↓
3. EXPORT       05_EXPORTS/setembro-2026/social/instagram/post-tema-v1.png
       ↓
4. APROVAÇÃO    cliente revisa → aprovado
       ↓
5. PUBLICAÇÃO   05_EXPORTS/_PUBLISH-READY/post-tema-v1.png  → vai pro ar
```

O passo 4→5 é feito por comando, não arrastando arquivo:
```bash
bash _META/automacao/publish-pipeline.sh setembro-2026
```
Ele confere os nomes, valida e move. Se algo estiver fora do padrão, ele avisa
em vez de publicar errado.

---

## Sobre o Git (o mínimo que você precisa saber)

Este projeto é versionado — significa que **nada se perde**. Toda alteração fica
registrada e dá pra voltar atrás.

Se você não usa Git, **não tem problema**: trabalhe nos arquivos normalmente.
Alguém do time sincroniza. Só evite:
- Renomear pastas numeradas (`00_BRAND`, `04_PRODUCTION`...)
- Apagar arquivos "que parecem inúteis"
- Salvar arquivos de 2 GB dentro de `04_PRODUCTION/` (vão para `08_MASTERS/`)

Se você usa Git, leia [`VERSIONAMENTO.md`](VERSIONAMENTO.md).

---

## Onde pedir ajuda

| Dúvida | Documento |
|---|---|
| Como nomear um arquivo específico | [`NOMENCLATURA.md`](NOMENCLATURA.md) |
| Como funciona a automação | [`PIPELINE.md`](PIPELINE.md) |
| Como usar Git aqui | [`VERSIONAMENTO.md`](VERSIONAMENTO.md) |
| O que conferir antes de entregar | [`checklist-entrega.md`](checklist-entrega.md) |
| Quem é o cliente | [`../01_STRATEGY/briefing-cliente.md`](../01_STRATEGY/briefing-cliente.md) |
