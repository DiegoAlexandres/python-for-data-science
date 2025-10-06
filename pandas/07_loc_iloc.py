#%%
import pandas as pd

#%%
dados = {
    'Data': pd.to_datetime(['2025-10-01', '2025-10-01', '2025-10-02', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-04', '2025-10-05', '2025-10-05', '2025-10-06']),
    'Vendedor': ['Ana', 'Carlos', 'Maria', 'Carlos', 'Ana', 'João', 'Maria', 'Ana', 'Carlos', 'João'],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'SSD 1TB', 'Webcam', 'Mouse', "Webcam", 'Teclado'],
    'Quantidade': [1, 5, 2, 1, 1, 3, 4, 8, 2, 3],
    'Preço Unitário': [4500.00, 80.00, 150.00, 950.00, 4600.00, 450.00, 250.00, 85.00, 980.00, 155.00]
}

#%%
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

#%%
# iloc linhas
df.iloc[7]

#%%
# iloc colunas
df.iloc[1, 1]

#%%
df.iloc[1:6]

# start 1 : 5 end

#%%
df.iloc[1:6, 0:2]


#%%
df.iloc[5, 2]
# iloc = indice posição

#%%
df

#%%
mouse = df.groupby("Vendedor")["Preço Unitário"].sum()
mouse

#%%
df

#%%
df.loc[0, "Vendedor"]

#%%

indice = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

df_2 = pd.DataFrame(dados, index=indice)
df_2

#%%
df_2.loc["H", "Vendedor"]

#%%
df_2.loc["C": "H"]

#%%
df_2.loc["A", "Produto"]

#%%
df_2.loc["D":, ["Produto", "Preço Unitário"]]

### Solução de agrupamento entre produtos e vendedores
#%%
df

#%%
# Solução com filtro
filtro_mouse = df[df["Produto"] == "Mouse"]
filtro_mouse

#%%
qtde_vendedores = filtro_mouse["Vendedor"].nunique()
qtde_vendedores

#%%
# Solução com loc
qtde_vendedores_loc = df.loc[df['Produto'] == 'Mouse', 'Vendedor'].nunique()
qtde_vendedores_loc

#%%
# Solução com groupby
groupby_produto_vendedor = df.groupby('Produto')['Vendedor'].nunique()
groupby_produto_vendedor
#%%
qtde_vendedores_mouse = groupby_produto_vendedor.loc['Mouse']
qtde_vendedores_mouse