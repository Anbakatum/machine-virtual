#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
set -e

echo "=== 3/5. Instalando XFCE4 e Sunshine ==="
sudo echo 'debconf debconf/frontend select Noninteractive' | sudo debconf-set-selections
sudo apt-get update -y || true

# Instalação dos componentes gráficos e dependências
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
    xvfb x11vnc xfce4 xfce4-terminal libgbm1 libegl1 wget curl libssl-dev libavcodec-dev libavformat-dev libavutil-dev libswscale-dev

# Baixa e força a resolução de dependências do Sunshine
wget -q https://github.com/LizardByte/Sunshine/releases/latest/download/sunshine-ubuntu-22.04-amd64.deb -O /tmp/sunshine.deb
sudo dpkg -i --force-depends /tmp/sunshine.deb || true
sudo DEBIAN_FRONTEND=noninteractive apt-get install -f -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"
rm -f /tmp/sunshine.deb
