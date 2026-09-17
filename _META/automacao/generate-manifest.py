#!/usr/bin/env python3
"""
generate-manifest.py
Akza — Pipeline de Comunicação v1.0

Percorre as pastas 04_PRODUCTION/ e 05_EXPORTS/ e atualiza o manifest.json
com todos os assets encontrados, preservando metadados já existentes.

Uso:
    python3 _META/automacao/generate-manifest.py
    python3 _META/automacao/generate-manifest.py --dry-run   # mostra sem salvar

Dependências: nenhuma (apenas stdlib Python 3.8+)
"""

import json
import os
import sys
import hashlib
import argparse
from datetime import date
from pathlib import Path

# ─── Configuração ────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).parent.parent.parent
MANIFEST_PATH = PROJECT_ROOT / "_META" / "automacao" / "manifest.json"
CONFIG_PATH = PROJECT_ROOT / "_META" / "automacao" / "pipeline-config.json"

SCAN_DIRS = [
    PROJECT_ROOT / "00_BRAND",      # identidade visual
    PROJECT_ROOT / "04_PRODUCTION", # editáveis em andamento
    PROJECT_ROOT / "05_EXPORTS",    # entregáveis por canal
    PROJECT_ROOT / "07_IMPRESSOS",  # peças de gráfica
    PROJECT_ROOT / "08_MASTERS",    # masters fora do Git — indexar é essencial
]

# Pastas cujo conteúdo NÃO é versionado pelo Git (ver .gitignore).
# Para esses arquivos o manifest é o único registro de que existem.
FORA_DO_GIT = ("08_MASTERS", "06_MEDIA/videos/brutos", "06_MEDIA/fotos/originais")

IGNORE_PATTERNS = [
    "._*",        # macOS metadata files
    ".DS_Store",
    "*.tmp",
    "_briefing.md",
    "README.md",
]

KNOWN_EXTENSIONS = {
    # Editáveis
    ".ai": "source", ".psd": "source", ".indd": "source", ".fig": "source",
    # Web
    ".jpg": "export", ".jpeg": "export", ".png": "export",
    ".webp": "export", ".gif": "export", ".svg": "export",
    # Vídeo
    ".mp4": "export", ".mov": "export", ".webm": "export",
    # Print
    ".pdf": "export", ".tif": "export", ".tiff": "export", ".eps": "export",
    # Marca
    ".otf": "font", ".ttf": "font",
    ".docx": "document",
}


# ─── Helpers ──────────────────────────────────────────────────────────────────

def file_id(filepath: Path) -> str:
    """Gera ID único a partir do caminho relativo completo.

    Usar apenas o nome (stem) colide: `logo-h-oficial-v1` existe em .ai,
    .eps, .png e .svg — quatro arquivos distintos com o mesmo stem. Com o
    caminho, cada um vira um asset próprio e o merge não mistura metadados.
    """
    return str(filepath.relative_to(PROJECT_ROOT))


def file_hash(filepath: Path) -> str:
    """MD5 rápido dos primeiros 64KB do arquivo."""
    h = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            h.update(f.read(65536))
        return h.hexdigest()
    except Exception:
        return ""


def parse_filename(name: str) -> dict:
    """
    Extrai metadados do nome do arquivo seguindo o padrão:
    [type]-[slug]-[variant]-v[N].[ext]
    """
    parts = name.split("-")
    version = None
    for part in reversed(parts):
        if part.startswith("v") and part[1:].isdigit():
            version = int(part[1:])
            break
    return {
        "type": parts[0] if parts else "unknown",
        "version": version or 1,
    }


def should_ignore(filename: str) -> bool:
    import fnmatch
    for pattern in IGNORE_PATTERNS:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


# ─── Scanner ──────────────────────────────────────────────────────────────────

def scan_assets() -> list:
    assets = []
    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for filepath in scan_dir.rglob("*"):
            if not filepath.is_file():
                continue
            if should_ignore(filepath.name):
                continue
            ext = filepath.suffix.lower()
            if ext not in KNOWN_EXTENSIONS:
                continue

            relative = filepath.relative_to(PROJECT_ROOT)
            meta = parse_filename(filepath.stem)
            asset_type = KNOWN_EXTENSIONS[ext]

            asset = {
                "id": file_id(filepath),
                "type": meta["type"],
                "file_type": asset_type,
                "file": str(relative),
                "extension": ext.lstrip("."),
                "size_bytes": filepath.stat().st_size,
                "hash_md5": file_hash(filepath),
                "version": meta["version"],
                "in_git": not str(relative).startswith(FORA_DO_GIT),
                "status": "draft",
                "campaign": None,
                "platform": None,
                "format": None,
                "copy": None,
                "approved_by": None,
                "published_at": None,
                "tags": [],
                "created_at": str(date.today()),
                "updated_at": str(date.today()),
            }
            assets.append(asset)
    return assets


# ─── Merge ────────────────────────────────────────────────────────────────────

def merge_assets(existing: list, discovered: list) -> list:
    """
    Combina assets existentes com os descobertos.
    Preserva metadados manuais (status, approved_by, campaign, etc.)
    """
    existing_map = {a["id"]: a for a in existing}
    result = []
    for asset in discovered:
        if asset["id"] in existing_map:
            merged = {**asset, **{
                k: v for k, v in existing_map[asset["id"]].items()
                if k not in ["file", "size_bytes", "hash_md5", "updated_at"]
            }}
            merged["updated_at"] = str(date.today())
            result.append(merged)
        else:
            result.append(asset)
    return result


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gera/atualiza o manifest.json do projeto")
    parser.add_argument("--dry-run", action="store_true", help="Mostra o resultado sem salvar")
    args = parser.parse_args()

    print(f"📂 Projeto: {PROJECT_ROOT}")
    print(f"🔍 Varrendo assets...")

    # Carrega manifest existente
    existing_assets = []
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            existing_assets = data.get("assets", [])
        print(f"   ✅ Manifest existente carregado ({len(existing_assets)} assets)")

    # Descobre assets
    discovered = scan_assets()
    print(f"   🔎 {len(discovered)} assets indexados")

    # Merge
    merged = merge_assets(existing_assets, discovered)

    # Carrega manifest completo
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    manifest["assets"] = merged
    manifest["project"]["updated_at"] = str(date.today())

    if args.dry_run:
        print("\n📋 DRY RUN — Resultado (não salvo):")
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
    else:
        with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"\n✅ manifest.json atualizado com {len(merged)} assets em:")
        print(f"   {MANIFEST_PATH}")

    # Resumo por status
    from collections import Counter
    status_count = Counter(a.get("status", "unknown") for a in merged)
    print("\n📊 Assets por status:")
    for status, count in status_count.most_common():
        print(f"   {status}: {count}")


if __name__ == "__main__":
    main()
