#!/bin/bash
set -e

echo "=== 5/5. Subindo Daemon do Tailscale ==="
sudo mkdir -p /var/run/tailscale /var/lib/tailscale

# Encerra processos antigos
sudo killall tailscaled 2>/dev/null || true

# Inicia o daemon com a flag userspace-networking
sudo tailscaled --tun=userspace-networking --state=/var/lib/tailscale/tailscaled.state --socket=/var/run/tailscale/tailscaled.sock > /dev/null 2>&1 &

# Aguarda a criação do socket
for i in {1..15}; do
    if [ -S /var/run/tailscale/tailscaled.sock ]; then
        echo "Daemon do Tailscale ativo com sucesso!"
        exit 0
    fi
    sleep 1
done

echo "Erro ao iniciar o socket do Tailscale."
exit 1
