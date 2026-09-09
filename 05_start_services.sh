#!/bin/bash
set -e

echo "=== 5/5. Subindo Daemon do Tailscale ==="
sudo mkdir -p /var/run/tailscale /var/lib/tailscale

# Mata instâncias antigas e sobe o daemon apontando o socket
sudo killall tailscaled 2>/dev/null || true
sudo tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/var/run/tailscale/tailscaled.sock > /dev/null 2>&1 &

# Aguarda a criação do socket
for i in {1..10}; do
    if [ -S /var/run/tailscale/tailscaled.sock ]; then
        echo "Daemon do Tailscale ativo com sucesso!"
        exit 0
    fi
    sleep 1
done

echo "Erro: O daemon do Tailscale não iniciou o socket a tempo."
exit 1
