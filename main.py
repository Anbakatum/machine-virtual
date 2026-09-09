import os
import time
import subprocess
import shutil

# Insira seu Authtoken do ngrok entre as aspas
NGROK_AUTH_TOKEN = "3J3AWUbpO8jfj8vfW3KpQgbsVhd_44stQ17sQEKNhxicZmDER"

def install_and_setup_ngrok():
    print("\n=== CONFIGURANDO NGROK ===")
    if not shutil.which("ngrok"):
        # Instala o ngrok via repositorio oficial de pacotes (APT)
        subprocess.run(["curl", "-s", "https://ngrok-agent.s3.amazonaws.com/ngrok.asc"], stdout=open("/etc/apt/trusted.gpg.d/ngrok.asc", "wb"), check=True)
        subprocess.run(["echo", "deb https://ngrok-agent.s3.amazonaws.com buster main"], stdout=open("/etc/apt/sources.list.d/ngrok.list", "w"), check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "ngrok", "-y"], check=True)
    
    subprocess.run(["ngrok", "config", "add-authtoken", NGROK_AUTH_TOKEN], check=True)

def start_sunshine_and_tunnel():
    print("=== INICIANDO SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

    print("=== CRIANDO TUNEL PARA O MOONLIGHT ===")
    # Expõe a porta principal do Sunshine (47989 TCP/UDP)
    subprocess.Popen(["ngrok", "tcp", "47989"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

    # Captura o IP e a Porta gerados pelo ngrok
    try:
        import urllib.request
        import json
        req = urllib.request.urlopen("http://localhost:4040/api/tunnels")
        data = json.loads(req.read().decode())
        public_url = data['tunnels'][0]['public_url'].replace("tcp://", "")
        
        print("\n=======================================================")
        print(f" ENDEREÇO PARA COLOCAR NO MOONLIGHT: {public_url}")
        print("=======================================================\n")
    except Exception as e:
        print("Erro ao obter URL do ngrok. Verifique se o token é válido.")

def main():
    install_and_setup_ngrok()
    start_sunshine_and_tunnel()

    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("=======================================================")
    print(" DIGITE O PIN DO MOONLIGHT ABAIXO")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        pin = input("Enter Moonlight PIN: ")
        sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine"
        subprocess.run(["sudo", sunshine_bin, "--pair", pin])

if __name__ == "__main__":
    main()
