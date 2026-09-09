import os
import subprocess
import sys

def mount_google_drive():
    """Monta o Google Drive no caminho padrão /content/drive"""
    print("\n=== MONTAGEM DO GOOGLE DRIVE ===")
    try:
        from google.colab import drive
        drive.mount('/content/drive')
        print("✔ Google Drive montado com sucesso em /content/drive!\n")
    except ImportError:
        print("⚠ Executando fora do ambiente Colab ou módulo google.colab indisponível.")
    except Exception as e:
        print(f"✖ Erro ao montar o Google Drive: {e}\n")

def main():
    # 1. Monta o Google Drive
    mount_google_drive()

    # 2. Caminho do script clonado via Makefile
    script_path = "/tmp/colab-gaming/moon-pair.sh"

    print("=======================================================")
    print(" INICIANDO AMBIENTE COLAB CLOUD GAMING")
    print("=======================================================\n")

    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        print(f"Erro: Script nao encontrado em {script_path}")

if __name__ == "__main__":
    main()
