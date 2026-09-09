#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
set -e

echo "=== 3/5. Instalando XFCE4 e Sunshine ==="
sudo echo 'debconf debconf/frontend select Noninteractive' | sudo debconf-set-selections
sudo apt-get update -y || true

# Instalação dos componentes gráficos base
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
    xvfb x11vnc xfce4 xfce4-terminal libgbm1 libegl1 wget curl libssl-dev libboost-program-options-dev libminiupnpc-dev libevdev-dev

# Instalar Sunshine AppImage portátil e registrar no sistema
if ! command -v sunshine &> /dev/null; then
    wget -q https://github.com/LizardByte/Sunshine/releases/latest/download/sunshine.AppImage -O /usr/bin/sunshine
    chmod +x /usr/bin/sunshine
fi
