#%%
import pandas as pd
import requests

#%%
# Importação da variavel de ambiente
import os
from dotenv import load_dotenv

# Config para ler a variaval de ambiente
load_dotenv()
token = os.getenv("token_api")

#%%
# Criando a primeira consulta
url_category = "https://myfin-financial-management.bubbleapps.io/api/1.1/obj/category/"

header = {
    "Authorization" : f"Bearer {token}"
}

response = requests.get(url_category, headers=header)

response_category = response.json()["response"]["results"]

df = pd.DataFrame(response_category, columns=["title", "_id"])

df.to_excel("Consulta_Categorias_sem_indece.xlsx", index=False)
#%%
# Fazendo multiplas consultas com função
url_category = "https://myfin-financial-management.bubbleapps.io/api/1.1/obj/category/"
url_recipient = "https://myfin-financial-management.bubbleapps.io/api/1.1/obj/recipient/"
url_transactions = "https://myfin-financial-management.bubbleapps.io/api/1.1/obj/transactions/?cursor=0"

header = {
    "Authorization" : f"Bearer {token}"
}

#%%
def chamar_api_xfinance(url):
    response = requests.get(url, headers=header)
    return response

#%%
response_category = chamar_api_xfinance(url_category)
response_recipient = chamar_api_xfinance(url_recipient)
response_transactions = chamar_api_xfinance(url_transactions)

#%%
# Navegando no Json da API
category = response_category.json()["response"]["results"]
recipient = response_recipient.json()["response"]["results"]
transactions = response_transactions.json()["response"]["results"]

#%%
# Criando um DataFrame de todas as colunas
df_category = pd.DataFrame(category)
df_recipient = pd.DataFrame(recipient)
df_transactions = pd.DataFrame(transactions)

#%%
# Criando um DataFrame com colunas selecionadas 
df_category = pd.DataFrame(category, columns=["title", "_id"])
df_recipient = pd.DataFrame(recipient, columns=["title", "_id", "category_ref"])
df_transactions = pd.DataFrame(transactions)

#%%
# Salvando em Excel
df_category.to_excel("Category.xlsx", index=False)
df_recipient.to_excel("Recipient.xlsx", index=False)

#%%
# Salando em parquet / Instale a biblioteca pyarrow / pip install pyarrow
df_category.to_parquet("Category.parquet", index=False)
df_recipient.to_parquet("Recipient.parquet", index=False)
