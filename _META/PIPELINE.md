---
tipo: documentacao
cliente: pibac
titulo: Pipeline de Publicação
usar_quando: rodar a automacao ou entender como uma peca vira entregavel
status: ativo
atualizado: 2026-09-14
fonte: _AKZA/docs/PIPELINE.md
---

# Pipeline de Publicação

> Como uma peça sai do Illustrator e chega no ar, com validação automática
> em cada passo. Padrão Akza v1.0.

---

## Visão geral

```
   03_CONTENT          04_PRODUCTION         05_EXPORTS          _PUBLISH-READY
   ──────────          ─────────────         ──────────          ──────────────
    roteiro      →      arte (.ai)      →     export por     →      aprovado
     copy               fontes/               canal                  no ar
                                                  │                    ▲
                                                  │                    │
                                          export-social.sh     publish-pipeline.sh
                                          (redimensiona)       (valida e move)
                                                  │                    │
                                                  └────────┬───────────┘
                                                           ▼
                                                    manifest.json
                                                 (índice + status)
```

O `manifest.json` é o **estado do projeto**: que peças existem, em que status,
para qual canal, com que checksum. Os scripts leem e escrevem nele.

---

## Os cinco comandos

| Comando | O que faz | Quando rodar |
|---|---|---|
| `generate-manifest.py` | Varre as pastas e indexa todo asset no `manifest.json` | Depois de adicionar ou mover arquivos |
| `validar-projeto.py` | Checa nomes, pastas e tamanhos contra o padrão | Antes de commitar |
| `rename-assets.py` | Normaliza nomes em lote | Ao receber arquivos de fora |
| `export-social.sh` | Redimensiona para cada rede social | Depois de exportar a arte-mãe |
| `publish-pipeline.sh` | Valida e move o aprovado para `_PUBLISH-READY/` | Após aprovação do cliente |

---

## Passo a passo de uma campanha

### 1. Criar a campanha

```bash
mkdir -p 04_PRODUCTION/campanha-mes-ano/{fontes,referencias,revisoes}
```

Escreva o briefing local em `04_PRODUCTION/campanha-mes-ano/_briefing.md` —
o que é, para quem, qual pilar de conteúdo, quais peças.

### 2. Produzir

Editáveis em `fontes/`, seguindo a nomenclatura:
```
04_PRODUCTION/campanha-mes-ano/fontes/post-tema-do-post-v1.ai
```

### 3. Exportar a arte-mãe

Exporte na maior resolução para:
```
05_EXPORTS/campanha-mes-ano/web/post-tema-do-post-v1.png
```

### 4. Gerar as versões por canal

```bash
bash _META/automacao/export-social.sh campanha-mes-ano
```

O script gera, a partir de cada imagem-mãe:

| Canal | Formato | Dimensão |
|---|---|---|
| Instagram | feed 1:1 | 1080×1080 |
| Instagram | story 9:16 | 1080×1920 |
| LinkedIn | post | 1200×628 |
| YouTube | thumbnail | 1280×720 |

Resultado em `05_EXPORTS/campanha-mes-ano/social/[plataforma]/`.

> [!NOTE]
> **Requer ImageMagick:** `brew install imagemagick`
> Sem ele o script para com aviso, sem alterar nada.

### 5. Indexar

```bash
python3 _META/automacao/generate-manifest.py
```

Cada asset entra no `manifest.json` com caminho, tamanho, checksum e `status: draft`.

### 6. Aprovar

O fluxo de aprovação tem quatro etapas (definidas em `pipeline-config.json`):

| Etapa | De → Para | Responsável |
|---|---|---|
| 1. Criação | `draft` → `review` | Designer Akza |
| 2. Revisão interna | `review` → `approved` | Diretor Akza |
| 3. Aprovação do cliente | `approved` | Contato de aprovação do cliente |
| 4. Publicação | `approved` → `published` | Gestor de tráfego |

Percorra o [`checklist-entrega.md`](checklist-entrega.md) antes de marcar como aprovado.

### 7. Publicar

```bash
bash _META/automacao/publish-pipeline.sh campanha-mes-ano
```

O script **valida antes de mover**:
- Nome dentro da convenção
- Sem acento, espaço ou maiúscula
- Asset registrado no manifest
- Status = `approved`

Passou em tudo → copia para `05_EXPORTS/_PUBLISH-READY/`.
Falhou → lista o que está errado e **não move nada**.

> [!IMPORTANT]
> `_PUBLISH-READY/` é o **único** diretório que uma automação de publicação
> (agendador, CI, integração com Meta/Notion/Drive) deve ler. Tudo fora dele
> é trabalho em andamento, mesmo que pareça pronto.

---

## O `manifest.json`

Índice de tudo. Estrutura:

```jsonc
{
  "project":   { /* nome, site, segmento, posicionamento */ },
  "brand":     { /* cores, fontes, caminhos dos logos */ },
  "platforms": { /* handles e formatos por rede */ },
  "campaigns": [ /* campanhas ativas */ ],
  "assets": [
    {
      "file": "05_EXPORTS/campanha-mes-ano/social/instagram/post-tema-v1.png",
      "type": "post",
      "campaign": "campanha-mes-ano",
      "platform": "instagram",
      "format": "feed-1x1",
      "status": "approved",
      "size_bytes": 842103,
      "hash_md5": "a2ae411adb...",
      "in_git": true,
      "updated_at": "2026-08-31"
    }
  ]
}
```

**Por que existe:** permite responder por comando perguntas como "quais peças
estão aguardando aprovação?" ou "esta arte já foi publicada?" — sem abrir pasta
por pasta. É também o que um agente de IA lê para entender o estado do projeto.

> [!WARNING]
> **Não edite o `manifest.json` à mão.** Rode `generate-manifest.py`.
> Ele preserva os metadados que você já preencheu (status, campanha, plataforma)
> e só atualiza o que é derivado do disco (caminho, tamanho, checksum).

Status possíveis: `draft` · `review` · `approved` · `published` · `archived`

---

## Validação

```bash
python3 _META/automacao/validar-projeto.py
```

Verifica:
- Nomes fora da convenção (acento, espaço, maiúscula, `final`)
- Arquivos acima de 100 MB fora de `08_MASTERS/`
- Pastas obrigatórias do padrão ausentes
- Arquivos `._*` do macOS esquecidos
- Assets em `_PUBLISH-READY/` sem status `approved`

Saída: lista do que corrigir. Código de saída ≠ 0 se houver erro — dá para
plugar num hook de pre-commit.

---

## Arquivos pesados

O GitHub bloqueia arquivos acima de **100 MB** — limite rígido, não contornável
nem com Git LFS na cota gratuita.

Por isso existe `08_MASTERS/`: masters de impressão, TIFFs de outdoor e vídeos
finalizados em alta ficam ali. A pasta está no `.gitignore`, mas os arquivos
**são indexados no `manifest.json`** com caminho, tamanho e checksum — e marcados
com `"in_git": false`.

Para listar o que existe fora do Git neste projeto:

```bash
python3 -c "
import json
a = json.load(open('_META/automacao/manifest.json'))['assets']
for x in a:
    if not x.get('in_git'):
        print(f\"{x['size_bytes']/1048576:8.0f} MB  {x['file']}\")
"
```

O backup desses arquivos é responsabilidade do backup em nuvem do disco, não do Git.

---

## Próximas automações (ainda não implementadas)

- [ ] Publicação direta na API do Meta a partir de `_PUBLISH-READY/`
- [ ] Sincronização de `05_EXPORTS/` com Google Drive do cliente
- [ ] Espelhamento do calendário editorial no Notion
- [ ] Hook de pre-commit rodando `validar-projeto.py`
- [ ] Geração de contact sheet (visualização em grade) de cada campanha
