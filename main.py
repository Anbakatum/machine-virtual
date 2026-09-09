import os
import subprocess

def setup_rdp():
    print("=== INSTALANDO INTERFACE GRÁFICA (XFCE4) E CHROME REMOTE DESKTOP ===")
    
    commands = [
        "sudo apt-get update -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4 desktop-base xfce4-terminal chrome-remote-desktop",
        "sudo apt-get install -y xscreensaver-",
        "sudo bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'"
    ]
    
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

def start_crd():
    print("\n=== PRONTO PARA AUTORIZAR ===")
    auth_code = input("Cole o seu comando 'Debian Linux' copiado do Chrome Remote Desktop e aperte ENTER:\n")
    
    if auth_code.strip():
        subprocess.run(auth_code, shell=True)
        print("\n=======================================================")
        print(" CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
        print(" Acesse https://remotedesktop.google.com/access para conectar.")
        print("=======================================================\n")
    else:
        print("[!] Nenhum comando inserido.")

def main():
    setup_rdp()
    start_crd()

if __name__ == "__main__":
    main()
