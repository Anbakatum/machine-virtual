import os
import shutil
import subprocess
import sys

def main():
    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale" or "/usr/sbin/tailscale"
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"

    print("\n=======================================================")
    print(" ACESSE O LINK ABAIXO PARA CONECTAR AO SEU TAILSCALE:")
    print("=======================================================\n")
    
    # Executa a autenticação interativa do Tailscale
    subprocess.run(["sudo", tailscale_bin, "up", "--qr=false"])

    print("\n=== INICIANDO SUNSHINE (SERVIDOR MOONLIGHT) ===")
    os.environ["DISPLAY"] = ":0"
    
    if os.path.exists(sunshine_bin):
        subprocess.run([sunshine_bin])
    else:
        print(f"Erro: Sunshine nao encontrado em {sunshine_bin}")

if __name__ == "__main__":
    main()
