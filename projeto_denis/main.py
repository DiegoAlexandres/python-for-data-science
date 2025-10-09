#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_excel("../dados/base_denis.xlsx")
df.head()

#%%
#######################################################-----1-----#########################################################

# 1. Transforma a coluna ANOMES para o formato de data (o dia será sempre 01)
df['ANOMES'] = pd.to_datetime(df['ANOMES'], format='%Y%m')

#%%
df.rename(columns={"ANOMES" : "DATA"}, inplace=True)
df.head()

#%%
#######################################################-----2-----#########################################################

# 2. Define as condições com base no início do texto em 'DES_GRUPO_DESPESA'
condicoes = [
    df['DES_GRUPO_DESPESA'].str.startswith('Pessoal', na=False),
    df['DES_GRUPO_DESPESA'].str.startswith('Juros', na=False),
    df['DES_GRUPO_DESPESA'].str.startswith('Outras', na=False),
    df['DES_GRUPO_DESPESA'].str.startswith('Investimentos', na=False),
    df['DES_GRUPO_DESPESA'].str.startswith('Inversoes', na=False),
    df['DES_GRUPO_DESPESA'].str.startswith('Amortizacao', na=False),
    df['DES_GRUPO_DESPESA'].str.startswith('Reserva', na=False)
]

# Define os valores correspondentes para cada condição
valores = ['1', '2', '3', '4', '5', '6', '9']

# Cria a nova coluna 'Cod_Grupo'
df['Cod_Grupo'] = np.select(condicoes, valores, default=None) # default=None se nenhuma condição for atendida

df.head()
#%%
df["Cod_Grupo"].unique()

#%%
#######################################################-----3-----#########################################################

# Lista dos códigos de fonte que marcam como 'Sim'
rpps_codes = [1801261, 2801261, 1800262, 2800262, 1802202, 2802202]

# Cria a coluna 'RPPS'. np.where é uma forma rápida de fazer uma declaração 'se-então-senão'.
df['RPPS'] = np.where(df['COD_FONTE_MAE'].isin(rpps_codes), 'Sim', 'Não')

print("\nColuna 'RPPS' criada:")
print(df[['COD_FONTE_MAE', 'RPPS']].head(10)) # Mostra 10 linhas para exemplo

#%%
#######################################################-----4-----#########################################################

# Verifica se o valor em 'Cod_Grupo' está na lista ['1', '2', '3']
df['Cod_Categoria'] = np.where(df['Cod_Grupo'].isin(['1', '2', '3']), '3', '4')

print("\nColuna 'Cod_Categoria' criada:")
print(df[['Cod_Grupo', 'Cod_Categoria']].head())

#%%
#######################################################-----5-----#########################################################

# Lista das colunas a serem concatenadas
cols_to_concat = ['Cod_Categoria', 'Cod_Grupo', 'COD_MODALIDADE', 'COD_ELEMENTO']

# Garante que todas as colunas são do tipo string
for col in cols_to_concat:
    df[col] = df[col].astype(str)

# Concatena os valores das colunas
df['Cod_Natureza_Elemento'] = df[cols_to_concat].agg(''.join, axis=1)

print("\nColuna 'Cod_Natureza_Elemento' criada:")
print(df[['Cod_Categoria', 'Cod_Grupo', 'COD_MODALIDADE', 'COD_ELEMENTO', 'Cod_Natureza_Elemento']].head())

#%%
#######################################################-----6-----#########################################################

# Padrão de Regex que combina todas as condições para marcar como 'Não'
regex_pattern = (
    '^(32|46|99|45..66)|'  # Começa com 32, 46, 99 ou 45..66
    '^45909266$|'            # É exatamente 45909266
    '^45909263$|'            # É exatamente 45909263
    '^45..64$|'              # É exatamente 45__64
    '^45909264$|'            # É exatamente 45909264
    '^45..63$'               # É exatamente 45__63
)

# Usa .str.contains() com regex para verificar o padrão
# O resultado será 'Não' se o padrão for encontrado, e 'Sim' caso contrário.
df['Primário'] = np.where(df['Cod_Natureza_Elemento'].str.contains(regex_pattern, na=False), 'Não', 'Sim')

print("\nColuna 'Primário' criada:")
# Exemplo de verificação:
print(df.loc[df['Cod_Natureza_Elemento'].str.startswith('32', na=False), ['Cod_Natureza_Elemento', 'Primário']].head())

#%%
#######################################################-----7-----#########################################################

df['Total_Pago'] = df['PAGO'] + df['PAGO_EXERCICIO_ANTERIOR']

print("\nColuna 'Total_Pago' criada:")
print(df[['PAGO', 'PAGO_EXERCICIO_ANTERIOR', 'Total_Pago']].head())


#%%
#######################################################-----8-----#########################################################

# 1. Filtrar o DataFrame
filtered_df = df[(df['RPPS'] == 'Não') & (df['Primário'] == 'Sim')].copy()

# Extrair ano e mês da coluna 'data'
filtered_df['ano'] = filtered_df['DATA'].dt.year
filtered_df['mes_num'] = filtered_df['DATA'].dt.month

# 2. Agrupar por ano e mês e somar o Total_Pago
summary = filtered_df.groupby(['ano', 'mes_num'])['Total_Pago'].sum().reset_index()

# Pivotar a tabela para ter anos como colunas
pivot_table = summary.pivot_table(index='mes_num', columns='ano', values='Total_Pago').fillna(0)

# Garante que as colunas 2024 e 2025 existam
if 2024 not in pivot_table.columns: pivot_table[2024] = 0
if 2025 not in pivot_table.columns: pivot_table[2025] = 0

# 3. Calcular as variações
pivot_table['Var $'] = pivot_table[2025] - pivot_table[2024]
# np.divide para evitar erro de divisão por zero
pivot_table['Var. %'] = np.divide(pivot_table['Var $'], pivot_table[2024], 
                                  out=np.zeros_like(pivot_table['Var $'], dtype=float), 
                                  where=pivot_table[2024]!=0) * 100

# 4. Formatar a tabela final
# Mapeia número do mês para nome abreviado
meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
         7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}
pivot_table.index = pivot_table.index.map(meses)
pivot_table = pivot_table.rename_axis('Mês')

# Cria um índice com todos os meses desejados para garantir que todos apareçam
meses_desejados = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago']
final_table = pivot_table.reindex(meses_desejados, fill_value=0)

# Seleciona e ordena as colunas
final_table = final_table[[2024, 2025, 'Var. %', 'Var $']]

print("\n--- Tabela Final ---")
print(final_table.to_string(formatters={'Var. %': '{:,.2f}%'.format, 2024: '{:,.2f}'.format, 2025: '{:,.2f}'.format, 'Var $': '{:,.2f}'.format}))

#%%
final_table.to_excel("teste_2.xlsx")