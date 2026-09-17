#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
#  limpar-sidecars.sh — remove o lixo que o macOS planta no .git
#
#  POR QUE EXISTE: o SSD é exFAT, que não guarda os metadados
#  estendidos do macOS. Para não perdê-los, o Finder grava um arquivo
#  irmão "._nome" ao lado de cada arquivo. Dentro de .git isso vira
#  problema: o git tenta ler "._<sha>" como objeto e "._pack-*.idx"
#  como índice de pack, e responde "bad sha1 file" ou
#  "non-monotonic index" em todo comando.
#
#  Roda depois de commit, checkout e merge — os três momentos em que
#  o git escreve dentro de .git.
# ═══════════════════════════════════════════════════════════════════
set -u
RAIZ="$(git rev-parse --git-dir 2>/dev/null)" || exit 0
find "$RAIZ" -name '._*' -delete 2>/dev/null
exit 0
