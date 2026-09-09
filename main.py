import os
import shutil
import subprocess
import sys

def main():
    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale" or "/usr/sbin/tailscale"
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine"

    print("\n=======================================================")
    print(" ACESSE O LINK ABAIXO PARA CONECTAR AO SEU TAILSCALE:")
    print("=======================================================\n")
    
    # Autenticação Tailscale
    subprocess.run(["sudo", tailscale_bin, "--socket=/var/run/tailscale/tailscaled.sock", "up", "--qr=false"])

    print("\n=== INICIANDO SUNSHINE (SERVIDOR MOONLIGHT) ===")
    os.environ["DISPLAY"] = ":0"
    
    if os.path.exists(sunshine_bin):
        # Flag necessária para AppImages rodarem dentro do docker/Colab
        subprocess.run([sunshine_bin, "--appimage-extract-and-run"])
    else:
        print(f"Erro: Sunshine nao encontrado em {sunshine_bin}")

if __name__ == "__main__":
    main()
