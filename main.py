import os
import time
import subprocess
import shutil

def setup_tun():
    """Cria o dispositivo TUN no Colab para o Tailscale funcionar como interface de rede real"""
    print("\n=== CONFIGURANDO INTERFACE TUN ===")
    subprocess.run(["sudo", "mkdir", "-p", "/dev/net"])
    subprocess.run(["sudo", "mknod", "/dev/net/tun", "c", "10", "200"], check=False)
    subprocess.run(["sudo", "chmod", "606", "/dev/net/tun"])

def setup_tailscale():
    setup_tun()
    print("\n=== INICIANDO TAILSCALE ===")
    
    # Inicia o daemon do tailscale em background com permissao para TUN
    subprocess.Popen(
        ["sudo", "tailscaled"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)

    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale" or "/usr/sbin/tailscale"

    # Conecta ao Tailscale
    subprocess.run(["sudo", tailscale_bin, "up", "--qr=false"])

    print("\n=======================================================")
    print(" SEU IP DO TAILSCALE:")
    subprocess.run(["sudo", tailscale_bin, "ip", "-4"])
    print("=======================================================\n")

def main():
    # 1. Configura e conecta o Tailscale com TUN habilitado
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
