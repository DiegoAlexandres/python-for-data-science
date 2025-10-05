#%%
import pandas as pd
import requests
import json

#%%
# Importação da variavel de ambiente
import os
from dotenv import load_dotenv

# Config para ler a variaval de ambiente
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

#%%
BASE_URL = "https://services.contaazul.com/"

endpoint = "contaazul-bff/person-registration/v1/persons"
url_completa = f"{BASE_URL}{endpoint}"

#%%
headers = {
    "X-Authorization": ACCESS_TOKEN,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

params = {
    "page": 1,
    "page_size": 100
}

print(f"Fazendo requisição GET para: {url_completa}")

#%%
try:
    response = requests.get(url_completa, headers=headers, params=params)

    response.raise_for_status()

    dados = response.json()['items']

    print("\n✅ Requisição bem-sucedida!")
    print("--- DADOS RECEBIDOS ---")

    print(json.dumps(dados, indent=4, ensure_ascii=False))

except requests.exceptions.HTTPError as http_err:
    print(f"\n❌ Erro HTTP: {http_err}")
    print(f"Código de Status: {response.status_code}")
    print(f"Resposta do Servidor: {response.text}")
except requests.exceptions.RequestException as err:
    print(f"\n❌ Erro na Requisição: {err}")

#%%
df = pd.DataFrame(dados)
df.head()    

#%%
df_clientes = df.rename(columns={
 "uuid" : "id_cliente",
 "name" : "nome_cliente",
 "profiles" : "tipo"
})

df_clientes

#%%
df_clientes.drop(["document", "email", "phone", "personType", "active", "personLegacyUUID", "personLegacyId"], axis= 1 )