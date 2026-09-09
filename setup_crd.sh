#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "ERRO: Forneça seu NGROK AUTHTOKEN."
    echo "Uso: ./run_vnc.sh SEU_AUTHTOKEN_AQUI"
    exit 1
fi

NGROK_TOKEN=$1

echo "=== Instalando Interface Gráfica e VNC ==="
sudo apt-get update -y
sudo apt-get install -y xfce4 xfce4-terminal desktop-base dbus-x11 tigervnc-standalone-server novnc wget curl htop

echo "=== Instalando Chrome ==="
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb
sudo apt-get install -y /tmp/chrome.deb && rm /tmp/chrome.deb

echo "=== Configurando VNC ==="
mkdir -p ~/.vnc
echo "123456" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

cat << 'EOF' > ~/.vnc/xstartup
#!/bin/sh
startxfce4 &
EOF
chmod +x ~/.vnc/xstartup

vncserver -kill :1 2>/dev/null || true
vncserver :1 -geometry 1366x768 -depth 24
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 6080 &

echo "=== Instalando e iniciando Ngrok ==="
wget -q https://bin.equinox.io/c/b5vmRzp7bqB/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
rm ngrok-v3-stable-linux-amd64.tgz

ngrok config add-authtoken $NGROK_TOKEN
ngrok http 6080 > /dev/null &

sleep 3
echo ""
echo "=== LINK DE ACESSO À SUA VM GRÁFICA ==="
curl -s http://localhost:4040/api/tunnels | grep -o 'https://[^"]*' | head -n 1
echo "========================================="
