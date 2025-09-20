#%%
import pandas as pd
import requests
import datetime
#%%
# Trabalhando com requests e fazendo uma consulta simples a API
url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json&$select=simbolo,nomeFormatado"

response = requests.get(url)

dados = response.json()['value']

moedas =pd.DataFrame(dados)

moedas = moedas.rename(columns={
    'nomeFormatado': 'MoedaNome',
    'simbolo': 'Moeda'
})

moedas = moedas['Moeda'].unique()
moedas
#%%
# Trabalhando com requests e fazendo uma consulta API
data_inicial = "09-15-2025"
data_final = datetime.date.today().strftime("%m-%d-%Y")
top = 100

todos_os_dados = []

for moeda in moedas:

  skip = 0

  while True:
    url = (
        f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        f"CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?"
        f"@moeda='{moeda}'&@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'"
        f"&$top={top}&$skip={skip}&$filter=tipoBoletim%20eq%20'Fechamento'&$format=json&$select=cotacaoCompra,dataHoraCotacao"
    )

    response = requests.get(url)
    dados = response.json()['value']

    if not dados:
      break

    for registro in dados:
      registro['moeda'] = moeda

    todos_os_dados.extend(dados)
    skip += top

df_cotacoes = pd.DataFrame(todos_os_dados)
df_cotacoes

#%%
# Renomeando as colunas
df_formatado = df_cotacoes.rename(columns={
    'cotacaoCompra' : 'Cotacao',
    'dataHoraCotacao': 'Data',
    'moeda': 'Moeda'
    })

df_formatado

#%%
# Formatando as datas
df_formatado['Data'] = pd.to_datetime(df_formatado['Data'])
df_formatado['Data'] = df_formatado['Data'].dt.strftime('%d/%m/%Y')
df_formatado

#%%
# Analisando os dados da moeda AUD
df_aud = df_formatado[df_formatado['Moeda'] == 'AUD']
df_aud

#%%
# Pega todas as cotações do dia 08 de setembro de 2025
cotacoes_hoje = df_formatado[df_formatado['Data'] == '15/09/2025']
cotacoes_hoje

#%%
# Filtra cotações maiores que 5.40 E menores que 5.45
cotacoes_intervalo = df_formatado[(df_formatado['Cotacao'] > 5.30) & (df_formatado['Cotacao'] < 5.45)]
cotacoes_intervalo

#%%
# Filtro utilizando query
df_formatado.query("Cotacao > 5.20 and Cotacao < 5.45")
