#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
set -e

echo "=== 2/5. Instalando Tailscale ==="
if ! command -v tailscale &> /dev/null; then
    curl -fsSL https://tailscale.com/install.sh | sh
fi
