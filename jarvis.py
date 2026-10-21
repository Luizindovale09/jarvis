import requests

API_KEY = "AIzaSyAQAb8RN6InDqCcuNS6dxgk3GGOLhef7uEezldFMTSB5ojR3ds8tg"
URL = f"https://googleapis.com{API_KEY}"

print("=-"*20)
print("  JARVIS v1.0 - INICIADO NO MOTO G30  ")
print("=-"*20)
print("Digite 'sair' para encerrar.\n")

while True:
    c = input("Você: ")
    if c.lower() == "sair":
        print("Jarvis: Desativando sistemas. Até logo, senhor.")
        break
    if not c.strip():
        continue
        
    p = {
        "contents": [{
            "parts": [{
                "text": f"Você é o Jarvis do Homem de Ferro. Responda de forma curta, inteligente e prestativa em português, sempre chamando o usuário de senhor. Comando: {c}"
            }]
        }]
    }
    
    try:
        r = requests.post(URL, json=p).json()
        t = r['candidates'][0]['content']['parts'][0]['text']
        print(f"\nJarvis: {t}\n")
    except Exception as e:
        print("\nErro de conexão.")
          
