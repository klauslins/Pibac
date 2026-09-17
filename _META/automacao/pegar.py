#!/usr/bin/env python3
"""
pegar.py
Akza — Padrão Organizacional de Projetos de Comunicação v1.0

Resolve arquivos do ACERVO — os que não estão no Git.

Editáveis pesados, masters de impressão e mídia bruta não são versionados:
moram no NAS. O Git guarda apenas o registro deles no manifest (caminho,
tamanho, checksum). Este script é a ponte entre os dois.

Serve para pessoas e para agentes de IA. Um agente que clona o repositório
lê o AGENTS.md, descobre que parte do acervo está fora do Git, e chama este
script — em vez de tentar adivinhar o caminho do compartilhamento de rede,
que muda entre macOS, Windows e Linux.

Uso:
    python3 _META/automacao/pegar.py --listar
    python3 _META/automacao/pegar.py --onde outdoor-v2
    python3 _META/automacao/pegar.py --copiar outdoor-v2 ./trabalho/
    python3 _META/automacao/pegar.py --verificar
    python3 _META/automacao/pegar.py --listar --json      # saída para agente

Código de saída:
    0  tudo certo
    1  nada casou com o padrão informado
    2  o acervo não está montado nesta máquina
    3  checksum não confere (arquivo mudou ou corrompeu)

Dependências: nenhuma (stdlib Python 3.8+)
"""

import argparse
import hashlib
import json
import os
import platform
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST_PATH = PROJECT_ROOT / "_META" / "automacao" / "manifest.json"

# Arquivo-sentinela na raiz do share. Confirma que o caminho montado é
# mesmo o acervo da Akza, e não outro volume que calhou de ter o nome.
SENTINELA = ".akza-acervo"

# Variável de ambiente tem precedência sobre a detecção automática.
ENV_RAIZ = "AKZA_ACERVO"

CHUNK = 1 << 20  # 1 MiB


# ─── Manifest ────────────────────────────────────────────────────────────────

def carregar_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        erro(f"manifest não encontrado em {MANIFEST_PATH.relative_to(PROJECT_ROOT)}")
        sys.exit(1)
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def bloco_acervo(manifest: dict) -> dict:
    """Configuração de onde o acervo mora. Ausente = projeto sem acervo."""
    return manifest.get("acervo") or {}


# ─── Localizar o acervo nesta máquina ────────────────────────────────────────

def candidatos(acervo: dict) -> list:
    """Caminhos onde o share pode estar montado, em ordem de preferência."""
    do_env = os.environ.get(ENV_RAIZ)
    if do_env:
        return [Path(do_env)]

    mounts = acervo.get("mount") or {}
    sistema = platform.system()
    chave = {"Darwin": "macos", "Windows": "windows", "Linux": "linux"}.get(sistema)

    lista = []
    if chave and mounts.get(chave):
        lista.append(Path(mounts[chave]))

    # Palpites por sistema, para quem montou no lugar padrão sem configurar.
    share = acervo.get("share", "projetos")
    if sistema == "Darwin":
        lista.append(Path("/Volumes") / share)
    elif sistema == "Linux":
        lista.append(Path("/mnt") / "akza" / share)
        lista.append(Path("/media") / share)
    elif sistema == "Windows":
        for letra in "ZYXW":
            lista.append(Path(f"{letra}:\\"))

    return lista


def encontrar_raiz(acervo: dict) -> Path:
    """Primeiro candidato que exista e tenha a sentinela. Sai com 2 se nenhum."""
    testados = candidatos(acervo)
    for base in testados:
        if (base / SENTINELA).exists():
            return base
    # Aceita sem sentinela se o caminho existe e foi dado explicitamente.
    for base in testados[:1]:
        if base.is_dir():
            aviso(f"{base} existe mas não tem o arquivo {SENTINELA} — seguindo assim mesmo")
            return base

    erro("o acervo não está montado nesta máquina")
    print()
    print("  Onde procurei:")
    for base in testados:
        print(f"    · {base}")
    print()
    print("  Para montar (macOS):")
    host = acervo.get("host", "nas-akza.local")
    share = acervo.get("share", "projetos")
    print(f"    open 'smb://{host}/{share}'")
    print()
    print(f"  Ou aponte direto:  export {ENV_RAIZ}=/caminho/do/share")
    sys.exit(2)


# ─── Checksum ────────────────────────────────────────────────────────────────

def sha256(caminho: Path) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(CHUNK), b""):
            h.update(bloco)
    return h.hexdigest()


def confere(asset: dict, caminho: Path) -> bool:
    """True se bate, False se não bate, True se o manifest não tem sha256."""
    esperado = asset.get("sha256")
    if not esperado:
        return True
    return sha256(caminho) == esperado


# ─── Resolução ───────────────────────────────────────────────────────────────

def fora_do_git(manifest: dict) -> list:
    return [a for a in manifest.get("assets", []) if not a.get("in_git", True)]


def casar(assets: list, padrao: str) -> list:
    """Busca por substring, sem diferenciar maiúsculas, no id e no caminho."""
    p = padrao.lower()
    return [a for a in assets if p in a.get("id", "").lower()
            or p in a.get("file", "").lower()]


def caminho_local(asset: dict, raiz_acervo: Path, acervo: dict) -> Path:
    """Onde o arquivo está de fato nesta máquina."""
    if asset.get("in_git", True):
        return PROJECT_ROOT / asset["file"]
    sub = acervo.get("raiz", "")
    return raiz_acervo / sub / asset["file"] if sub else raiz_acervo / asset["file"]


# ─── Saída ───────────────────────────────────────────────────────────────────

def erro(msg):  print(f"❌ {msg}", file=sys.stderr)
def aviso(msg): print(f"⚠️  {msg}", file=sys.stderr)
def ok(msg):    print(f"✅ {msg}")


def humano(n: int) -> str:
    for unidade in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unidade == "TB":
            return f"{n:.0f} {unidade}" if unidade == "B" else f"{n:.1f} {unidade}"
        n /= 1024


# ─── Comandos ────────────────────────────────────────────────────────────────

def cmd_listar(manifest, args):
    assets = fora_do_git(manifest)
    if args.padrao:
        assets = casar(assets, args.padrao)

    if args.json:
        acervo = bloco_acervo(manifest)
        print(json.dumps({
            "acervo": acervo,
            "total": len(assets),
            "assets": [{
                "id": a["id"],
                "file": a["file"],
                "size_bytes": a.get("size_bytes"),
                "sha256": a.get("sha256"),
            } for a in assets],
        }, ensure_ascii=False, indent=2))
        return 0

    if not assets:
        print("Nenhum arquivo fora do Git registrado no manifest.")
        return 0

    print(f"{len(assets)} arquivo(s) no acervo, fora do Git:\n")
    for a in assets:
        tam = humano(a.get("size_bytes", 0))
        print(f"  {tam:>9}  {a['file']}")
    print()
    print("Para trazer um deles:  pegar.py --copiar <parte-do-nome> <destino>")
    return 0


def cmd_onde(manifest, args):
    acervo = bloco_acervo(manifest)
    achados = casar(manifest.get("assets", []), args.padrao)
    if not achados:
        erro(f"nada no manifest casa com '{args.padrao}'")
        return 1

    raiz = encontrar_raiz(acervo) if any(
        not a.get("in_git", True) for a in achados) else None

    for a in achados:
        destino = caminho_local(a, raiz, acervo) if raiz else PROJECT_ROOT / a["file"]
        marca = "git" if a.get("in_git", True) else "nas"
        existe = "" if destino.exists() else "  (não encontrado no disco)"
        print(f"[{marca}] {destino}{existe}")
    return 0


def cmd_copiar(manifest, args):
    acervo = bloco_acervo(manifest)
    achados = casar(manifest.get("assets", []), args.padrao)
    if not achados:
        erro(f"nada no manifest casa com '{args.padrao}'")
        return 1
    if len(achados) > 1:
        erro(f"'{args.padrao}' casa com {len(achados)} arquivos — seja mais específico:")
        for a in achados[:10]:
            print(f"    {a['file']}", file=sys.stderr)
        return 1

    asset = achados[0]
    raiz = encontrar_raiz(acervo) if not asset.get("in_git", True) else None
    origem = caminho_local(asset, raiz, acervo)

    if not origem.exists():
        erro(f"o manifest registra este arquivo, mas ele não está lá:\n   {origem}")
        return 1

    # Barra no fim, ou pasta que já existe, significa "coloque dentro dela".
    # Sem isso, `--copiar x ./trabalho/` cria um ARQUIVO chamado trabalho.
    pede_pasta = args.destino.endswith(("/", os.sep)) or Path(args.destino).is_dir()
    destino = Path(args.destino)
    if pede_pasta:
        destino.mkdir(parents=True, exist_ok=True)
        destino = destino / origem.name
    else:
        destino.parent.mkdir(parents=True, exist_ok=True)

    print(f"📥 {origem}")
    print(f"   → {destino}  ({humano(asset.get('size_bytes', origem.stat().st_size))})")
    shutil.copy2(origem, destino)

    if not confere(asset, destino):
        erro("checksum não confere — o arquivo no acervo mudou desde o último manifest")
        print(f"   esperado: {asset.get('sha256')}", file=sys.stderr)
        print(f"   obtido:   {sha256(destino)}", file=sys.stderr)
        return 3

    ok("copiado e verificado")
    return 0


def cmd_verificar(manifest, args):
    assets = fora_do_git(manifest)
    if not assets:
        print("Nenhum arquivo fora do Git para verificar.")
        return 0

    acervo = bloco_acervo(manifest)
    raiz = encontrar_raiz(acervo)

    faltando, divergente, integros = [], [], 0
    for a in assets:
        caminho = caminho_local(a, raiz, acervo)
        if not caminho.exists():
            faltando.append(a)
            continue
        if not confere(a, caminho):
            divergente.append(a)
            continue
        integros += 1

    print(f"Acervo em {raiz}\n")
    print(f"  ✅ íntegros:    {integros}")
    print(f"  ⚠️  divergentes: {len(divergente)}")
    print(f"  ❌ faltando:    {len(faltando)}")

    for rotulo, grupo in (("faltando", faltando), ("divergente", divergente)):
        if grupo:
            print(f"\n  {rotulo}:")
            for a in grupo:
                print(f"    · {a['file']}")

    if faltando:
        return 1
    if divergente:
        return 3
    return 0


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description="Resolve arquivos do acervo que não estão no Git.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Uso:")[1].split("Código de saída:")[0].strip(),
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--listar", action="store_true", help="lista o que está fora do Git")
    g.add_argument("--onde", metavar="PADRAO", help="mostra o caminho local de um arquivo")
    g.add_argument("--copiar", metavar="PADRAO", help="copia um arquivo do acervo para cá")
    g.add_argument("--verificar", action="store_true", help="confere presença e checksum de tudo")
    p.add_argument("destino", nargs="?", default=".", help="destino do --copiar")
    p.add_argument("--padrao", help="filtra o --listar")
    p.add_argument("--json", action="store_true", help="saída em JSON, para agentes")
    args = p.parse_args()

    manifest = carregar_manifest()

    if args.listar:
        return cmd_listar(manifest, args)
    if args.onde:
        args.padrao = args.onde
        return cmd_onde(manifest, args)
    if args.copiar:
        args.padrao = args.copiar
        return cmd_copiar(manifest, args)
    if args.verificar:
        return cmd_verificar(manifest, args)


if __name__ == "__main__":
    sys.exit(main())
