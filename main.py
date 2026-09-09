import os
import time
import subprocess
import shutil
import re

def start_sunshine():
    print("=== INICIANDO SERVIDOR SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    # Inicia o Sunshine com sudo
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

def start_tunnel():
    print("\n=== CRIANDO TÚNEL PÚBLICO AUTOMÁTICO (PINGGY) ===")
    
    # Usa o Pinggy via SSH para expor a porta TCP do Sunshine (47989)
    # Nao exige token nem cadastro
    cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ServerAliveInterval=30", "-R", "0:localhost:47989", "a.pinggy.io"]
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    
    public_address = None
    start_time = time.time()
    
    # Le o output em tempo real para capturar o IP:Porta gerado
    while time.time() - start_time < 20:
        line = process.stdout.readline()
        if not line:
            break
        
        # Procura por padroes como tcp://tcp.pinggy.link:XXXXX ou a.pinggy.io:XXXXX
        match = re.search(r'(tcp://[^\s]+|https?://[^\s]+|[a-zA-Z0-9.-]+\.pinggy\.link:\d+|a\.pinggy\.io:\d+)', line)
        if match:
            found = match.group(0).replace("tcp://", "").replace("https://", "").replace("http://", "")
            if ":" in found:
                public_address = found
                break

    if public_address:
        print("\n=======================================================")
        print(f" ENDEREÇO PARA COLOCAR NO MOONLIGHT: {public_address}")
        print("=======================================================\n")
    else:
        print("\n=== TENTANDO TÚNEL DE BACKUP (SER VEO) ===")
        # Se Pinggy falhar, tenta o Serveo como alternativa
        cmd_backup = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "0:localhost:47989", "serveo.net"]
        process_backup = subprocess.Popen(cmd_backup, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        time.sleep(5)
        print("Conectado via Serveo. Tente o IP do Colab ou reconecte.\n")

def main():
    start_sunshine()
    start_tunnel()

    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("=======================================================")
    print(" READY! DIGITE O PIN DO MOONLIGHT ABAIXO")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        pin = input("Enter Moonlight PIN: ")
        sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine"
        subprocess.run(["sudo", sunshine_bin, "--pair", pin])

if __name__ == "__main__":
    main()
