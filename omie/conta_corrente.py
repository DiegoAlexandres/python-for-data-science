import requests
import json

# Suas credenciais da API Omie (substitua pelos seus valores)
APP_KEY = 'SEU_APP_KEY'
APP_SECRET = 'SEU_APP_SECRET'

# 1. Defina a URL do endpoint da API
# Consulte a documentação para encontrar o endpoint correto para cada funcionalidade.
# Exemplo para listar contas correntes:
url_endpoint = 'https://app.omie.com.br/api/v1/geral/contacorrente/'

# 2. Monte o corpo (payload) da requisição em um dicionário Python
# A ação desejada é definida no parâmetro "call".
payload = {
    "call": "ListarContasCorrentes",
    "app_key": APP_KEY,
    "app_secret": APP_SECRET,
    "param": [
        {
            # Parâmetros para a chamada "ListarContasCorrentes"
            # Neste caso, queremos a primeira página, com 50 registros por página.
            "pagina": 1,
            "registros_por_pagina": 50
        }
    ]
}

# 3. Defina os cabeçalhos da requisição
headers = {
    'Content-Type': 'application/json'
}

# 4. Faça a requisição POST usando a biblioteca requests
try:
    response = requests.post(
        url_endpoint,
        data=json.dumps(payload), # Converte o dicionário Python para uma string JSON
        headers=headers
    )

    # 5. Verifique se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        print("Requisição bem-sucedida!")

        # Converte a resposta JSON para um dicionário Python para fácil manipulação
        dados_resposta = response.json()

        # Imprime a resposta formatada
        print("\nResposta da API:")
        print(json.dumps(dados_resposta, indent=4, ensure_ascii=False))

    else:
        print(f"Erro na requisição: Código {response.status_code}")
        print("Resposta:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro ao fazer a requisição: {e}")