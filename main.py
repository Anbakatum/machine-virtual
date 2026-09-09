import os
import time
import subprocess
import shutil

def install_and_start_tailscale():
    print("\n=== INSTALANDO TAILSCALE ===")
    if not shutil.which("tailscale"):
        subprocess.run("curl -fsSL https://tailscale.com/install.sh | sh", shell=True, check=True)

    print("\n=== INICIANDO SERVIÇO DO TAILSCALE ===")
    subprocess.Popen(["sudo", "tailscaled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

    print("\n=== FAÇA LOGIN NO TAILSCALE ===")
    print("Acesse o link abaixo no seu navegador para autorizar a máquina do Colab:\n")
    
    # Executa o login e exibe a URL no terminal
    process = subprocess.Popen(["sudo", "tailscale", "up"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
        if "https://tailscale.com/a/" in line or "Success" in line:
            break

def start_sunshine():
    print("=== INICIANDO SERVIDOR SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

def main():
    start_sunshine()
    install_and_start_tailscale()

    print("\n=======================================================")
    print(" PASSO 1: Abra o link do Tailscale exibido acima e faça login")
    print(" PASSO 2: Baixe/abra o aplicativo Tailscale no seu PC/Celular")
    print(" PASSO 3: Copie o IP 100.x.x.x gerado no app do Tailscale e adicione no Moonlight")
    print("=======================================================\n")

    script_path = "/tmp/colab-gaming/moon-pair.sh"

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        pin = input("Enter Moonlight PIN: ")
        sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine"
        subprocess.run(["sudo", sunshine_bin, "--pair", pin])

if __name__ == "__main__":
    main()
