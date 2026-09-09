import os
import time
import subprocess
import shutil

def setup_tailscale():
    print("\n=== INICIANDO TAILSCALE ===")
    
    # 1. Inicia o tailscaled em segundo plano (&) para não travar o terminal com logs
    subprocess.Popen(
        ["sudo", "tailscaled", "--tun=userspace-networking", "--socks5-server=localhost:1055"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3) # Aguarda o daemon subir

    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale" or "/usr/sbin/tailscale"

    print("\n=======================================================")
    print(" ACESSE O LINK ABAIXO PARA CONECTAR AO SEU TAILSCALE:")
    print("=======================================================\n")
    
    # 2. Executa o comando de login
    subprocess.run(["sudo", tailscale_bin, "up", "--qr=false"])

def main():
    # 1. Configura e conecta o Tailscale
    setup_tailscale()

    # 2. Inicia o script do Sunshine / Moon-pair
    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("\n=======================================================")
    print(" INICIANDO SUNSHINE / MOONLIGHT PAIRING")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        print(f"Erro: Script nao encontrado em {script_path}")

if __name__ == "__main__":
    main()
