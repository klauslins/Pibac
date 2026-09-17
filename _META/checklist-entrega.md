---
tipo: checklist
cliente: pibac
titulo: Checklist de Entrega
usar_quando: conferir uma peca antes de entregar
status: ativo
atualizado: 2026-09-14
fonte: _AKZA/docs/checklist-entrega.md
---

# Checklist de Entrega

> Percorra antes de mandar qualquer peça para aprovação do cliente ou para publicação.
> Padrão Akza v1.0.

---

## 1. Antes de mandar para aprovação do cliente

### Marca
- [ ] Logo na versão correta para o fundo (claro/escuro) — ver `00_BRAND/logo/`
- [ ] Área de respiro do logo respeitada
- [ ] Cores dentro da paleta oficial
- [ ] Tipografia da marca (as fontes definidas em `00_BRAND/tipografia/`) — sem fonte de sistema
- [ ] Logo não foi distorcido, recolorido ou recriado

### Conteúdo
- [ ] Texto revisado — ortografia e gramática
- [ ] Números, datas e valores conferidos
- [ ] Nome e cargo das pessoas corretos
- [ ] Telefone, site e @ conferidos
- [ ] Tom de voz alinhado ao posicionamento da marca (ver [`AGENTS.md`](../AGENTS.md) §8)
- [ ] Sem promessa que gere risco regulatório ou de compliance no segmento

### Técnico
- [ ] Nome do arquivo segue o padrão (`validar-projeto.py` passa)
- [ ] Dimensão correta para o canal (ver `automacao/pipeline-config.json`)
- [ ] RGB para digital · CMYK para impressão
- [ ] Sem elemento cortado na área de segurança
- [ ] Texto legível no menor tamanho de exibição

---

## 2. Específico por canal

<details>
<summary><b>Instagram / Feed</b></summary>

- [ ] 1080×1080 (1:1) ou 1080×1350 (4:5)
- [ ] RGB, 72 dpi, JPG ou PNG
- [ ] Abaixo de 8 MB
- [ ] Legenda escrita e salva em `03_CONTENT/copy/social/`
- [ ] Elementos importantes fora dos 10% das bordas
</details>

<details>
<summary><b>Instagram / Stories e Reels</b></summary>

- [ ] 1080×1920 (9:16)
- [ ] Zona segura: 250 px do topo e 320 px da base livres de texto
- [ ] Reels: MP4, H.264, até 90s
- [ ] Áudio conferido — sem clipping, sem ruído
- [ ] Legendas queimadas (a maioria assiste sem som)
</details>

<details>
<summary><b>LinkedIn</b></summary>

- [ ] 1200×628 (post) ou 1080×1080
- [ ] Registro mais sóbrio que o Instagram
- [ ] Sem excesso de emoji
</details>

<details>
<summary><b>YouTube</b></summary>

- [ ] Vídeo 1920×1080 · Thumbnail 1280×720
- [ ] Thumbnail abaixo de 2 MB
- [ ] Título, descrição e tags escritos
- [ ] Thumbnail legível em miniatura (teste a 20% do tamanho)
</details>

<details>
<summary><b>Impressão</b></summary>

- [ ] CMYK, mínimo 300 dpi (150 dpi para outdoor)
- [ ] Sangria de 3 mm
- [ ] Marcas de corte
- [ ] Fontes convertidas em curvas
- [ ] Imagens vinculadas embutidas
- [ ] PDF/X-1a ou PDF/X-4
- [ ] Preto de texto: 100% K puro, não composto
- [ ] Prova impressa conferida antes da tiragem
</details>

---

## 3. Antes de publicar

- [ ] Cliente aprovou **por escrito** (e-mail ou mensagem registrada)
- [ ] Versão final está em `05_EXPORTS/[campanha]/`
- [ ] `manifest.json` atualizado (`python3 _META/automacao/generate-manifest.py`)
- [ ] Status no manifest = `approved`
- [ ] Rodou `bash _META/automacao/publish-pipeline.sh [campanha]` sem erro
- [ ] Arquivo está em `05_EXPORTS/_PUBLISH-READY/`
- [ ] Data e horário de publicação confirmados com o calendário
- [ ] Legenda e hashtags prontas
- [ ] Fonte editável arquivada em `04_PRODUCTION/[campanha]/fontes/`

---

## 4. Depois de publicar

- [ ] Peça publicada conferida no ar (formato não foi cortado?)
- [ ] Link ou permalink registrado
- [ ] Status no manifest atualizado para `published`
- [ ] `git add . && git commit && git push`
- [ ] `_META/CHANGELOG.md` atualizado se foi entrega relevante

---

## 5. Sinais de que algo está errado

Pare e revise se:

- 🚩 O nome do arquivo tem `final`, espaço ou acento
- 🚩 A peça está em `_PUBLISH-READY/` sem aprovação registrada
- 🚩 O editável não existe — só o PNG exportado
- 🚩 A fonte usada não está em `00_BRAND/tipografia/`
- 🚩 A cor foi escolhida "no olho" em vez da paleta
- 🚩 O arquivo tem mais de 100 MB e não está em `08_MASTERS/`
- 🚩 Alguém editou algo dentro de `00_BRAND/`
