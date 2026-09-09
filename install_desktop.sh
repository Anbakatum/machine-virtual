#!/bin/bash
set -e

echo "=== 1. Atualizando e instalando pacotes base ==="
sudo apt-get update -y
sudo apt-get install -y xfce4 xfce4-terminal desktop-base dbus-x11 tigervnc-standalone-server novnc tmate wget curl htop

echo "=== 2. Configurando o Servidor Gráfico VNC ==="
mkdir -p ~/.vnc
echo "123456" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

cat << 'EOF' > ~/.vnc/xstartup
#!/bin/sh
xrdb $HOME/.Xresources
startxfce4 &
EOF
chmod +x ~/.vnc/xstartup

echo "=== 3. Instalando o Google Chrome ==="
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb
sudo apt-get install -y /tmp/chrome.deb
rm /tmp/chrome.deb

echo "=== 4. Instalando a Steam ==="
sudo dpkg --add-architecture i386 || true
sudo apt-get update -y
sudo apt-get install -y steam || true

echo "=== 5. Iniciando os Servidores de Tela ==="
vncserver -kill :1 2>/dev/null || true
vncserver :1 -geometry 1280x720 -depth 24
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 6080 &

echo "=== 6. Gerando Link de Acesso Remoto ==="
tmate -S /tmp/tmate.sock new-session -d
tmate -S /tmp/tmate.sock wait tmate-ready

echo ""
echo "=========================================================="
echo " VM PRONTA! ACESSE SUA ÁREA DE TRABALHO ABAIXO:"
echo "=========================================================="
echo ""
URL=$(tmate -S /tmp/tmate.sock display -p '#{tmate_web}')
echo "Link do terminal tmate: $URL"
echo ""
echo "Para ver a TELA (interface gráfica), use a porta 6080 via tmate ou use um túnel."
echo "=========================================================="
