#!/bin/bash
set -e

echo "=== 4/5. Inicializando Display Virtual ==="
export DISPLAY=:0
Xvfb :0 -screen 0 1920x1080x24 &
sleep 2
nohup startxfce4 >/dev/null 2>&1 &
