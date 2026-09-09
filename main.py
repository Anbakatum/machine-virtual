import os
import time
import subprocess
import shutil
import re

def start_sunshine():
    print("=== INICIANDO SERVIDOR SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    # Inicia o Sunshine com privilégios sudo
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

def start_tunnel():
    print("\n=== CRIANDO TÚNEL PÚBLICO AUTOMÁTICO (PINGGY) ===")
    
    # Comando com parâmetros para ignorar checagem de chave SSH do host
    cmd = [
        "ssh", 
        "-o", "StrictHostKeyChecking=no", 
        "-o", "UserKnownHostsFile=/dev/null", 
        "-o", "ServerAliveInterval=30", 
        "-p", "443", 
        "-R", "0:localhost:47989", 
        "a.pinggy.io"
    ]
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    
    public_address = None
    start_time = time.time()
    
    # Faz a leitura do output em tempo real
    while time.time() - start_time < 25:
        line = process.stdout.readline()
        if not line:
            break
        
        # Procura qualquer padrao de URL emitido pelo Pinggy
        match = re.search(r'([a-zA-Z0-9.-]+\.pinggy\.link:\d+|a\.pinggy\.io:\d+|free\.pinggy\.link:\d+)', line)
        if match:
            public_address = match.group(0)
            break

    if public_address:
        print("\n=======================================================")
        print(f" ENDEREÇO PARA COLOCAR NO MOONLIGHT: {public_address}")
        print("=======================================================\n")
    else:
        print("\n=== TENTANDO TÚNEL ALTERNATIVO (SER VEO) ===")
        cmd_backup = [
            "ssh", 
            "-o", "StrictHostKeyChecking=no", 
            "-o", "UserKnownHostsFile=/dev/null", 
            "-R", "47989:localhost:47989", 
            "serveo.net"
        ]
        process_backup = subprocess.Popen(cmd_backup, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        start_time_b = time.time()
        while time.time() - start_time_b < 15:
            line_b = process_backup.stdout.readline()
            if not line_b:
                break
            match_b = re.search(r'Forwarding SSH traffic from ([^\s]+)', line_b)
            if match_b:
                print("\n=======================================================")
                print(f" ENDEREÇO SERVEO: serveo.net:47989")
                print("=======================================================\n")
                break

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
