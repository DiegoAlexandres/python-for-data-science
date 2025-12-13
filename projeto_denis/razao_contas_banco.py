#%%
import pandas as pd

#%%
pd.options.display.float_format = '{:,.2f}'.format

#%%
df = pd.read_excel("../dados/RazaoContasBanco_14102.xlsx")
df.head()

#%%
df.info()

#%%
#===============================Etapa 0=====================================
colunas = ["COCONTACONTABIL", "DALANCAMENTO"]
df[colunas] = df[colunas].astype(str)

#%%
#===============================Etapa 1=====================================
df['FR'] = df['COCONTACORRENTE'].str.slice(1, 8)
df.head()

#%%
filtro_excecao = df['COCONTACONTABIL'] == '1111102050000'
filtro_excecao.value_counts()

#%%
df.loc[filtro_excecao, 'FR'] = df.loc[filtro_excecao, 'COCONTACORRENTE'].str.slice(7, 14)
df.head()

#%%
#===============================Etapa 2=====================================
df['BANCO'] = df['COCONTACORRENTE'].str.slice(-14)
df.head()

#%%
df.loc[df['COCONTACONTABIL'] == '1111102010000', 'BANCO'] = '23703739162000'
df.head()

#%%
lista_agentes = ['1111130010000', '1111130020000']

#%%
df.loc[df['COCONTACONTABIL'].isin(lista_agentes), 'BANCO'] = 'Agente Arrecadador'
df.head()

#%%
#===============================Etapa 4=====================================
df.drop(columns=['DATA'], inplace=True)

#%%
df['DALANCAMENTO'] = df['DALANCAMENTO'].str.replace(r'00$', '01', regex=True)
df.head()

#%%
#===============================Etapa 3=====================================
df['DALANCAMENTO'] = pd.to_datetime(df['DALANCAMENTO'], format='%Y%m%d', errors='coerce')
df.head()

#%%
#===============================Etapa 5 a 9=====================================
colunas_texto = ['UGDOC', 'GESTAODOC', 'NUDOCUMENTO', 'COEVENTO', 'NOEVENTO']
df[colunas_texto] = df[colunas_texto].astype(str)

#%%
df[colunas_texto] = df[colunas_texto].replace('null', '00000').fillna('00000')
df.head()

#%%
df

#%%
#===============================Etapa 10=====================================
df['VALOR_NUMERICO'] = df['VALANCAMENTO'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
df.head()

#%%
df['ANO'] = df['DATA'].dt.year
df.head()

#%%
df = df.sort_values(by=['ANO', 'DATA'])
df.head()

#%%
df['SALDO_FINAL'] = df.groupby('ANO')['VALOR_NUMERICO'].cumsum()
df.head()
