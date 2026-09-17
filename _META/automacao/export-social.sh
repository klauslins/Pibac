#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# export-social.sh
# Akza — Pipeline de Comunicação v1.0
#
# Exporta e redimensiona imagens de 05_EXPORTS/[campanha]/ para os formatos
# corretos de cada plataforma usando ImageMagick (convert).
#
# Pré-requisito: brew install imagemagick
#
# Uso:
#   bash _META/automacao/export-social.sh [campanha]
#   bash _META/automacao/export-social.sh lancamento-conteudo-ago-2026
#
#   Se nenhuma campanha for passada, processa todas em 05_EXPORTS/
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

# ─── Configuração ─────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
EXPORTS_DIR="$PROJECT_ROOT/05_EXPORTS"
PUBLISH_READY="$PROJECT_ROOT/05_EXPORTS/_PUBLISH-READY"

# Verificar ImageMagick. O IM 7 renomeou "convert" para "magick" — o nome
# antigo ainda funciona no IM 6 e foi removido no 7, então detectamos os dois.
if command -v magick &>/dev/null; then
  IM="magick"
elif command -v convert &>/dev/null; then
  IM="convert"
else
  echo "❌ ImageMagick não encontrado."
  echo "   Instale com: brew install imagemagick"
  exit 1
fi

# ─── Especificações por plataforma ────────────────────────────────────────────
# Formato: "plataforma:formato:WxH:qualidade"

declare -a SPECS=(
  "instagram:feed-1x1:1080x1080:85"
  "instagram:story-9x16:1080x1920:85"
  "linkedin:post-1200x628:1200x628:85"
  "youtube:thumbnail-1280x720:1280x720:90"
)

# ─── Funções ──────────────────────────────────────────────────────────────────

process_image() {
  local src="$1"
  local out_dir="$2"
  local size="$3"
  local quality="$4"
  local filename
  filename=$(basename "$src")
  local out="$out_dir/$filename"

  mkdir -p "$out_dir"

  # Redimensiona com crop central (cover) + otimização
  "$IM" "$src" \
    -resize "${size}^" \
    -gravity center \
    -extent "$size" \
    -strip \
    -quality "$quality" \
    -colorspace sRGB \
    "$out"

  echo "   ✅ $(basename "$out_dir")/$(basename "$out")"
}

process_campaign() {
  local campaign_dir="$1"
  local campaign
  campaign=$(basename "$campaign_dir")

  # Pula _PUBLISH-READY
  [[ "$campaign" == "_PUBLISH-READY" ]] && return

  echo ""
  echo "📁 Campanha: $campaign"

  # Busca imagens fonte (web/ ou root da campanha)
  local sources=()
  while IFS= read -r -d $'\0' f; do
    sources+=("$f")
  done < <(find "$campaign_dir" -maxdepth 2 \
    \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) \
    -not -name "._*" \
    -not -path "*/_*" \
    -print0 2>/dev/null)

  if [[ ${#sources[@]} -eq 0 ]]; then
    echo "   ⚠️  Nenhuma imagem encontrada em $campaign"
    return
  fi

  for src in "${sources[@]}"; do
    echo "   🔄 Processando: $(basename "$src")"
    for spec in "${SPECS[@]}"; do
      IFS=':' read -r platform format size quality <<< "$spec"
      local out_dir="$campaign_dir/social/$platform/$format"
      process_image "$src" "$out_dir" "$size" "$quality"
    done
  done
}

# ─── Main ────────────────────────────────────────────────────────────────────

CAMPAIGN="${1:-}"

echo "🚀 export-social.sh — Akza Pipeline"
echo "   Projeto: $PROJECT_ROOT"

if [[ -n "$CAMPAIGN" ]]; then
  campaign_dir="$EXPORTS_DIR/$CAMPAIGN"
  if [[ ! -d "$campaign_dir" ]]; then
    echo "❌ Campanha não encontrada: $campaign_dir"
    exit 1
  fi
  process_campaign "$campaign_dir"
else
  echo "   Processando todas as campanhas em 05_EXPORTS/..."
  for dir in "$EXPORTS_DIR"/*/; do
    [[ -d "$dir" ]] && process_campaign "$dir"
  done
fi

echo ""
echo "✅ Export concluído!"
echo "   Verifique os arquivos gerados em 05_EXPORTS/[campanha]/social/"
