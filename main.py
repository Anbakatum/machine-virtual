import os
import time
import subprocess
import shutil

def setup_tailscale():
    print("\n=== INICIANDO TAILSCALE ===")
    
    # Inicia o daemon se nao estiver rodando
    subprocess.Popen(
        ["sudo", "tailscaled", "--tun=userspace-networking", "--socks5-server=localhost:1055"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)

    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale" or "/usr/sbin/tailscale"

    # Conecta ao Tailscale
    subprocess.run(["sudo", tailscale_bin, "up", "--qr=false"])

    print("\n=======================================================")
    print(" SEU IP DO TAILSCALE:")
    # Mostra o IP gerado para usar no Moonlight
    subprocess.run(["sudo", tailscale_bin, "ip", "-4"])
    print("=======================================================\n")

def main():
    # 1. Configura e exibe o IP do Tailscale
    setup_tailscale()

    # 2. Inicia o script do Sunshine / Moon-pair
    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("=======================================================")
    print(" INICIANDO SUNSHINE / MOONLIGHT PAIRING")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        print(f"Erro: Script nao encontrado em {script_path}")

if __name__ == "__main__":
    main()
