#!/usr/bin/env python3
"""Gera CSS, SCSS e preset Tailwind a partir de 00_BRAND/tokens/tokens.json.

O tokens.json e a unica fonte da verdade da marca. Edite so ele e rode:

    python3 _META/automacao/gerar-tokens.py

Token com "$value": null e decisao de design ainda nao tomada. Enquanto
houver algum, o script recusa gerar e lista o que falta — melhor nao ter
arquivo do que ter arquivo com valor inventado.

Baseado no gerar-tokens.py do padrao organizacional Akza v1.5.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ORIGEM = RAIZ / "00_BRAND" / "tokens" / "tokens.json"
DESTINO = ORIGEM.parent
PREFIXO = "pibac"

CABECALHO = (
    "PIBAC — design tokens\n"
    "GERADO AUTOMATICAMENTE por _META/automacao/gerar-tokens.py\n"
    "Nao edite este arquivo. Edite 00_BRAND/tokens/tokens.json e rode o script."
)


def achatar(no: dict, prefixo: tuple[str, ...] = ()) -> dict[str, dict]:
    """Percorre a arvore e devolve {'cor-marca-primaria': {...token...}}."""
    saida = {}
    for chave, valor in no.items():
        if chave.startswith("$"):
            continue
        caminho = prefixo + (chave,)
        if isinstance(valor, dict) and "$value" in valor:
            saida["-".join(caminho)] = valor
        elif isinstance(valor, dict):
            saida.update(achatar(valor, caminho))
    return saida


def resolver(valor, plano: dict[str, dict]) -> str:
    """Troca referencias {cor.marca.primaria} pelo valor final."""
    if not isinstance(valor, str):
        return str(valor)
    for _ in range(10):
        alvos = re.findall(r"\{([^}]+)\}", valor)
        if not alvos:
            break
        for alvo in alvos:
            chave = alvo.replace(".", "-")
            if chave not in plano:
                raise SystemExit(f"referencia quebrada: {{{alvo}}}")
            destino = plano[chave]["$value"]
            if destino is None:
                raise SystemExit(f"{{{alvo}}} aponta para um token ainda nao decidido")
            valor = valor.replace("{" + alvo + "}", str(destino))
    return valor


def escrever(caminho: Path, conteudo: str) -> None:
    caminho.write_text(conteudo, encoding="utf-8")
    print(f"  escrito  {caminho.relative_to(RAIZ)}")


def por_grupo(resolvido: dict[str, str], prefixo: str) -> dict:
    """Agrupa 'cor-marca-primaria' em {'marca': {'primaria': ...}}."""
    saida: dict = {}
    for chave, valor in resolvido.items():
        if not chave.startswith(prefixo + "-"):
            continue
        partes = chave[len(prefixo) + 1:].split("-")
        if len(partes) == 1:
            saida[partes[0]] = valor
        else:
            saida.setdefault(partes[0], {})["-".join(partes[1:])] = valor
    return saida


def plano_de_grupo(resolvido: dict[str, str], prefixo: str) -> dict[str, str]:
    return {
        k[len(prefixo) + 1:]: v
        for k, v in resolvido.items()
        if k.startswith(prefixo + "-")
    }


def main() -> int:
    if not ORIGEM.exists():
        raise SystemExit(f"nao encontrei {ORIGEM}")

    dados = json.loads(ORIGEM.read_text(encoding="utf-8"))
    plano = achatar(dados)

    pendentes = [k for k, v in plano.items() if v["$value"] is None]
    if pendentes:
        print(f"❌ {len(pendentes)} token(s) ainda sem valor — nada foi gerado.\n")
        print("   Decida em 00_BRAND/tokens/tokens.json e rode de novo:\n")
        for k in pendentes:
            print(f"     {k}")
        print("\n   Enquanto houver null aqui, o CSS nao existe — de proposito.")
        return 1

    resolvido = {k: resolver(v["$value"], plano) for k, v in plano.items()}

    # ---------- CSS ----------
    linhas = ["/*", *[f" * {l}" for l in CABECALHO.splitlines()], " */", "", ":root {"]
    grupo_atual = None
    for chave, valor in resolvido.items():
        grupo = chave.split("-")[0]
        if grupo != grupo_atual:
            linhas.append("")
            grupo_atual = grupo
        linhas.append(f"  --{PREFIXO}-{chave}: {valor};")
    linhas += ["}", ""]
    escrever(DESTINO / "tokens.css", "\n".join(linhas))

    # ---------- SCSS ----------
    linhas = [*[f"// {l}" for l in CABECALHO.splitlines()], ""]
    grupo_atual = None
    for chave, valor in resolvido.items():
        grupo = chave.split("-")[0]
        if grupo != grupo_atual:
            linhas.append("")
            grupo_atual = grupo
        linhas.append(f"${PREFIXO}-{chave}: {valor};")
    linhas.append("")
    escrever(DESTINO / "tokens.scss", "\n".join(linhas))

    # ---------- Tailwind ----------
    # Os grupos de cor saem do proprio tokens.json: criou "cor.liturgica",
    # ela aparece aqui sozinha. Nada de lista fixa para esquecer de atualizar.
    preset = {
        "theme": {
            "extend": {
                "colors": por_grupo(resolvido, "cor"),
                "fontFamily": {
                    k: [p.strip().strip("'\"") for p in v.split(",")]
                    for k, v in plano_de_grupo(resolvido, "fonte-familia").items()
                },
                "fontWeight": plano_de_grupo(resolvido, "fonte-peso"),
                "fontSize": plano_de_grupo(resolvido, "fonte-tamanho"),
                "lineHeight": plano_de_grupo(resolvido, "fonte-entrelinha"),
                "letterSpacing": plano_de_grupo(resolvido, "fonte-tracking"),
                "spacing": plano_de_grupo(resolvido, "espaco"),
                "borderRadius": plano_de_grupo(resolvido, "raio"),
                "boxShadow": plano_de_grupo(resolvido, "sombra"),
            }
        }
    }
    corpo = json.dumps(preset, indent=2, ensure_ascii=False)
    escrever(
        DESTINO / "tailwind.preset.js",
        "\n".join(f"// {l}" for l in CABECALHO.splitlines())
        + f"\n\nmodule.exports = {corpo};\n",
    )

    print(f"\n✅ {len(resolvido)} tokens gerados a partir de {ORIGEM.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
