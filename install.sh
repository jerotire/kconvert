#!/usr/bin/env bash
# Install kconvert for the current user. Idempotent; safe to re-run.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="${HOME}/.local/bin"
MENU_DIR="${HOME}/.local/share/kio/servicemenus"

need() { command -v "$1" >/dev/null 2>&1; }

missing=()
need magick       || missing+=(imagemagick)
need notify-send  || missing+=(libnotify)
python3 -c 'import PyQt6' 2>/dev/null || missing+=(python-pyqt6)

if ((${#missing[@]})); then
  echo "Missing dependencies: ${missing[*]}"
  echo "Install with:  sudo pacman -S --needed ${missing[*]}"
  exit 1
fi

mkdir -p "$BIN_DIR" "$MENU_DIR"
install -m 755 "$HERE/bin/kconvert" "$BIN_DIR/kconvert"
install -m 755 "$HERE/share/kio/servicemenus/kconvert.desktop" "$MENU_DIR/kconvert.desktop"

if need kbuildsycoca6; then kbuildsycoca6 >/dev/null 2>&1 || true; fi

case ":$PATH:" in
  *":$BIN_DIR:"*) ;;
  *) echo "Warning: $BIN_DIR is not in PATH. Dolphin needs it to find kconvert." ;;
esac

echo "Installed. Restart Dolphin, right-click an image, pick Convert..."
