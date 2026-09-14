import os
import subprocess
import time

def setup_drive():
    print("=== MONTA O GOOGLE DRIVE ===")
    from google.colab import drive
    drive.mount('/content/drive')

def setup_tailscale():
    print("=== INSTALANDO TAILSCALE ===")
    subprocess.run("curl -fsSL https://tailscale.com/install.sh | sh", shell=True, check=True)
    print("\nIniciando Tailscale... Acesse o link que aparecer para autenticar:")
    subprocess.run("sudo tailscale up", shell=True)

def setup_sunshine():
    print("=== INSTALANDO SUNSHINE ===")
    commands = [
        "sudo apt-get update -y",
        "sudo apt-get install -y libssl-dev libcurl4-openssl-dev libboost-program-options-dev libgl1-mesa-dev",
        "wget https://github.com/LizardByte/Sunshine/releases/download/v0.21.0/sunshine-ubuntu-22.04-amd64.deb",
        "sudo dpkg -i sunshine-ubuntu-22.04-amd64.deb || sudo apt-get install -f -y",
        "rm -f sunshine-ubuntu-22.04-amd64.deb"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True)

def main():
    setup_drive()
    setup_tailscale()
    setup_sunshine()
    
    print("\n=======================================================")
    print(" SUNSHINE RODANDO!")
    print(" Acesse pelo IP do Tailscale na porta 47990 no navegador.")
    print(" Exemplo: https://<IP-DO-TAILSCALE>:47990")
    print("=======================================================\n")
    
    # Mantém o Sunshine ativo no terminal
    subprocess.run("sunshine", shell=True)

if __name__ == "__main__":
    main()
