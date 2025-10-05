#%%
import pandas as pd
import numpy as np

#%%
data = {
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Preco_Unitario': [10.50, 25.00, 5.75, 11.00, 24.50, 6.00, 10.75, 25.50, 5.50],
    'Quantidade': [10, 5, 20, 12, 6, 18, 15, 4, 22],
    'Custo_Unitario': [8.00, 20.50, 4.00, 8.50, 20.00, 4.25, 8.25, 21.00, 3.75]
}

df_vendas = pd.DataFrame(data)
df_vendas

#%%
def calcular_valor_total(preco, quantidade):
    return preco * quantidade

#%%
df_vendas['Valor_Total'] = df_vendas.apply(
    lambda row: calcular_valor_total(row['Preco_Unitario'], row['Quantidade']),
    axis=1
)

#%%
df_vendas

#%%
def categorizar_preco(preco):
  if preco > 20.00:
    return 'Caro'
  elif 10.00 <= preco <= 20.00:
    return 'Médio'
  else:
    return 'Barato'

#%%
df_vendas['Categoria_Preco'] = df_vendas['Preco_Unitario'].apply(categorizar_preco)

#%%
df_vendas