#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
set -e

echo "=== 3/5. Instalando XFCE4 e Sunshine ==="
sudo echo 'debconf debconf/frontend select Noninteractive' | sudo debconf-set-selections
sudo apt-get update -y || true

# Componentes gráficos base
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
    xvfb x11vnc xfce4 xfce4-terminal libgbm1 libegl1 wget curl libssl-dev libboost-program-options-dev libminiupnpc-dev libevdev-dev

# Baixa AppImage do Sunshine e concede permissões
if [ ! -f /usr/bin/sunshine ]; then
    sudo wget -q https://github.com/LizardByte/Sunshine/releases/latest/download/sunshine.AppImage -O /usr/bin/sunshine
    sudo chmod 755 /usr/bin/sunshine
fi
