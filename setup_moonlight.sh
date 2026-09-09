#!/bin/bash
set -e

echo "=== 1. Liberando travamentos do sistema ==="
sudo killall apt apt-get 2>/dev/null || true
sudo rm -f /var/lib/apt/lists/lock /var/cache/apt/archives/lock /var/lib/dpkg/lock*
sudo dpkg --configure -a

echo "=== 2. Instalando Tailscale ==="
curl -fsSL https://tailscale.com/install.sh | sh

echo "=== 3. Instalando Interface Gráfica e Sunshine ==="
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc xfce4 xfce4-terminal libgbm1 libegl1-mesa wget

wget https://github.com/LizardByte/Sunshine/releases/latest/download/sunshine-ubuntu-22.04-amd64.deb -O /tmp/sunshine.deb
sudo apt-get install -y /tmp/sunshine.deb || sudo apt-get install -fy
rm -f /tmp/sunshine.deb

echo "=== 4. Inicializando Display Virtual ==="
export DISPLAY=:0
Xvfb :0 -screen 0 1920x1080x24 &
sleep 2
nohup startxfce4 >/dev/null 2>&1 &

echo "=== Instalação concluída com sucesso! ==="
