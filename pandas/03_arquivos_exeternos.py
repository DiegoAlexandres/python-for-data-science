
#%%
import pandas as pd

df_contas_receber = pd.read_excel("../dados/fContasReceber.xlsx") # df_clientes = pd.read_excel('base_de_dados.xlsx', sheet_name='dClientes')
df_clientes = pd.read_excel("../dados/dClientes.xlsx")

#%%
# Ele junta as duas tabelas usando a coluna 'CodCliente' como elo de ligação.
df_relatorio = pd.merge(
    df_contas_receber,
    df_clientes,
    on='CodCliente', # Coluna em comum para o cruzamento
    how="left" # Mantém tudo de contas a receber e traz as infos de clientes
)

df_relatorio

#%%
# Convertendo o tipo das colunas de datas para datetime
colunas = ['DataCompetencia', 'DataVencimento', 'DataPagamento']

for coluna in colunas:
  df_contas_receber[coluna] = pd.to_datetime(df_contas_receber[coluna], errors='coerce')

df_contas_receber.head()


#%%
# --- ETAPA 3: Calcular o resumo por cliente ---
# O 'groupby' agrupa todas as linhas pelo nome do cliente e o '.sum()' soma os valores.
df_resumo = df_relatorio.groupby('Cliente/Fornecedor')['Valor'].sum().reset_index()

#%%
# Renomeia as colunas para clareza
df_resumo.rename(columns={'Cliente/Fornecedor': 'Nome Cliente', 'Valor': 'Valor Total Recebido'}, inplace=True)
# inplace=True significa: "Modifique o DataFrame original diretamente no lugar onde ele está,
# em vez de criar e me devolver uma cópia modificada."
# Por padrão, a maioria das funções do Pandas opera com inplace=False.
# inplace=False e como salvar um arquico como Salvar Como

#%%
# --- ETAPA 4: Salvar os resultados em um novo arquivo Excel ---
# Usamos o ExcelWriter para salvar múltiplos DataFrames em múltiplas abas
with pd.ExcelWriter('relatorio_final_pandas.xlsx') as writer:
    df_relatorio.to_excel(writer, sheet_name='Contas a Receber com Nomes', index=False)
    df_resumo.to_excel(writer, sheet_name='Resumo por Cliente', index=False)

print("Relatório 'relatorio_final_pandas.xlsx' gerado com sucesso usando Pandas!")