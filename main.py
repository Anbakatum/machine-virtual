import os
import subprocess
import re

def setup_rdp():
    print("=== INSTALANDO INTERFACE GRÁFICA (XFCE4) E DEPENDÊNCIAS ===")
    commands = [
        "sudo apt-get update -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4 desktop-base xfce4-terminal xscreensaver-",
        "wget -q https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ./chrome-remote-desktop_current_amd64.deb",
        "rm -f chrome-remote-desktop_current_amd64.deb",
        "sudo bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

def start_crd():
    print("\n=== PRONTO PARA AUTORIZAR ===")
    auth_code = input("Cole o seu comando 'Debian Linux' copiado do Chrome Remote Desktop e aperte ENTER:\n").strip()
    
    if auth_code:
        # Garante a passagem do parametro de usuario do sistema para o CRD
        if "--user-name=" not in auth_code:
            auth_code += " --user-name=root"
        
        # Define um PIN fixo automático de 6 digitos para evitar travamentos no terminal
        if "--pin=" not in auth_code:
            auth_code += " --pin=123456"

        print("\n=== INICIANDO O SERVIÇO DO CRD ===")
        subprocess.run(auth_code, shell=True)

        print("\n=======================================================")
        print(" CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
        print(" PIN PADRÃO CONFIGURADO: 123456")
        print(" Acesse https://remotedesktop.google.com/access para conectar.")
        print("=======================================================\n")

        # Mantém a sessão do Colab viva em loop infinito para não encerrar o container
        while True:
            pass
    else:
        print("[!] Nenhum comando inserido.")

def main():
    setup_rdp()
    start_crd()

if __name__ == "__main__":
    main()
