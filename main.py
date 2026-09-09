import os
import time
import subprocess
import shutil
import json
import urllib.request

def install_and_start_playit():
    print("\n=== CONFIGURANDO PLAYIT.GG ===")
    
    # Baixa o executavel do playit se nao existir
    if not os.path.exists("/usr/local/bin/playit"):
        subprocess.run(
            ["wget", "-O", "/usr/local/bin/playit", "https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64"],
            check=True
        )
        subprocess.run(["chmod", "+x", "/usr/local/bin/playit"], check=True)

    print("=== INICIANDO TUNEL PLAYIT ===")
    # Inicia o playit em segundo plano
    subprocess.Popen(["/usr/local/bin/playit"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

def start_sunshine():
    print("=== INICIANDO SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)

def main():
    start_sunshine()
    install_and_start_playit()

    print("\n=======================================================")
    print(" PASSO 1: Abra o link gerado pelo Playit para vincular")
    print(" PASSO 2: Crie um agente/tunnel apontando para o IP 127.0.0.1")
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
