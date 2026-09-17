---
tipo: guia-de-pasta
cliente: pibac
titulo: _META
usar_quando: precisar saber o que vai, e o que nao vai, em _META/
status: ativo
atualizado: 2026-09-10
---

# _META — Documentação e automação

> **O manual do projeto e os scripts que o mantêm em ordem.** O `_` no início
> sinaliza: isto não é etapa do fluxo de trabalho.

## Documentação

| Arquivo | Para quê |
|---|---|
| [`GUIA-RAPIDO.md`](GUIA-RAPIDO.md) | **Comece por aqui** se você é novo no time |
| [`NOMENCLATURA.md`](NOMENCLATURA.md) | Como nomear qualquer arquivo |
| [`PIPELINE.md`](PIPELINE.md) | Como a automação funciona |
| [`VERSIONAMENTO.md`](VERSIONAMENTO.md) | Como usar Git neste projeto |
| [`checklist-entrega.md`](checklist-entrega.md) | Conferir antes de entregar |
| [`CHANGELOG.md`](CHANGELOG.md) | Histórico do projeto |

## Automação

| Script | O que faz |
|---|---|
| `automacao/validar-projeto.py` | Confere o projeto inteiro contra o padrão |
| `automacao/rename-assets.py` | Renomeia em lote para a nomenclatura |
| `automacao/generate-manifest.py` | Regenera o índice de arquivos |
| `automacao/export-social.sh` | Gera variações de formato para redes |
| `automacao/publish-pipeline.sh` | Move aprovado para `_PUBLISH-READY/` |
| `automacao/pegar.py` | Resolve arquivos do ACERVO — os que não estão no Git |

```bash
# Sempre simule antes de aplicar
python3 _META/automacao/rename-assets.py --dry-run 05_EXPORTS/campanha/

# Confere o projeto inteiro
python3 _META/automacao/validar-projeto.py
```

> [!WARNING]
> **Não edite `automacao/manifest.json` à mão.** Ele é gerado por
> `generate-manifest.py`. Edição manual dessincroniza o índice do conteúdo real.

## Links

`links/` guarda referências para o que existe fora do Git — master em
`08_MASTERS/`, pasta no Drive, arquivo grande no SSD.

## Se você não usa terminal

Os scripts são para quem trabalha em linha de comando. Quem usa GitHub Desktop ou
o site não precisa rodá-los — mas precisa seguir a nomenclatura, porque a
validação roda automaticamente a cada push e acusa arquivo fora do padrão.

📖 [`NOMENCLATURA.md`](NOMENCLATURA.md) é a única leitura obrigatória para todo mundo.
