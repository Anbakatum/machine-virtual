import os
import subprocess
import time

def install_wireguard_and_tools():
    print("=== INSTALANDO WIREGUARD, NGROK E DEPENDÊNCIAS ===")
    commands = [
        "sudo apt-get update -y",
        "sudo apt-get install -y wireguard qrencode xvfb libssl-dev libcurl4-openssl-dev libboost-program-options-dev libgl1-mesa-dev",
        "curl -s https://bin.equinox.io/c/bNyA16AP2g/ngrok-v3-stable-linux-amd64.tgz | tar -xz -C /usr/local/bin"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True)

def setup_wireguard(ngrok_authtoken):
    print("=== CONFIGURANDO INTERFACE WIREGUARD ===")
    
    # Gerar chaves do Servidor (Colab)
    server_private_key = subprocess.getoutput("wg genkey").strip()
    server_public_key = subprocess.getoutput(f"echo '{server_private_key}' | wg pubkey").strip()
    
    # Gerar chaves do Cliente (Seu PC/Celular)
    client_private_key = subprocess.getoutput("wg genkey").strip()
    client_public_key = subprocess.getoutput(f"echo '{client_private_key}' | wg pubkey").strip()
    
    # Criar wg0.conf do Servidor
    server_conf = f"""[Interface]
PrivateKey = {server_private_key}
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = {client_public_key}
AllowedIPs = 10.0.0.2/32
"""
    with open("/etc/wireguard/wg0.conf", "w") as f:
        f.write(server_conf)

    # Subir interface WireGuard
    subprocess.run("wg-quick up wg0", shell=True)

    # Autenticar e abrir túnel UDP no Ngrok
    subprocess.run(f"ngrok config add-authtoken {ngrok_authtoken}", shell=True)
    subprocess.Popen(["ngrok", "udp", "51820"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

    # Obter IP/Porta pública do Ngrok
    try:
        import urllib.request, json
        data = json.loads(urllib.request.urlopen("http://localhost:4040/api/tunnels").read())
        public_url = data['tunnels'][0]['public_url'].replace("udp://", "")
    except Exception:
        public_url = "SEU_ENDPOINT_NGROK:PORTA"

    # Criar arquivo .conf para o Cliente
    client_conf = f"""[Interface]
PrivateKey = {client_private_key}
Address = 10.0.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = {server_public_key}
Endpoint = {public_url}
AllowedIPs = 10.0.0.0/24
PersistentKeepalive = 25
"""
    
    # Salva o arquivo na pasta do projeto e no Google Drive (se montado)
    conf_path = "/content/machine-virtual/wireguard_moonlight.conf"
    with open(conf_path, "w") as f:
        f.write(client_conf)

    if os.path.exists("/content/drive/MyDrive"):
        with open("/content/drive/MyDrive/wireguard_moonlight.conf", "w") as f:
            f.write(client_conf)

    print("\n=======================================================")
    print(" ARCHIVO DE CONFIGURAÇÃO GERADO COM SUCESSO!")
    print(f" Caminho do arquivo: {conf_path}")
    print(" IP PARA USAR NO MOONLIGHT APÓS CONECTAR: 10.0.0.1")
    print("=======================================================\n")

def setup_sunshine():
    print("=== INSTALANDO E INICIANDO SUNSHINE ===")
    commands = [
        "wget https://github.com/LizardByte/Sunshine/releases/download/v0.21.0/sunshine-ubuntu-22.04-amd64.deb",
        "sudo dpkg -i sunshine-ubuntu-22.04-amd64.deb || sudo apt-get install -f -y",
        "rm -f sunshine-ubuntu-22.04-amd64.deb"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True)

    subprocess.Popen(["Xvfb", ":99", "-screen", "0", "1280x720x24"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    # COLE SEU AUTHTOKEN DO NGROK AQUI (Crie gratis em ngrok.com):
    NGROK_TOKEN = "3J3AWUbpO8jfj8vfW3KpQgbsVhd_44stQ17sQEKNhxicZmDER"

    install_wireguard_and_tools()
    setup_wireguard(NGROK_TOKEN)
    setup_sunshine()

    env = os.environ.copy()
    env["DISPLAY"] = ":99"
    subprocess.run("sunshine", shell=True, env=env)

if __name__ == "__main__":
    main()
