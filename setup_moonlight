#!/bin/bash
set -e

echo "=== 1. Instalando Tailscale ==="
curl -fsSL https://tailscale.com/install.sh | sh

echo "=== 2. Instalando Servidor X Virtual e Driver Virtual NVIDIA ==="
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc xfce4 xfce4-terminal libgbm1 libegl1-mesa

echo "=== 3. Instalando Sunshine (Streaming Server) ==="
wget https://github.com/LizardByte/Sunshine/releases/latest/download/sunshine-ubuntu-22.04-amd64.deb -O /tmp/sunshine.deb
sudo apt-get install -y /tmp/sunshine.deb
rm /tmp/sunshine.deb

echo "=== 4. Configurando Display Virtual ==="
export DISPLAY=:0
Xvfb :0 -screen 0 1920x1080x24 &
sleep 2
startxfce4 &

echo "=== Instalação Concluída ==="
