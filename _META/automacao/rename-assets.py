#!/usr/bin/env python3
"""
rename-assets.py
Akza — Pipeline de Comunicação v1.0

Renomeia arquivos em lote seguindo a convenção:
  [type]-[slug]-[variant]-v[N].[ext]

Remove acentos, espaços e caracteres especiais automaticamente.

Uso:
    # Ver o que seria renomeado (sem alterar nada):
    python3 _META/automacao/rename-assets.py --dry-run 06_MEDIA/fotos/originais/

    # Renomear de fato:
    python3 _META/automacao/rename-assets.py 04_PRODUCTION/lancamento-conteudo-ago-2026/fontes/

    # Renomear recursivamente:
    python3 _META/automacao/rename-assets.py --recursive 05_EXPORTS/

Dependências: nenhuma (apenas stdlib Python 3.8+)
"""

import os
import sys
import re
import argparse
import unicodedata
from pathlib import Path

# ─── Configuração ────────────────────────────────────────────────────────────

KNOWN_EXTENSIONS = {
    ".ai", ".psd", ".indd", ".fig",
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg",
    ".mp4", ".mov", ".webm",
    ".pdf", ".tif", ".tiff", ".eps",
    ".docx", ".doc", ".md",
    ".ttf", ".otf", ".woff", ".woff2",
}

IGNORE_PATTERNS = ["._*", ".DS_Store", "*.tmp", "README.md", "AGENTS.md"]


# ─── Helpers ──────────────────────────────────────────────────────────────────

def remove_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def slugify(text: str) -> str:
    """Converte qualquer string em slug válido para nome de arquivo.

    Todo caractere que não seja letra ou número vira hífen — inclusive
    parênteses, colchetes e vírgulas.

    Trocar por hífen em vez de apagar é o que evita colar palavras:
        "-HORIZONTAL (BRANCO)"  →  "horizontal-branco"   ✅
                                →  "horizontalbranco"    ❌ (bug antigo)
    """
    text = remove_accents(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def needs_rename(name: str) -> bool:
    """Retorna True se o nome do arquivo precisa ser normalizado."""
    return name != slugify(name.rsplit(".", 1)[0]) + ("." + name.rsplit(".", 1)[1] if "." in name else "")


def should_ignore(filename: str) -> bool:
    import fnmatch
    for pattern in IGNORE_PATTERNS:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def safe_rename(src: Path, dst: Path, dry_run: bool) -> bool:
    """Renomeia com segurança, evitando colisões."""
    if dst.exists() and dst != src:
        stem = dst.stem
        ext = dst.suffix
        counter = 1
        while dst.exists():
            dst = dst.parent / f"{stem}-{counter}{ext}"
            counter += 1

    if dry_run:
        print(f"  [DRY-RUN] {src.name!r}\n           → {dst.name!r}")
        return True

    try:
        src.rename(dst)
        print(f"  ✅ {src.name!r} → {dst.name!r}")
        return True
    except Exception as e:
        print(f"  ❌ Erro ao renomear {src.name!r}: {e}", file=sys.stderr)
        return False


# ─── Main ─────────────────────────────────────────────────────────────────────

def process_directory(directory: Path, recursive: bool, dry_run: bool) -> tuple:
    renamed = 0
    skipped = 0
    errors = 0

    pattern = "**/*" if recursive else "*"
    files = [f for f in directory.glob(pattern) if f.is_file()]

    for filepath in sorted(files):
        if should_ignore(filepath.name):
            continue
        if filepath.suffix.lower() not in KNOWN_EXTENSIONS:
            continue

        stem = filepath.stem
        ext = filepath.suffix.lower()
        new_stem = slugify(stem)
        new_name = f"{new_stem}{ext}"

        if new_name == filepath.name:
            skipped += 1
            continue

        new_path = filepath.parent / new_name
        ok = safe_rename(filepath, new_path, dry_run)
        if ok:
            renamed += 1
        else:
            errors += 1

    return renamed, skipped, errors


def main():
    parser = argparse.ArgumentParser(
        description="Renomeia arquivos para o padrão de nomenclatura Akza"
    )
    parser.add_argument("directory", help="Diretório a processar")
    parser.add_argument("--dry-run", action="store_true",
                        help="Mostra o que seria renomeado sem fazer alterações")
    parser.add_argument("--recursive", action="store_true",
                        help="Processa subdiretórios recursivamente")
    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.exists():
        print(f"❌ Diretório não encontrado: {directory}", file=sys.stderr)
        sys.exit(1)

    mode = "DRY RUN" if args.dry_run else "RENOMEANDO"
    print(f"\n🔄 {mode} — {directory}")
    print(f"   Recursivo: {'sim' if args.recursive else 'não'}\n")

    renamed, skipped, errors = process_directory(directory, args.recursive, args.dry_run)

    print(f"\n📊 Resultado:")
    print(f"   ✅ Renomeados: {renamed}")
    print(f"   ⏭️  Já corretos: {skipped}")
    print(f"   ❌ Erros: {errors}")

    if args.dry_run:
        print("\n   ⚠️  DRY RUN — nenhum arquivo foi alterado.")
        print("      Execute sem --dry-run para aplicar as alterações.")


if __name__ == "__main__":
    main()
