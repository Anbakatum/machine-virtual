import os
import subprocess

def setup_rdp():
    print("=== INSTALANDO INTERFACE GRÁFICA (XFCE4) E DEPENDÊNCIAS ===")
    
    commands = [
        "sudo apt-get update -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y xfce4 desktop-base xfce4-terminal xscreensaver-",
        # Baixa o pacote oficial do Chrome Remote Desktop da Google
        "wget -q https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb",
        # Instala o pacote baixado resolvendo dependências automaticamente
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ./chrome-remote-desktop_current_amd64.deb",
        "rm -f chrome-remote-desktop_current_amd64.deb",
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
