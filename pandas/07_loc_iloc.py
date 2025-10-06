#%%
import pandas as pd

# Dicionário com os dados de exemplo
# dados = {
#     'Data': pd.to_datetime(['2025-10-01', '2025-10-01', '2025-10-02', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-04', '2025-10-05', '2025-10-05', '2025-10-06']),
#     'Vendedor': ['Ana', 'Carlos', 'Maria', 'Carlos', 'Ana', 'João', 'Maria', 'Ana', 'Carlos', 'João'],
#     'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'SSD 1TB', 'Webcam', 'Mouse', "Webcam", 'Teclado'],
#     'Quantidade': [1, 5, 2, 1, 1, 3, 4, 8, 2, 3],
#     'Preço Unitário': [4500.00, 80.00, 150.00, 950.00, 4600.00, 450.00, 250.00, 85.00, 980.00, 155.00]
# }

dados = {
    'Data': ['2025-10-01', '2025-10-01', '2025-10-02', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-04', '2025-10-05', '2025-10-05', '2025-10-06'],
    'Vendedor': ['Ana', 'Carlos', 'Maria', 'Carlos', 'Ana', 'João', 'Maria', 'Ana', 'Carlos', 'João'],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'SSD 1TB', 'Webcam', 'Mouse', "Webcam", 'Teclado'],
    'Quantidade': [1, 5, 2, 1, 1, 3, 4, 8, 2, 3],
    'Preço Unitário': [4500.00, 80.00, 150.00, 950.00, 4600.00, 450.00, 250.00, 85.00, 980.00, 155.00]
}

df = pd.DataFrame(dados)

df['Data'] = pd.to_datetime(df['Data'])

df.info()

#%%
# Salvando em um arquivo Excel
df.to_excel('vendas_loja.xlsx', index=False)

#%%
df
#%%
# A primeira linha está na posição 0
primeira_linha = df.iloc[0]

type(primeira_linha)

#%%
# Linha de índice 3, coluna de índice 1
valor_especifico = df.iloc[3, 1]
valor_especifico

#%%
# Pega as linhas de índice 2, 3 e 4. O 5 não é incluído.
intervalo_linhas = df.iloc[2:5]
intervalo_linhas