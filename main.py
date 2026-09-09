import os
import subprocess

def setup_rdp():
    print("=== INSTALANDO AMBIENTE GRÁFICO (XFCE4) E CHROME REMOTE DESKTOP ===")
    
    commands = [
        "sudo apt-get update -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4 desktop-base xfce4-terminal chrome-remote-desktop",
        "sudo apt-get install -y xscreensaver-",
        "sudo bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'"
    ]
    
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

def start_crd():
    print("\n=== EXECUTANDO COMANDO DE AUTORIZAÇÃO ===")
    auth_code = input("Cole o comando do Chrome Remote Desktop aqui e aperte ENTER:\n")
    
    if auth_code.strip():
        subprocess.run(auth_code, shell=True)
        print("\n=======================================================")
        print(" CONFIGURAÇÃO CONCLUÍDA!")
        print(" Acesse: https://remotedesktop.google.com/access")
        print("=======================================================\n")
    else:
        print("[!] Comando inválido. Execute o script novamente.")

def main():
    setup_rdp()
    start_crd()

if __name__ == "__main__":
    main()
