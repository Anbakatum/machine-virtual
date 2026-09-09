import os
import time
import subprocess
import shutil

# Cole sua chave do Tailscale aqui dentro das aspas
TAILSCALE_AUTH_KEY = "tskey-auth-kx1rN23Fd111CNTRL-e1TRa8s7zH4aKKnhnHd9J4CwvJG2RRPa"

def setup_tailscale():
    print("\n=== INICIANDO TAILSCALE ===")
    
    # Cria o diretorio do socket
    subprocess.run(["sudo", "mkdir", "-p", "/var/run/tailscale"])
    
    # Inicia o daemon do Tailscale em background
    subprocess.Popen(
        ["sudo", "tailscaled", "--tun=userspace-networking", "--socket=/var/run/tailscale/tailscaled.sock"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(4)

    tailscale_bin = shutil.which("tailscale") or "/usr/bin/tailscale"

    # Autentica via Auth Key
    if "tskey-auth" in TAILSCALE_AUTH_KEY:
        subprocess.run(["sudo", tailscale_bin, "--socket=/var/run/tailscale/tailscaled.sock", "up", "--authkey=" + TAILSCALE_AUTH_KEY])
    else:
        subprocess.run(["sudo", tailscale_bin, "--socket=/var/run/tailscale/tailscaled.sock", "up", "--qr=false"])

    print("\n=======================================================")
    print(" SEU IP DO TAILSCALE:")
    subprocess.run(["sudo", tailscale_bin, "--socket=/var/run/tailscale/tailscaled.sock", "ip", "-4"])
    print("=======================================================\n")

def start_sunshine():
    print("=== INICIANDO SERVIDOR SUNSHINE ===")
    # Sobe o servidor Sunshine no Colab antes do pairing
    subprocess.Popen(["sunshine"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)

def main():
    setup_tailscale()
    start_sunshine()

    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("=======================================================")
    print(" READY! DIGITE O PIN DO MOONLIGHT ABAIXO")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        print("Digite o PIN gerado pelo Moonlight no seu PC/celular:")
        pin = input("Enter Moonlight PIN: ")
        subprocess.run(["sunshine", "--pair", pin])

if __name__ == "__main__":
    main()
