import os
import subprocess
import time

def setup_tailscale():
    print("=== INSTALANDO E INICIANDO TAILSCALE ===")
    subprocess.run("curl -fsSL https://tailscale.com/install.sh | sh", shell=True, check=True)
    
    # Inicia o daemon do Tailscale em segundo plano (necessario no Colab)
    subprocess.Popen(["tailscaled", "--tun=userspace-networking"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
    
    print("\nIniciando Tailscale... Acesse o link para autenticar:")
    subprocess.run("sudo tailscale up", shell=True)

def setup_display_and_sunshine():
    print("=== CONFIGURANDO AMBIENTE DE TELA E SUNSHINE ===")
    commands = [
        "sudo apt-get update -y",
        "sudo apt-get install -y xvfb x11vnc libssl-dev libcurl4-openssl-dev libboost-program-options-dev libgl1-mesa-dev",
        "wget https://github.com/LizardByte/Sunshine/releases/download/v0.21.0/sunshine-ubuntu-22.04-amd64.deb",
        "sudo dpkg -i sunshine-ubuntu-22.04-amd64.deb || sudo apt-get install -f -y",
        "rm -f sunshine-ubuntu-22.04-amd64.deb"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True)

    # Inicia servidor virtual de exibicao no DISPLAY :99
    print("=== INICIANDO DISPLAY VIRTUAL (Xvfb) ===")
    subprocess.Popen(["Xvfb", ":99", "-screen", "0", "1280x720x24"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.environ["DISPLAY"] = ":99"

def main():
    setup_tailscale()
    setup_display_and_sunshine()
    
    print("\n=======================================================")
    print(" SUNSHINE RODANDO NO DISPLAY :99!")
    print(" Acesse pelo IP do Tailscale na porta 47990 no navegador.")
    print(" Exemplo: https://<IP-DO-TAILSCALE>:47990")
    print("=======================================================\n")
    
    # Executa o Sunshine atrelado ao Display Virtual
    env = os.environ.copy()
    env["DISPLAY"] = ":99"
    subprocess.run("sunshine", shell=True, env=env)

if __name__ == "__main__":
    main()
