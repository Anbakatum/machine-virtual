import os
import subprocess
import time

def setup_tailscale(auth_key):
    print("=== INSTALANDO E CONFIGURANDO TAILSCALE ===")
    subprocess.run("curl -fsSL https://tailscale.com/install.sh | sh", shell=True, check=True)
    
    # Inicia o daemon em modo userspace para nao depender de permissoes de kernel do Colab
    subprocess.Popen(["tailscaled", "--tun=userspace-networking"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
    
    if auth_key and auth_key != "tskey-auth-kKzHadsQrc11CNTRL-tajcLJ3dkNJcUJTLSzQkPJ24yVXu8o18Q":
        subprocess.run(f"tailscale up --authkey={auth_key}", shell=True)
    else:
        print("\n[!] Chave do Tailscale nao fornecida. Abra o link abaixo para autorizar:")
        subprocess.run("tailscale up", shell=True)

def setup_sunshine():
    print("=== INSTALANDO DISPLAY VIRTUAL E SUNSHINE ===")
    commands = [
        "sudo apt-get update -y",
        "sudo apt-get install -y xvfb libssl-dev libcurl4-openssl-dev libboost-program-options-dev libgl1-mesa-dev",
        "wget https://github.com/LizardByte/Sunshine/releases/download/v0.21.0/sunshine-ubuntu-22.04-amd64.deb",
        "sudo dpkg -i sunshine-ubuntu-22.04-amd64.deb || sudo apt-get install -f -y",
        "rm -f sunshine-ubuntu-22.04-amd64.deb"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True)

    subprocess.Popen(["Xvfb", ":99", "-screen", "0", "1280x720x24"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def save_connection_info():
    ip_tailscale = subprocess.getoutput("tailscale ip -4").strip()
    
    info_text = f"""=== CONEXÃO MOONLIGHT / SUNSHINE ===
IP para adicionar no Moonlight: {ip_tailscale}
Painel de Configuração do Sunshine: https://{ip_tailscale}:47990
"""
    
    # Salva localmente e no Google Drive
    local_path = "/content/machine-virtual/conexao_moonlight.txt"
    with open(local_path, "w") as f:
        f.write(info_text)

    drive_path = "/content/drive/MyDrive/conexao_moonlight.txt"
    if os.path.exists("/content/drive/MyDrive"):
        with open(drive_path, "w") as f:
            f.write(info_text)
        print(f"[✓] INFORMAÇÕES DE CONEXÃO SALVAS NO GOOGLE DRIVE: {drive_path}")

    print("\n=======================================================")
    print(f" TAILSCALE CONECTADO!")
    print(f" IP PARA O MOONLIGHT: {ip_tailscale}")
    print(f" PAINEL SUNSHINE: https://{ip_tailscale}:47990")
    print("=======================================================\n")

def main():
    # Crie uma Auth Key em: https://login.tailscale.com/admin/settings/keys
    TAILSCALE_AUTH_KEY = "SUA_AUTH_KEY_AQUI"

    setup_tailscale(TAILSCALE_AUTH_KEY)
    setup_sunshine()
    save_connection_info()

    env = os.environ.copy()
    env["DISPLAY"] = ":99"
    subprocess.run("sunshine", shell=True, env=env)

if __name__ == "__main__":
    main()
