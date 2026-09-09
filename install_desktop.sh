#!/bin/bash
set -e

echo "=== Ativando suporte a 32-bit e atualizando pacotes ==="
sudo dpkg --add-architecture i386
sudo apt-get update -y

echo "=== Instalando Interface Gráfica (XFCE4) e Utilitários ==="
DEBIAN_FRONTEND=noninteractive sudo apt-get install -y \
    xfce4 \
    xfce4-terminal \
    desktop-base \
    dbus-x11 \
    p7zip-full \
    htop \
    wget \
    curl

echo "=== Instalando Google Chrome ==="
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

echo "=== Instalando Dependências da Steam ==="
sudo apt-get install -y steam || true

echo "=== Instalação de pacotes concluída ==="
