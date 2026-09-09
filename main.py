import os
import subprocess
import sys

def main():
    print("\n=======================================================")
    print(" INICIANDO AMBIENTE COLAB CLOUD GAMING")
    print("=======================================================\n")

    # Inicia a execução do script de pairing/streaming do repositório
    script_path = "/tmp/colab-gaming/moon-pair.sh"
    
    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
    else:
        print(f"Erro: Script nao encontrado em {script_path}")

if __name__ == "__main__":
    main()
