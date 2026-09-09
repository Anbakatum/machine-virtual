import os
import time
import subprocess
import shutil
import re

def install_and_start_cloudflared():
    print("\n=== INSTALANDO CLOUDFLARE TUNNEL ===")
    cloudflared_bin = shutil.which("cloudflared") or "/usr/local/bin/cloudflared"
    
    if not os.path.exists(cloudflared_bin):
        subprocess.run([
            "wget", "-q", "-O", "/usr/local/bin/cloudflared",
            "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
        ], check=True)
        subprocess.run(["chmod", "+x", "/usr/local/bin/cloudflared"], check=True)
        cloudflared_bin = "/usr/local/bin/cloudflared"

    print("=== INICIANDO TÚNEL DA CLOUDFLARE ===")
    
    # Inicia o túnel direcionando a porta 47989 do Sunshine
    log_file = open("/tmp/cloudflared.log", "w")
    subprocess.Popen(
        [cloudflared_bin, "tunnel", "--url", "tcp://localhost:47989"],
        stdout=log_file,
        stderr=log_file
    )
    
    public_address = None
    start_time = time.time()
    
    # Aguarda gerar o link no arquivo de log sem travar o Python
    while time.time() - start_time < 15:
        time.sleep(1)
        if os.path.exists("/tmp/cloudflared.log"):
            with open("/tmp/cloudflared.log", "r") as f:
                content = f.read()
                match = re.search(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com', content)
                if match:
                    # Formata o endereço removendo o https://
                    public_address = match.group(0).replace("https://", "")
                    break

    if public_address:
        print("\n=======================================================")
        print(f" ENDEREÇO PARA COLOCAR NO MOONLIGHT: {public_address}")
        print("=======================================================\n")
    else:
        print("\n[!] Verifique os logs de conexão do túnel em /tmp/cloudflared.log\n")

def start_sunshine():
    print("=== INICIANDO SERVIDOR SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

def main():
    start_sunshine()
    install_and_start_cloudflared()

    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("=======================================================")
    print(" READY! DIGITE O PIN DO MOONLIGHT ABAIXO")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        pin = input("Enter Moonlight PIN: ")
        sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine"
        subprocess.run(["sudo", sunshine_bin, "--pair", pin])

if __name__ == "__main__":
    main()
