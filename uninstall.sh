#!/usr/bin/env bash
set -euo pipefail
rm -f "${HOME}/.local/bin/kconvert" \
      "${HOME}/.local/share/kio/servicemenus/kconvert.desktop"
command -v kbuildsycoca6 >/dev/null 2>&1 && kbuildsycoca6 >/dev/null 2>&1 || true
echo "Removed."
