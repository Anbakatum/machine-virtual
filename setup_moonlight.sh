#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
set -e

echo "=== 1. Forçando modo não-interativo e desativando prompts ==="
sudo echo 'debconf debconf/frontend select Noninteractive' | sudo debconf-set-selections

echo "=== 2. Limpando travas e pacotes quebrados ==="
sudo killall apt apt-get 2>/dev/null || true
sudo rm -f /var/lib/apt/lists/lock /var/cache/apt/archives/lock /var/lib/dpkg/lock*
sudo dpkg --configure -a --force-confold

echo "=== 3. Instalando Tailscale ==="
curl -fsSL https://tailscale.com/install.sh | sh

echo "=== 4. Instalando XFCE4, Xvfb e Sunshine sem prompts ==="
sudo apt-get update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
    xvfb x11vnc xfce4 xfce4-terminal libgbm1 libegl1-mesa wget curl

# Baixa e instala o Sunshine
wget -q https://github.com/LizardByte/Sunshine/releases/latest/download/sunshine-ubuntu-22.04-amd64.deb -O /tmp/sunshine.deb
sudo DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/sunshine.deb || sudo DEBIAN_FRONTEND=noninteractive apt-get install -fy
rm -f /tmp/sunshine.deb

echo "=== 5. Inicializando Display Virtual ==="
export DISPLAY=:0
Xvfb :0 -screen 0 1920x1080x24 &
sleep 2
nohup startxfce4 >/dev/null 2>&1 &

echo "=== INSTALAÇÃO CONCLUÍDA ==="
