#!/usr/bin/env python3
"""
validar-projeto.py
Akza — Padrão Organizacional de Projetos de Comunicação v1.0

Verifica se o projeto está dentro do padrão: nomenclatura, estrutura de
pastas, limites de tamanho e coerência do manifest.

Uso:
    python3 _META/automacao/validar-projeto.py
    python3 _META/automacao/validar-projeto.py --strict   # avisos viram erros
    python3 _META/automacao/validar-projeto.py --quiet    # só o resumo

Código de saída: 0 se tudo certo, 1 se houver erro.
Serve para hook de pre-commit ou CI.

Dependências: nenhuma (stdlib Python 3.8+)
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST = PROJECT_ROOT / "_META" / "automacao" / "manifest.json"

# ─── Regras ──────────────────────────────────────────────────────────────────

LIMITE_GITHUB_MB = 100


def fora_do_git(caminhos):
    """Quais destes caminhos o .gitignore ja exclui.

    O limite de 100 MB e uma regra do GitHub: so faz sentido para arquivo que
    vai ser versionado. Perguntar ao proprio git evita manter aqui uma lista
    paralela ao .gitignore, que divergiria na primeira alteracao.
    """
    import subprocess
    if not caminhos:
        return set()
    try:
        p = subprocess.run(
            ["git", "-C", str(PROJECT_ROOT), "check-ignore", "--stdin"],
            input="\n".join(caminhos), capture_output=True, text=True, timeout=60)
    except Exception:
        return set()          # sem git: mantem o comportamento antigo
    return {l.strip() for l in p.stdout.splitlines() if l.strip()}
PASTA_MASTERS = "08_MASTERS"

PASTAS_OBRIGATORIAS = [
    "00_BRAND", "01_STRATEGY", "02_PLANNING", "03_CONTENT",
    "04_PRODUCTION", "05_EXPORTS", "05_EXPORTS/_PUBLISH-READY",
    "06_MEDIA", "07_IMPRESSOS", "_META", "_META/automacao",
]

ARQUIVOS_OBRIGATORIOS = [
    "README.md", "AGENTS.md", ".gitignore", ".gitattributes",
    "_META/CHANGELOG.md", "_META/GUIA-RAPIDO.md", "_META/NOMENCLATURA.md",
    "_META/PIPELINE.md", "_META/VERSIONAMENTO.md", "_META/checklist-entrega.md",
    "_META/automacao/manifest.json", "_META/automacao/pipeline-config.json",
]

# Nomes proibidos que sinalizam falta de versionamento
PALAVRAS_PROIBIDAS = re.compile(
    r"(?:^|[-_])(final|final\d+|finalizado|aprovado|ok|novo|atual|"
    r"definitivo|ultimo|agora-?vai|copia|copy\d+|sem-?titulo|untitled)"
    r"(?:$|[-_.])",
    re.IGNORECASE,
)

# Extensões que devem seguir a convenção de nomenclatura
EXT_NORMATIVAS = {
    ".ai", ".psd", ".psb", ".indd", ".fig", ".eps",
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".tif", ".tiff",
    ".mp4", ".mov", ".webm", ".pdf", ".docx",
}

# Caminhos onde a convenção não se aplica (material de terceiros, sistema)
ISENTOS = [
    "00_BRAND/tipografia/",   # fontes de terceiros: nome técnico tem significado
    "_META/",
    ".git/",
    ".claude/",               # skills: o Claude Code define os nomes
    ".github/",               # workflows e templates seguem a convenção do GitHub
    # Captação bruta. O nome vem da câmera (AKZ09228.jpg) e é ele que preserva a
    # sequência do que foi fotografado. A convenção de nomenclatura existe para
    # o que vai ao ar — arquivo bruto não é entregável, e renomear em massa aqui
    # destruiria a única ordem confiável do acervo.
    "06_MEDIA/fotos/originais/",
    "06_MEDIA/videos/brutos/",
]

# Artefatos gerados por ferramenta. O nome é definido pela ferramenta e está
# referenciado dentro dos próprios arquivos — renomear quebra a edição.
SUFIXOS_FERRAMENTA = (".dc.html",)
NOMES_FERRAMENTA = {"canvas.json"}

IGNORAR_SEMPRE = {".gitkeep", ".DS_Store", ".gitignore", ".gitattributes"}

# Arquivos que a convenção da indústria exige em MAIÚSCULA — a regra de
# minúsculas não se aplica a eles.
NOMES_CANONICOS = {
    "README.md", "AGENTS.md", "CHANGELOG.md", "CONTRIBUTING.md",
    "LICENSE", "LICENSE.md", "CLAUDE.md", "NOMENCLATURA.md",
    "PIPELINE.md", "VERSIONAMENTO.md", "GUIA-RAPIDO.md", "MEMORY.md",
    # O Claude Code so reconhece uma skill se o arquivo se chamar SKILL.md.
    "SKILL.md", "INDICE.md",
}


# ─── Coleta ──────────────────────────────────────────────────────────────────

class Relatorio:
    def __init__(self):
        self.erros = []
        self.avisos = []

    def erro(self, categoria, caminho, detalhe):
        self.erros.append((categoria, caminho, detalhe))

    def aviso(self, categoria, caminho, detalhe):
        self.avisos.append((categoria, caminho, detalhe))


def isento(rel: str) -> bool:
    nome = rel.rsplit("/", 1)[-1]
    if nome in NOMES_FERRAMENTA or rel.endswith(SUFIXOS_FERRAMENTA):
        return True
    return any(rel.startswith(p) for p in ISENTOS)


def tem_acento(texto: str) -> bool:
    return any(unicodedata.combining(c) for c in unicodedata.normalize("NFKD", texto))


def validar_nome(nome: str) -> list:
    """Retorna a lista de problemas do nome de arquivo."""
    problemas = []
    stem = nome.rsplit(".", 1)[0] if "." in nome else nome
    ext = nome[len(stem):]

    if tem_acento(nome):
        problemas.append("contém acento")
    if " " in nome:
        problemas.append("contém espaço")
    if stem != stem.lower():
        problemas.append("contém maiúscula")
    if ext != ext.lower():
        problemas.append("extensão em maiúscula")
    if re.search(r"[^a-zA-Z0-9\-._]", nome):
        achados = sorted(set(re.findall(r"[^a-zA-Z0-9\-._]", nome)))
        problemas.append(f"caractere inválido: {' '.join(repr(c) for c in achados)}")
    if PALAVRAS_PROIBIDAS.search(stem):
        problemas.append("usa 'final/aprovado/novo' — use versão numerada (v1, v2)")
    if "--" in nome:
        problemas.append("hífen duplo")

    return problemas


def validar(strict: bool) -> Relatorio:
    r = Relatorio()

    # 1. Estrutura de pastas
    for pasta in PASTAS_OBRIGATORIAS:
        if not (PROJECT_ROOT / pasta).is_dir():
            r.erro("estrutura", pasta, "pasta obrigatória do padrão ausente")

    # 2. Arquivos de documentação
    for arq in ARQUIVOS_OBRIGATORIOS:
        if not (PROJECT_ROOT / arq).is_file():
            r.erro("documentacao", arq, "arquivo obrigatório ausente")

    # 3. Varredura de arquivos
    sem_versao = []
    arquivos = [f for f in PROJECT_ROOT.rglob("*") if f.is_file()]
    IGNORADOS = fora_do_git([str(f.relative_to(PROJECT_ROOT)) for f in arquivos])

    for f in arquivos:
        rel = str(f.relative_to(PROJECT_ROOT))

        if rel.startswith(".git/"):
            continue

        # Lixo do macOS
        if f.name.startswith("._"):
            r.aviso("lixo-macos", rel, "sidecar do macOS — rode: find . -name '._*' -delete")
            continue
        if f.name in IGNORAR_SEMPRE or f.name in NOMES_CANONICOS:
            continue

        # Tamanho
        mb = f.stat().st_size / 1_048_576
        if mb > LIMITE_GITHUB_MB and not rel.startswith(PASTA_MASTERS) and rel not in IGNORADOS:
            r.erro("tamanho", rel,
                   f"{mb:.0f} MB — acima do limite de {LIMITE_GITHUB_MB} MB do GitHub. "
                   f"Mova para {PASTA_MASTERS}/")

        if isento(rel):
            continue

        # Nomenclatura
        problemas = validar_nome(f.name)
        if problemas:
            r.erro("nomenclatura", rel, "; ".join(problemas))

        # Versão no nome
        if f.suffix.lower() in EXT_NORMATIVAS and not re.search(r"-v\d+", f.stem):
            sem_versao.append(rel)

    for rel in sem_versao:
        r.aviso("versao", rel, "sem sufixo de versão (-v1, -v2...)")

    # 4. Coerência do manifest
    if MANIFEST.is_file():
        try:
            dados = json.loads(MANIFEST.read_text())
        except json.JSONDecodeError as e:
            r.erro("manifest", "_META/automacao/manifest.json", f"JSON inválido: {e}")
            dados = None

        if dados:
            indexados = {a.get("file") for a in dados.get("assets", [])}
            status = {a.get("file"): a.get("status") for a in dados.get("assets", [])}

            pr = PROJECT_ROOT / "05_EXPORTS" / "_PUBLISH-READY"
            if pr.is_dir():
                for f in pr.rglob("*"):
                    if not f.is_file() or f.name in IGNORAR_SEMPRE or f.name.startswith("._"):
                        continue
                    rel = str(f.relative_to(PROJECT_ROOT))
                    if rel not in indexados:
                        r.erro("publicacao", rel,
                               "está em _PUBLISH-READY/ mas não consta no manifest")
                    elif status.get(rel) not in ("approved", "published"):
                        r.erro("publicacao", rel,
                               f"está em _PUBLISH-READY/ com status '{status.get(rel)}' "
                               f"— só 'approved' ou 'published' podem estar aqui")

            # Placeholders não preenchidos
            for chave, valor in dados.get("brand", {}).items():
                if isinstance(valor, str) and "CONFIRMAR" in valor:
                    r.aviso("manifest", f"brand.{chave}", "valor ainda não confirmado")

    if strict:
        r.erros.extend(r.avisos)
        r.avisos = []

    return r


# ─── Saída ───────────────────────────────────────────────────────────────────

def imprimir(r: Relatorio, quiet: bool):
    def bloco(itens, titulo, icone):
        if not itens:
            return
        print(f"\n{icone} {titulo} ({len(itens)})")
        por_cat = {}
        for cat, caminho, det in itens:
            por_cat.setdefault(cat, []).append((caminho, det))
        for cat in sorted(por_cat):
            print(f"\n  [{cat}]")
            for caminho, det in sorted(por_cat[cat])[:15]:
                print(f"    {caminho}")
                print(f"      → {det}")
            if len(por_cat[cat]) > 15:
                print(f"    ... e mais {len(por_cat[cat]) - 15}")

    print(f"\n🔍 Validando: {PROJECT_ROOT.name}")

    if not quiet:
        bloco(r.erros, "ERROS", "❌")
        bloco(r.avisos, "AVISOS", "⚠️ ")

    print("\n" + "─" * 60)
    if not r.erros and not r.avisos:
        print("✅ Projeto 100% dentro do padrão Akza.")
    elif not r.erros:
        print(f"✅ Nenhum erro. {len(r.avisos)} aviso(s) — não bloqueiam.")
    else:
        print(f"❌ {len(r.erros)} erro(s) e {len(r.avisos)} aviso(s).")
        print("   Consulte _META/NOMENCLATURA.md para as regras.")
    print("─" * 60 + "\n")


def main():
    ap = argparse.ArgumentParser(description="Valida o projeto contra o padrão Akza")
    ap.add_argument("--strict", action="store_true", help="trata avisos como erros")
    ap.add_argument("--quiet", action="store_true", help="mostra apenas o resumo")
    args = ap.parse_args()

    r = validar(args.strict)
    imprimir(r, args.quiet)
    sys.exit(1 if r.erros else 0)


if __name__ == "__main__":
    main()
