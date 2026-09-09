#!/bin/bash
set -e

echo "=== Baixando e Instalando Chrome Remote Desktop ==="
wget -q https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
sudo apt-get install -y ./chrome-remote-desktop_current_amd64.deb
rm chrome-remote-desktop_current_amd64.deb

# Define a interface XFCE como padrão para o Remote Desktop
sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'

echo "=== Chrome Remote Desktop Instalado ==="
