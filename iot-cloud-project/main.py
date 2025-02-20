import time
import random
import firebase_admin
from firebase_admin import credentials, db

# Inicialização do Firebase
cred = credentials.Certificate("caminho/para/seu/firebase/credencial.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seu-projeto.firebaseio.com/'
})

# Simulação de sensores
def coletar_dados():
    return {
        "temperatura": round(random.uniform(18, 35), 2),
        "umidade": round(random.uniform(40, 90), 2),
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }

# Enviar dados para o Firebase
def enviar_dados():
    ref = db.reference('sensores')
    while True:
        dados = coletar_dados()
        ref.push(dados)
        print(f"Dados enviados: {dados}")
        time.sleep(10)  # Enviar a cada 10 segundos

if __name__ == "__main__":
    enviar_dados()