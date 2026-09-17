#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# publish-pipeline.sh
# Akza — Pipeline de Comunicação v1.0
#
# Valida e move assets aprovados de 05_EXPORTS/[campanha]/ para
# 05_EXPORTS/_PUBLISH-READY/, garantindo que seguem todas as convenções.
#
# Uso:
#   bash _META/automacao/publish-pipeline.sh [campanha] [--force]
#
#   --force  move sem validação de nome (use com cuidado)
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
MANIFEST="$PROJECT_ROOT/_META/automacao/manifest.json"
PUBLISH_READY="$PROJECT_ROOT/05_EXPORTS/_PUBLISH-READY"
EXPORTS_DIR="$PROJECT_ROOT/05_EXPORTS"

CAMPAIGN="${1:-}"
FORCE="${2:-}"

# ─── Funções ──────────────────────────────────────────────────────────────────

log_info()    { echo "   ℹ️  $*"; }
log_ok()      { echo "   ✅ $*"; }
log_warn()    { echo "   ⚠️  $*"; }
log_error()   { echo "   ❌ $*" >&2; }

validate_filename() {
  local name="$1"
  # Verifica: apenas letras minúsculas, números, hífens, extensão permitida
  if echo "$name" | grep -qP '[^\x00-\x7F]'; then
    echo "tem caracteres não-ASCII (acentos)"
    return 1
  fi
  if echo "$name" | grep -q ' '; then
    echo "tem espaços"
    return 1
  fi
  if echo "$name" | grep -qP '[A-Z]'; then
    echo "tem letras maiúsculas"
    return 1
  fi
  echo "ok"
  return 0
}

move_to_publish() {
  local src="$1"
  local campaign="$2"
  local filename
  filename=$(basename "$src")

  # Valida nome
  if [[ "$FORCE" != "--force" ]]; then
    result=$(validate_filename "$filename")
    if [[ "$result" != "ok" ]]; then
      log_warn "Ignorado ($result): $filename"
      log_warn "→ Renomeie com: python3 _META/automacao/rename-assets.py $(dirname "$src")"
      return
    fi
  fi

  # Verifica se contém número de versão
  if ! echo "$filename" | grep -qP '\-v\d+\.'; then
    log_warn "Sem versão no nome: $filename (esperado: -v1, -v2, etc.)"
    [[ "$FORCE" != "--force" ]] && return
  fi

  local dest_dir="$PUBLISH_READY/$campaign"
  mkdir -p "$dest_dir"
  cp "$src" "$dest_dir/$filename"
  log_ok "Copiado → _PUBLISH-READY/$campaign/$filename"
}

process_campaign() {
  local campaign_dir="$1"
  local campaign
  campaign=$(basename "$campaign_dir")
  [[ "$campaign" == "_PUBLISH-READY" ]] && return

  echo ""
  echo "📦 Processando campanha: $campaign"

  local count=0
  while IFS= read -r -d $'\0' f; do
    move_to_publish "$f" "$campaign"
    ((count++)) || true
  done < <(find "$campaign_dir" -type f \
    \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \
       -o -name "*.mp4" -o -name "*.pdf" -o -name "*.webp" \) \
    -not -name "._*" \
    -not -path "*/_*" \
    -print0 2>/dev/null)

  if [[ $count -eq 0 ]]; then
    log_info "Nenhum arquivo exportável encontrado"
  fi
}

# ─── Main ────────────────────────────────────────────────────────────────────

echo "🚀 publish-pipeline.sh — Akza Pipeline"
echo "   Projeto: $PROJECT_ROOT"
echo "   Destino: _PUBLISH-READY/"
[[ "$FORCE" == "--force" ]] && echo "   ⚠️  Modo FORCE ativo — validações ignoradas"

mkdir -p "$PUBLISH_READY"

if [[ -n "$CAMPAIGN" && "$CAMPAIGN" != "--force" ]]; then
  campaign_dir="$EXPORTS_DIR/$CAMPAIGN"
  if [[ ! -d "$campaign_dir" ]]; then
    log_error "Campanha não encontrada: $campaign_dir"
    exit 1
  fi
  process_campaign "$campaign_dir"
else
  for dir in "$EXPORTS_DIR"/*/; do
    [[ -d "$dir" ]] && process_campaign "$dir"
  done
fi

echo ""
echo "✅ Pipeline concluído!"
echo "   Verifique: $PUBLISH_READY"
echo ""
echo "📋 Próximo passo:"
echo "   Verifique os arquivos em _PUBLISH-READY/ e publique manualmente"
echo "   ou integre com sua plataforma de agendamento."
