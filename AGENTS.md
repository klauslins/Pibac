---
tipo: hub
cliente: pibac
titulo: AGENTS.md
usar_quando: sempre, antes de qualquer tarefa neste projeto
status: ativo
atualizado: 2026-09-17
---

# AGENTS.md — Instruções para Agentes de IA

> Fonte primária de instruções para qualquer LLM, agente ou automação que
> opere neste repositório. Padrão organizacional **Akza v1.5**.

---

## 1. Contexto do projeto

| Campo | Valor |
|---|---|
| **Igreja** | Primeira Igreja Batista em Águas Claras (PIBAC) |
| **Comunicação** | Akza |
| **Segmento** | Igreja evangélica batista — Convenção Batista Brasileira (CBB), Águas Claras/DF |
| **Denominação** | Batista. Integra a CBB e a Convenção Batista do Planalto Central (CBPC) |
| **Pastor presidente** | Pr. Moisés Gonçalves — eleito em 19/07/2020, empossado em 31/10/2020 |
| **Aprovação de conteúdo** | #CONFIRMAR — quem assina o "pode publicar" (pastor? secretaria? líder de comunicação?) |
| **Site** | pibaguasclaras.org.br |
| **Instagram** | [@pib.aguasclaras](https://www.instagram.com/pib.aguasclaras) |
| **Endereço** | Rua Jerivá, nº 5, Águas Claras/DF — CEP 71928-360 |
| **Contato** | WhatsApp (61) 99118-4691 · contato@pibaguasclaras.org.br · seg–sex, 8h–17h |

### Visão e missão (texto oficial — não parafraseie)

> **Visão:** "Ser uma igreja de verdadeiros discípulos discipuladores"
> **Missão:** "Fazer o maior número de discípulos, de todas as nações, até a volta
> do Senhor Jesus."

**Tema do ano:** #CONFIRMAR

### Agenda fixa — a espinha dorsal do calendário de conteúdo

| Dia | Atividade | Horário |
|---|---|---|
| Quarta | Manhã de Oração | 8h–10h |
| Quarta | Culto de Oração | 19h30 |
| Sábado | Embaixadores e Mensageiras do Rei | 9h–11h |
| Domingo | Escola Bíblica Dominical (EBD) | 9h–11h30 |
| Domingo | Culto de Celebração | 18h–20h |

### Frentes e ministérios documentados no site

EBD e EBD para Crianças · Juventude Farol · Jovens e Adolas · Embaixadores e
Mensageiras do Rei · Ministério de Mulheres · Universidade da Família (UDF) ·
PGMs (pequenos grupos) · Mãos Amigas · CRER (Centro de Reabilitação Emocional) ·
Carona Solidária · Coral Infantil · TADEL (Treinamento Avançado de Líderes) ·
Maratona Bíblica · PIBAC TV · Quarta de Guerra (oração e jejum) · Missões ·
Informativo Mensal · Escala de Serviço

**Diferencial a comunicar:** #CONFIRMAR — *proposta da Akza, a validar com a
liderança:* uma igreja de bairro que nasceu de porta em porta no Residencial
Araucárias, em 2002, e que organiza a vida inteira em torno de **discipulado**,
não de evento. O que ela oferece a quem chega não é uma programação, é um lugar
onde alguém caminha com você — PGM, EBD, UDF, TADEL são degraus da mesma escada.

**Tom de voz:** #CONFIRMAR — *proposta da Akza, a validar com a liderança:*
acolhedor, claro e próximo. Fala com o vizinho de Águas Claras, não com o
"público-alvo". Frases curtas, segunda pessoa, sem jargão de seminário e sem
jargão de marketing. Convida sempre com o essencial na mão: **o que é, que dia,
que horas, onde**.

> [!IMPORTANT]
> **Tensão de marca.** Comunicação de igreja escorrega por três lados, e aqui
> os três estão à mão:
>
> 1. **Virar mural de avisos.** O acervo mais fácil de produzir é o card de
>    evento. Se o feed vira só data e horário, a igreja comunica agenda e não
>    comunica fé. Todo mês precisa de conteúdo que sirva a quem **não** vai ao
>    culto naquela semana.
> 2. **Importar o tom do marketing.** Gatilho de escassez, promessa de resultado
>    e linguagem de conversão não cabem aqui. **Proibido:** "últimas vagas" para
>    culto, "garanta sua bênção", promessa de cura, prosperidade ou milagre como
>    retorno de oferta. A PIBAC é batista, da CBB — teologia de prosperidade não
>    é o registro dela.
> 3. **Transcrever o púlpito.** Linguagem de sermão não vira legenda. Cite a
>    passagem, dê a referência (livro, capítulo e versículo) e traduza para a
>    vida de quem lê no ônibus.
>
> **Também proibido:** anunciar preletor, data, horário ou local que não estejam
> confirmados pela secretaria; usar a nomenclatura de um ministério que mudou de
> nome; e publicar valor de campanha financeira sem texto aprovado pela diretoria.

---

## 2. Regras absolutas — NUNCA violar

1. **NÃO** delete, mova ou renomeie nada em `00_BRAND/` sem aprovação humana explícita.
2. **NÃO** trate nada como publicável fora de `05_EXPORTS/_PUBLISH-READY/`.
3. **NÃO** crie nomes com acento, espaço, maiúscula ou caractere especial.
4. **NÃO** edite `_META/automacao/manifest.json` à mão — use `generate-manifest.py`.
5. **NÃO** commite arquivos acima de 100 MB. Vão para `08_MASTERS/` (ignorado pelo Git).
6. **NÃO** use `final`, `final2`, `FINAL_REAL`. Só versão numerada: `v1`, `v2`, `v3`.
7. **NÃO** invente dado da igreja (horário, nome de ministério, referência bíblica,
   nome de liderança, valor de campanha). Se não estiver documentado aqui ou no
   site, **pergunte** ou marque como `#CONFIRMAR`.
8. **NÃO** use imagem de criança ou adolescente sem autorização de imagem
   assinada pelos responsáveis. Vale para EBD Infantil, Coral Infantil,
   Embaixadores e Mensageiras do Rei e Juventude Farol. As autorizações ficam em
   `01_STRATEGY/_fontes/autorizacoes-de-imagem/` — sem autorização registrada,
   a foto não sai de `06_MEDIA/`.
9. **NÃO** exponha dado pessoal de membro (telefone, endereço, pedido de oração,
   situação de saúde ou financeira) em peça pública. Pedido de oração e
   testemunho só vão ao ar com consentimento explícito e registrado.
10. **NÃO** cite versículo sem conferir o texto e a referência na versão adotada
    pela igreja (#CONFIRMAR qual — ARA, NVI, ACF…). Versículo errado em peça
    impressa é erro que não se corrige depois.
11. **NÃO** escreva um hex, um tamanho ou um espaçamento à mão em código ou em
    peça. A fonte é `00_BRAND/tokens/tokens.json`; o CSS, o SCSS e o preset do
    Tailwind saem dele por `gerar-tokens.py`. Valor colado na mão é o valor que
    não se atualiza quando a marca muda.
12. **NÃO** redesenhe, redigite, vetorize automaticamente nem gere a marca por
    IA. Se o vetor original não existe, ele é procurado — não refeito. Ver
    `00_BRAND/logo/logo.md`.

---

## 3. Onde colocar cada arquivo

| O que você tem | Onde vai |
|---|---|
| Editável de design (`.ai`, `.psd`, `.fig`) | `04_PRODUCTION/[campanha]/fontes/` |
| Export para redes sociais | `05_EXPORTS/[campanha]/social/[plataforma]/` |
| Export para impressão | `05_EXPORTS/[campanha]/print/` |
| Export para web | `05_EXPORTS/[campanha]/web/` |
| Peça aprovada, pronta para publicar | `05_EXPORTS/_PUBLISH-READY/` |
| Foto bruta de culto ou evento | `06_MEDIA/fotos/originais/` *(fora do Git)* |
| Foto tratada | `06_MEDIA/fotos/tratadas/` |
| Vídeo bruto | `06_MEDIA/videos/brutos/` *(fora do Git)* |
| Vídeo editado (PIBAC TV, cortes de mensagem) | `06_MEDIA/videos/editados/` |
| Roteiro de vídeo | `03_CONTENT/roteiros/[YYYY-MM]/` |
| Copy para social | `03_CONTENT/copy/social/` |
| Texto do informativo mensal | `03_CONTENT/copy/email/` |
| Documento de visão, missão ou identidade | `01_STRATEGY/[categoria]/` |
| Autorização de uso de imagem | `01_STRATEGY/_fontes/autorizacoes-de-imagem/` |
| Calendário de conteúdo | `02_PLANNING/calendario/[YYYY-QN]/` |
| Master de impressão >100 MB | `08_MASTERS/[tipo]/` *(fora do Git)* |

> [!NOTE]
> A igreja já tem 19 GB de material bruto em `Pibac/` na raiz do SSD (missões,
> cultos de domingo, PSDs de modelo). Esse acervo **não entra no Git**: o que for
> aproveitado é tratado e copiado para `06_MEDIA/` ou `08_MASTERS/`, com o nome
> normalizado. O resto fica onde está.

---

## 4. Convenção de nomenclatura

**Padrão:** `[tipo]-[assunto]-[variacao]-v[N].[ext]`

- **tipos gerais:** `post`, `story`, `reels`, `carrossel`, `banner`, `thumbnail`,
  `logo`, `simbolo`, `roteiro`, `copy`, `outdoor`, `card`, `timbrado`
- **assuntos recorrentes da PIBAC:** `culto-celebracao`, `culto-oracao`,
  `manha-oracao`, `ebd`, `ebd-infantil`, `pgm`, `udf`, `tadel`, `juventude-farol`,
  `min-mulheres`, `emr` *(Embaixadores e Mensageiras do Rei)*, `maos-amigas`,
  `crer`, `missoes`, `maratona-biblica`, `pibac-tv`, `informativo`, `escala`
- **extensão:** sempre minúscula

```
post-culto-celebracao-convite-v1.png
story-ebd-classe-nova-v2.jpg
reels-pastor-reflexao-marcos4-v1.mp4
card-agenda-semanal-outubro-v1.png
```

```bash
python3 _META/automacao/rename-assets.py --dry-run <pasta>   # simula
python3 _META/automacao/rename-assets.py <pasta>             # aplica
```

---

## 5. Fluxo esperado

```
03_CONTENT (texto) → 04_PRODUCTION (arte) → 05_EXPORTS (canal) → _PUBLISH-READY (aprovado)
```

Antes de considerar uma peça pronta:
1. O nome segue a convenção? (`validar-projeto.py` verifica)
2. Está no `manifest.json` com `status: approved`?
3. Passou pelo [`_META/checklist-entrega.md`](_META/checklist-entrega.md)?
4. Data, horário e local conferem com a agenda confirmada pela secretaria?
5. Tem criança na imagem? A autorização está registrada?

---

## 6. Comandos da automação

```bash
python3 _META/automacao/gerar-tokens.py         # cor e tipo -> CSS, SCSS, Tailwind
python3 _META/automacao/generate-manifest.py    # indexa assets
python3 _META/automacao/validar-projeto.py      # valida o padrão
python3 _META/automacao/rename-assets.py --dry-run <pasta>
bash _META/automacao/export-social.sh [campanha]
bash _META/automacao/publish-pipeline.sh [campanha]
```

---

## 7. Git neste repositório

- **Repositório público** em [github.com/klauslins/Pibac](https://github.com/klauslins/Pibac).
  Tudo que for commitado fica visível para qualquer pessoa, **e o histórico do Git
  guarda para sempre**: apagar o arquivo num commit seguinte não remove o conteúdo.
  Antes de commitar, aplique as regras §2.8 (imagem de menores) e §2.9 (dado
  pessoal de membro) — aqui elas não são cuidado interno, são exposição pública.
- **Git LFS** para `.ai`, `.eps`, `.psd`, `.pdf`, `.tif`, `.mp4`, `.mov`.
- **Disco exFAT:** `core.filemode=false` já configurado. Não altere.
- **Nunca** commite `08_MASTERS/`, `06_MEDIA/videos/brutos/` ou `06_MEDIA/fotos/originais/`.
- Commits em português, no imperativo: `adiciona roteiros de outubro`.

📖 [`_META/VERSIONAMENTO.md`](_META/VERSIONAMENTO.md)

---

## 8. Ao gerar conteúdo — checagem antes de publicar

- [ ] Serve a quem **não** está na igreja nesta semana, ou é só aviso de agenda?
- [ ] O tom é de convite, não de venda? (sem escassez, sem promessa de resultado)
- [ ] A referência bíblica está completa e conferida na versão adotada?
- [ ] Data, horário, local e nome do ministério batem com a agenda confirmada?
- [ ] Nenhuma criança ou adolescente sem autorização de imagem registrada?
- [ ] Nenhum dado pessoal de membro exposto?
- [ ] Fala de Águas Claras — lugar, gente e rotina de quem mora aqui?
- [ ] Está coerente com a visão de "discípulos discipuladores"?

---

## 9. Fontes de verdade — consulte antes de assumir

| Pergunta | Onde está a resposta |
|---|---|
| Quem é a igreja, qual o contexto? | `01_STRATEGY/briefing-cliente.md` |
| Qual a visão, a missão e os pilares? | §1 deste arquivo · `01_STRATEGY/manifesto/` |
| Que cor, fonte ou logo usar numa peça? | `00_BRAND/design-system.md` |
| O valor exato de uma cor ou medida | `00_BRAND/tokens/tokens.json` — **a única fonte** |
| Como escrever para esta igreja? | `01_STRATEGY/guia-de-conteudo/` |
| Quais assets existem e qual o status? | `_META/automacao/manifest.json` |
| Quais formatos e specs por canal? | `_META/automacao/pipeline-config.json` |
| Quem autorizou uso de imagem? | `01_STRATEGY/_fontes/autorizacoes-de-imagem/` |
| O que já foi feito? | `_META/CHANGELOG.md` |
| Agenda e programação do mês | Secretaria da igreja · pibaguasclaras.org.br/agenda-semanal |

> [!NOTE]
> Documentos `.docx` — para ler o conteúdo:
> `python3 -c "import docx; print('\n'.join(p.text for p in docx.Document('arquivo.docx').paragraphs))"`
