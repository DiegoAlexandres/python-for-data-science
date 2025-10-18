#%%
import pandas as pd

#%%
df = pd.read_excel("../dados/base_denis.xlsx")
df.head()

#%%
#######################################################-----1-----#########################################################

# 1. Transforma a coluna ANOMES para o formato de data (o dia será sempre 01)
df['ANOMES'] = pd.to_datetime(df['ANOMES'], format='%Y%m')
df.head()

#%%
df = df.rename(columns={"ANOMES" : "DATA"})
df.head()

#%%
#######################################################-----2-----#########################################################

# Cria a nova coluna com um valor padrão nulo
df['COD_GRUPO'] = None
df.head()

#%%
# Para cada condição, selecionamos as linhas com .loc e atribuímos o valor correto
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Pessoal', na=False), 'COD_GRUPO'] = '1'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Juros', na=False), 'COD_GRUPO'] = '2'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Outras', na=False), 'COD_GRUPO'] = '3'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Investimentos', na=False), 'COD_GRUPO'] = '4'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Inversoes', na=False), 'COD_GRUPO'] = '5'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Amortizacao', na=False), 'COD_GRUPO'] = '6'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Reserva', na=False), 'COD_GRUPO'] = '9'

df.head()
#%%
#######################################################-----3-----#########################################################

codigo_rpps = [1801261, 2801261, 1800262, 2800262, 1802202, 2802202]

#%%
# 1. Define 'Não' como o valor padrão para a coluna inteira
df['RPPS'] = 'Não'
df.head()
# df["RPPS"].unique()

#%%
# 2. Usa .loc para selecionar as linhas onde a condição é verdadeira e muda o valor para 'Sim'
df.loc[df['COD_FONTE_MAE'].isin(codigo_rpps), 'RPPS'] = 'Sim'

df["RPPS"].unique()
#%%
#######################################################-----4-----#########################################################

# 1. Define '4' como o valor padrão (caso "senão")
df['COD_CATEGORIA'] = 4
df.head()

#%%
# df = df.drop("Cod_Categoria", axis=1)
# df.head()

# codigo_categorias = [1, 2, 3]

#%%
# df.drop("COD_CATEGORIA", axis=1, inplace=True)
# df.head()
#%%
# 2. Usa .loc para atualizar o valor para '3' onde a condição é atendida
df.loc[df['COD_GRUPO'].isin([1, 2, 3]), 'COD_CATEGORIA'] = 3

df.tail()
df["COD_CATEGORIA"].unique()
#%%
#######################################################-----5-----#########################################################

colunas_concatenadas = ['COD_CATEGORIA', 'COD_GRUPO', 'COD_MODALIDADE', 'COD_ELEMENTO']

#%%
for col in colunas_concatenadas:
    df[col] = df[col].astype(str)

#%%
df['COD_NATUREZA_ELEMENTO'] = df[colunas_concatenadas].agg(''.join, axis=1)

df.head()
#%%
#######################################################-----6-----#########################################################

padroes = '^(32|46|99|45..66)|^45909266$|^45909263$|^45..64$|^45909264$|^45..63$'

#%%
# 1. Define 'Sim' como o valor padrão (caso "senão")
df['PRIMARIO'] = 'Sim'

#%%
# 2. Usa .loc para encontrar as linhas que correspondem ao regex e muda o valor para 'Não'
df.loc[df['COD_NATUREZA_ELEMENTO'].str.contains(padroes, na=False), 'PRIMARIO'] = 'Não'

df.head()
df["PRIMARIO"].unique()
#%%
#######################################################-----7-----#########################################################

df['TOTAL_PAGO'] = df['PAGO'] + df['PAGO_EXERCICIO_ANTERIOR']
df.head()

# df[df['TOTAL_PAGO'].notna()] # Faz um filtro e retorna os valores quando a coluna não esta vazia 
# df.head()

#%%
#######################################################-----8-----#########################################################

filtered_df = df[(df['RPPS'] == 'Não') & (df['PRIMARIO'] == 'Sim')].copy()
filtered_df['ano'] = filtered_df['DATA'].dt.year
filtered_df['mes_num'] = filtered_df['DATA'].dt.month
summary = filtered_df.groupby(['ano', 'mes_num'])['TOTAL_PAGO'].sum().reset_index()
pivot_table = summary.pivot_table(index='mes_num', columns='ano', values='TOTAL_PAGO').fillna(0)

if 2024 not in pivot_table.columns: pivot_table[2024] = 0
if 2025 not in pivot_table.columns: pivot_table[2025] = 0

# AJUSTE: Renomeando a coluna de variação para 'Var. R$'
pivot_table['Var. R$'] = pivot_table[2025] - pivot_table[2024]
pivot_table['Var. %'] = (pivot_table['Var. R$'] / pivot_table[2024].replace(0, float('nan'))) * 100
pivot_table = pivot_table.fillna(0)

meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
         7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}
pivot_table.index = pivot_table.index.map(meses)
pivot_table = pivot_table.rename_axis('Mês')

# AJUSTE: Mudança para exibir todos os 12 meses, garantindo a ordem correta
meses_todos = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
final_table = pivot_table.reindex(meses_todos, fill_value=0)

# AJUSTE: Reordenando as colunas para corresponder ao exemplo
final_table = final_table[[2024, 2025, 'Var. %', 'Var. R$']]

# AJUSTE NOVO: Adicionando a linha de "Total"
total_2024 = final_table[2024].sum()
total_2025 = final_table[2025].sum()
total_var_rs = final_table['Var. R$'].sum()
# O percentual total é calculado sobre os totais, não somado
total_var_pct = (total_var_rs / total_2024) * 100 if total_2024 != 0 else 0

final_table.loc['Total'] = [total_2024, total_2025, total_var_pct, total_var_rs]

final_table

# # Filtrar o DataFrame usando uma condição booleana
# filtered_df = df[(df['RPPS'] == 'Não') & (df['Primário'] == 'Sim')].copy()

# filtered_df['ano'] = filtered_df['DATA'].dt.year
# filtered_df['mes_num'] = filtered_df['DATA'].dt.month

# # Usar .groupby() para agregar os dados
# summary = filtered_df.groupby(['ano', 'mes_num'])['Total_Pago'].sum().reset_index()

# # Pivotar a tabela
# pivot_table = summary.pivot_table(index='mes_num', columns='ano', values='Total_Pago').fillna(0)

# if 2024 not in pivot_table.columns: pivot_table[2024] = 0
# if 2025 not in pivot_table.columns: pivot_table[2025] = 0

# # Cálculos de variação (operações padrão do Pandas)
# pivot_table['Var $'] = pivot_table[2025] - pivot_table[2024]
# pivot_table['Var. %'] = (pivot_table['Var $'] / pivot_table[2024].replace(0, float('nan'))) * 100
# pivot_table = pivot_table.fillna(0) # Preenche NaN/inf se houve divisão por zero

# # Formatação final
# meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
#          7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}
# pivot_table.index = pivot_table.index.map(meses)
# pivot_table = pivot_table.rename_axis('Mês')

# todos_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# final_table = pivot_table.reindex(todos_meses, fill_value=0)
# final_table = final_table[[2024, 2025, 'Var. %', 'Var $']]

# total_2024 = final_table[2024].sum()
# total_2025 = final_table[2025].sum()
# total_var_rs = final_table['Var. R$'].sum()
# # O percentual total é calculado sobre os totais, não somado
# total_var_pct = (total_var_rs / total_2024) * 100 if total_2024 != 0 else 0

# final_table.loc['Total'] = [total_2024, total_2025, total_var_pct, total_var_rs]

# print("--- Tabela Final (Gerada Apenas com Pandas) ---")
# print(final_table.to_string(formatters={'Var. %': '{:,.2f}%'.format, 2024: '{:,.2f}'.format, 2025: '{:,.2f}'.format, 'Var $': '{:,.2f}'.format}))


#%%
################################################-----COMPLETO-----#########################################################

import pandas as pd
import io

df = pd.read_excel("../dados/base_denis.xlsx")

# Regra 1: Transformar data (Pandas)
df['data'] = pd.to_datetime(df['ANOMES'], format='%Y%m')

# Regra 2: Criar "Cod_Grupo" (Pandas com .loc)
df['Cod_Grupo'] = None
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Pessoal', na=False), 'Cod_Grupo'] = '1'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Juros', na=False), 'Cod_Grupo'] = '2'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Outras', na=False), 'Cod_Grupo'] = '3'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Investimentos', na=False), 'Cod_Grupo'] = '4'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Inversoes', na=False), 'Cod_Grupo'] = '5'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Amortizacao', na=False), 'Cod_Grupo'] = '6'
df.loc[df['DES_GRUPO_DESPESA'].str.startswith('Reserva', na=False), 'Cod_Grupo'] = '9'

# Regra 3: Criar 'RPPS' (Pandas com .loc)
rpps_codes = [1801261, 2801261, 1800262, 2800262, 1802202, 2802202]
df['RPPS'] = 'Não'
df.loc[df['COD_FONTE_MAE'].isin(rpps_codes), 'RPPS'] = 'Sim'

# Regra 4: Criar "Cod_Categoria" (Pandas com .loc)
df['Cod_Categoria'] = '4'
df.loc[df['Cod_Grupo'].isin(['1', '2', '3']), 'Cod_Categoria'] = '3'

# Regra 5: Criar 'Cod_Natureza_Elemento' (Pandas)
cols_to_concat = ['Cod_Categoria', 'Cod_Grupo', 'COD_MODALIDADE', 'COD_ELEMENTO']
for col in cols_to_concat:
    df[col] = df[col].astype(str)
df['Cod_Natureza_Elemento'] = df[cols_to_concat].agg(''.join, axis=1)

# Regra 6: Criar 'Primário' (Pandas com .loc)
regex_pattern = '^(32|46|99|45..66)|^45909266$|^45909263$|^45..64$|^45909264$|^45..63$'
df['Primário'] = 'Sim'
df.loc[df['Cod_Natureza_Elemento'].str.contains(regex_pattern, na=False), 'Primário'] = 'Não'

# Regra 7: Criar 'Total_Pago' (Pandas)
df['Total_Pago'] = df['PAGO'] + df['PAGO_EXERCICIO_ANTERIOR']

# Regra 8: Imprimir a tabela final (Pandas com groupby)
filtered_df = df[(df['RPPS'] == 'Não') & (df['Primário'] == 'Sim')].copy()
filtered_df['ano'] = filtered_df['data'].dt.year
filtered_df['mes_num'] = filtered_df['data'].dt.month
summary = filtered_df.groupby(['ano', 'mes_num'])['Total_Pago'].sum().reset_index()
pivot_table = summary.pivot_table(index='mes_num', columns='ano', values='Total_Pago').fillna(0)

if 2024 not in pivot_table.columns: pivot_table[2024] = 0
if 2025 not in pivot_table.columns: pivot_table[2025] = 0

# AJUSTE: Renomeando a coluna de variação para 'Var. R$'
pivot_table['Var. R$'] = pivot_table[2025] - pivot_table[2024]
pivot_table['Var. %'] = (pivot_table['Var. R$'] / pivot_table[2024].replace(0, float('nan'))) * 100
pivot_table = pivot_table.fillna(0)

meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
         7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}
pivot_table.index = pivot_table.index.map(meses)
pivot_table = pivot_table.rename_axis('Mês')

# AJUSTE: Mudança para exibir todos os 12 meses, garantindo a ordem correta
meses_todos = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
final_table = pivot_table.reindex(meses_todos, fill_value=0)

# AJUSTE: Reordenando as colunas para corresponder ao exemplo
final_table = final_table[[2024, 2025, 'Var. %', 'Var. R$']]

# AJUSTE NOVO: Adicionando a linha de "Total"
total_2024 = final_table[2024].sum()
total_2025 = final_table[2025].sum()
total_var_rs = final_table['Var. R$'].sum()
# O percentual total é calculado sobre os totais, não somado
total_var_pct = (total_var_rs / total_2024) * 100 if total_2024 != 0 else 0

final_table.loc['Total'] = [total_2024, total_2025, total_var_pct, total_var_rs]

final_table

#%%
final_table.to_excel("ddd..xlsx")