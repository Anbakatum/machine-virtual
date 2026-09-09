def start_sunshine_and_tunnel():
    print("=== INICIANDO SUNSHINE ===")
    sunshine_bin = shutil.which("sunshine") or "/usr/bin/sunshine" or "/usr/local/bin/sunshine"
    subprocess.run(["sudo", "chmod", "+x", sunshine_bin], check=False)
    
    subprocess.Popen(["sudo", sunshine_bin], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

    print("=== CRIANDO TUNEL PARA O MOONLIGHT ===")
    subprocess.Popen(["ngrok", "tcp", "47989"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Aguarda o processo do ngrok subir a API local
    public_url = None
    import urllib.request
    import json

    for attempt in range(10):
        time.sleep(1)
        try:
            req = urllib.request.urlopen("http://localhost:4040/api/tunnels")
            data = json.loads(req.read().decode())
            tunnels = data.get('tunnels', [])
            if tunnels:
                public_url = tunnels[0]['public_url'].replace("tcp://", "")
                break
        except Exception:
            continue

    if public_url:
        print("\n=======================================================")
        print(f" ENDEREÇO PARA COLOCAR NO MOONLIGHT: {public_url}")
        print("=======================================================\n")
    else:
        print("\n[ERRO] Não foi possível iniciar o túnel do ngrok.")
        print("Certifique-se de que substituiu 'SEU_NGROK_TOKEN_AQUI' no main.py pelo seu token do dashboard do ngrok.\n")
