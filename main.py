import os
import time
import subprocess
import shutil

def setup_tailscale():
    print("\n=== INICIANDO TAILSCALE ===")
    
    # Cria o diretorio do socket se nao existir
    subprocess.run(["sudo", "mkdir", "-p", "/var/run/tailscale"])
    
    # Inicia o daemon apontando explicitamente o socket e em userspace mode
    subprocess.Popen(
        ["sudo", "tailscaled", "--tun=userspace-networking", "--socket=/var/run/tailscale/tailscaled.sock"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Aguarda o socket ser criado no sistema
    time.sleep(5)

    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale" or "/usr/sbin/tailscale"

    # Conecta o Tailscale
    subprocess.run(["sudo", tailscale_bin, "--socket=/var/run/tailscale/tailscaled.sock", "up", "--qr=false"])

    print("\n=======================================================")
    print(" SEU IP DO TAILSCALE:")
    subprocess.run(["sudo", tailscale_bin, "--socket=/var/run/tailscale/tailscaled.sock", "ip", "-4"])
    print("=======================================================\n")

def main():
    # 1. Configura e inicia o Tailscale
    setup_tailscale()

    # 2. Executa o script de streaming/pairing
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
