---
tipo: documentacao
cliente: pibac
titulo: Versionamento
usar_quando: usar git, LFS ou branch neste projeto
status: ativo
atualizado: 2026-09-14
fonte: _AKZA/docs/VERSIONAMENTO.md
---

# Versionamento — Como usar Git neste projeto

> Padrão Akza v1.0. Vale para todos os repositórios de cliente.

---

## Por que versionar arquivos de design?

Porque a alternativa é o caos que todo mundo conhece:

```
outdoor_final.ai
outdoor_final_v2.ai
outdoor_final_APROVADO.ai
outdoor_final_APROVADO_correcao_cliente.ai
outdoor_final_AGORA_VAI.ai
```

Com Git, existe **um** `outdoor-local-v1.ai` e um histórico que diz quem
mudou o quê, quando e por quê — com possibilidade de voltar a qualquer ponto.

---

## Setup inicial (uma vez por computador)

```bash
# Git LFS é obrigatório — sem ele você baixa ponteiros, não arquivos
brew install git-lfs
git lfs install

# Identifique-se
git config --global user.name "Seu Nome"
git config --global user.email "voce@exemplo.com"
```

### Clonando um projeto

```bash
git clone https://github.com/klauslins/Pibac.git
cd Pibac
git lfs pull        # baixa os arquivos de design de verdade
```

> [!WARNING]
> Abriu um `.ai` e o Illustrator reclamou de arquivo corrompido?
> É um ponteiro LFS. Rode `git lfs pull`.

---

## O que entra e o que não entra no Git

| Entra ✅ | Não entra ❌ |
|---|---|
| Documentos (`.md`, `.docx`, `.json`) | `08_MASTERS/` — arquivos >100 MB |
| Logos e fontes (`00_BRAND/`) | `06_MEDIA/videos/brutos/` |
| Roteiros e copies (`03_CONTENT/`) | `06_MEDIA/fotos/originais/` |
| Fontes de design via LFS (`.ai`, `.psd`) | Arquivos `._*` do macOS |
| Exports finais (`05_EXPORTS/`) | Temporários do Adobe (`.idlk`, `.aidb`) |

**Por que excluir mídia bruta?** Uma captação gera dezenas de GB de vídeo que
nunca são editados diretamente. O que importa versionar é o resultado.
O bruto fica no SSD e no backup em nuvem.

> [!IMPORTANT]
> **GitHub bloqueia arquivos acima de 100 MB — hard limit.**
> Neste projeto, `08_MASTERS/outdoor/outdoor-exemplo-v1.tif` tem **mais de 1 GB**.
> Ele existe no SSD, está indexado no `manifest.json` com checksum, mas **nunca**
> vai para o GitHub. Isso é intencional, não é um esquecimento.

---

## Git LFS — o que é e por que importa

Arquivos de design são **binários**. O Git guarda cada versão inteira de um
binário — não consegue guardar "só a diferença" como faz com texto.

Sem LFS, 10 versões de um `.ai` de 5 MB = **50 MB no histórico, para sempre**,
baixados por todo mundo que clonar, mesmo anos depois.

Com LFS, o Git guarda um ponteiro de ~130 bytes e o arquivo real vai para um
armazenamento separado, baixado só quando necessário.

**Tipos em LFS neste projeto** (definidos em `.gitattributes`):
`.ai` `.eps` `.psd` `.psb` `.indd` `.fig` `.tif` `.pdf` `.mp4` `.mov` `.wav` `.zip`

**Tipos em Git comum** (pequenos ou imutáveis):
`.png` `.jpg` `.svg` `.ttf` `.otf` `.docx` `.md` `.json`

> [!NOTE]
> O LFS aqui é o do próprio GitHub: **1 GB de armazenamento e 1 GB de tráfego por
> mês** na cota gratuita. É pouco — só binário que realmente muda vai para o LFS.
> Fontes (`.ttf`) ficam no Git comum, não mudam nunca. Vídeo bruto e master de
> impressão não entram no Git de jeito nenhum.

---

## O dia a dia

```bash
# 1. Antes de começar, puxe as novidades
git pull

# 2. Trabalhe normalmente (Illustrator, Word, o que for)

# 3. Veja o que mudou
git status

# 4. Adicione e descreva
git add 04_PRODUCTION/setembro-2026/
git commit -m "adiciona artes do carrossel de setembro"

# 5. Envie
git push
```

### Mensagens de commit

Em português, no imperativo, dizendo **o que mudou**:

```
✅ adiciona roteiros de setembro
✅ corrige cor do logo no outdoor
✅ atualiza calendário para Q4
✅ remove versão antiga do timbrado

❌ update
❌ mudanças
❌ asdasd
❌ commit final
```

**Por quê:** daqui a seis meses alguém vai procurar quando o outdoor mudou de cor.
`update` não ajuda ninguém.

---

## Versão de arquivo (`v1`, `v2`) vs versão de Git

São coisas diferentes e complementares:

| | Versão no nome (`v2`) | Histórico do Git |
|---|---|---|
| **Para quê** | Variações que **coexistem** e podem ser comparadas lado a lado | Rastrear **toda** alteração automaticamente |
| **Quem vê** | Cliente, designer, gráfica | Quem usa Git |
| **Exemplo** | `post-tema-v1.png` e `post-tema-v2.png` — duas propostas | "quem alterou o `-v2` na terça?" |

**Regra prática:** suba o `vN` quando a mudança é **conceitual** — outra proposta,
outra direção de arte, uma revisão que o cliente pediu e quer comparar.
Ajuste pequeno (mudou um kerning, corrigiu um typo)? Mantenha o `vN` e deixe o
Git registrar.

---

## Branches

Para a maior parte do trabalho de comunicação, **trabalhe direto na `main`**.
O fluxo de produção é sequencial, e branch atrapalha mais do que ajuda quando
duas pessoas não editam o mesmo `.ai`.

Use branch quando:
- Testar uma direção de arte que talvez seja descartada
  → `git checkout -b proposta/rebranding-outdoor`
- Fazer uma mudança estrutural grande no repositório
  → `git checkout -b estrutura/novo-fluxo-exports`

```bash
git checkout -b proposta/nome-da-ideia
# ... trabalha, commita ...
git push -u origin proposta/nome-da-ideia
# aprovado? faz merge. descartado? deleta a branch. nada se perde.
```

---

## Problemas comuns

<details>
<summary><b>"Todos os arquivos aparecem como modificados e eu não toquei em nada"</b></summary>

Disco exFAT não guarda permissões Unix. O Git interpreta isso como mudança.
Já está resolvido neste repo, mas se voltar:
```bash
git config core.filemode false
```
</details>

<details>
<summary><b>"Aparecem centenas de arquivos <code>._alguma-coisa</code>"</b></summary>

São sidecars que o macOS cria em disco exFAT. Já estão no `.gitignore`.
Para limpar: `find . -name '._*' -delete`
</details>

<details>
<summary><b>"O push falhou: file exceeds GitHub's file size limit"</b></summary>

Um arquivo >100 MB entrou no commit. Mova para `08_MASTERS/`:
```bash
git rm --cached caminho/do/arquivo-gigante.tif
mv caminho/do/arquivo-gigante.tif 08_MASTERS/
git commit -m "move master pesado para fora do Git"
```
</details>

<details>
<summary><b>"Meu <code>.ai</code> abriu como arquivo de texto"</b></summary>

É um ponteiro LFS não resolvido:
```bash
git lfs install && git lfs pull
```
</details>

<details>
<summary><b>"Preciso voltar um arquivo para como estava ontem"</b></summary>

```bash
git log --oneline -- caminho/do/arquivo.ai   # acha o commit
git checkout <hash> -- caminho/do/arquivo.ai # restaura aquela versão
```
</details>

---

## Este repositório

```
github.com/klauslins/Pibac     (público)
```

Um repositório só, com toda a comunicação da igreja. A estrutura de pastas segue
o padrão organizacional Akza v1.5 — é o mesmo esqueleto usado em projetos de
comunicação profissionais, o que significa que quem já trabalhou nele sabe
navegar aqui sem treinamento.

> [!CAUTION]
> **O repositório é público.** Antes de commitar qualquer coisa, pergunte: *isso
> pode ser lido por qualquer pessoa, para sempre?*
>
> Nunca entram: foto de criança sem autorização assinada, telefone ou endereço de
> membro, pedido de oração nominal, situação de saúde ou financeira de alguém,
> ata de assembleia, lista de membros, relatório financeiro.
>
> O histórico do Git não esquece: se algo assim for commitado, **apagar num
> commit seguinte não resolve** — é preciso reescrever o histórico ou tornar o
> repositório privado.
