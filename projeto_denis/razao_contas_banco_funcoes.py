#%%
import pandas as pd

#%%
pd.options.display.float_format = '{:,.2f}'.format

#%%
df = pd.read_excel("../dados/RazaoContasBanco_14102.xlsx")
df.head()


#%%
#===============================Etapa 1=====================================
# Definimos uma função que contém as regras de negócio
def definir_fr(linha):
    conta = str(linha['COCONTACONTABIL'])
    corrente = str(linha['COCONTACORRENTE'])
    
    # Regra específica 1
    if conta == '1111102010000':
        return corrente[1:8]
    # Regra específica 2 (pega da posição 8 em diante por 7 caracteres)
    elif conta == '1111102050000':
        return corrente[7:14] 
    # Regra geral para as outras contas listadas
    elif conta in ['1111119010000', '1111119020000', '1111119030000', 
                   '1111119050000', '1111130010000', '1111130020000']:
        return corrente[1:8]
    else:
        return corrente[1:8] # Caso padrão se não cair em nenhuma acima

# Aplicamos essa função em cada linha (axis=1) para criar a nova coluna
df['FR'] = df.apply(definir_fr, axis=1)



#%%
#===============================Etapa 2=====================================
def definir_banco(linha):
    conta = str(linha['COCONTACONTABIL'])
    corrente = str(linha['COCONTACORRENTE'])
    
    if conta == '1111102010000':
        return '23703739162000'
    elif conta in ['1111130010000', '1111130020000']:
        return 'Agente Arrecadador'
    else:
        # Pega os 14 caracteres da direita
        return corrente[-14:]

df['BANCO'] = df.apply(definir_banco, axis=1)



#%%
#===============================Etapa 3=====================================
# Garante que é texto primeiro
df['DALANCAMENTO'] = df['DALANCAMENTO'].astype(str)

# Função lambda: Se terminar com '00', pega tudo menos os 2 últimos e adiciona '01'. Senão, mantém igual.
df['DALANCAMENTO'] = df['DALANCAMENTO'].apply(lambda x: x[:-2] + '01' if x.endswith('00') else x)


#%%
#===============================Etapa 4=====================================
df['DATA'] = pd.to_datetime(df['DALANCAMENTO'], format='%Y%m%d', errors='coerce')


#%%
#===============================Etapa 5=====================================
colunas_para_limpar = ['UGDOC', 'GESTAODOC', 'NUDOCUMENTO', 'COEVENTO', 'NOEVENTO']

for coluna in colunas_para_limpar:
    # Verifica se a coluna existe no seu arquivo para evitar erros
    if coluna in df.columns:
        # 1. Converte para texto
        # 2. Substitui a palavra escrita "null" por "00000"
        # 3. Se tiver vazio real (NaN), preenche com "00000"
        df[coluna] = df[coluna].astype(str).replace('null', '00000').fillna('00000')


#%%
#===============================Etapa 6=====================================
colunas_para_limpar = ['UGDOC', 'GESTAODOC', 'NUDOCUMENTO', 'COEVENTO', 'NOEVENTO']

for coluna in colunas_para_limpar:
    # Verifica se a coluna existe no seu arquivo para evitar erros
    if coluna in df.columns:
        # 1. Converte para texto
        # 2. Substitui a palavra escrita "null" por "00000"
        # 3. Se tiver vazio real (NaN), preenche com "00000"
        df[coluna] = df[coluna].astype(str).replace('null', '00000').fillna('00000')




#%%
#===============================Etapa 7=====================================
colunas_para_limpar = ['UGDOC', 'GESTAODOC', 'NUDOCUMENTO', 'COEVENTO', 'NOEVENTO']

for coluna in colunas_para_limpar:
    # Verifica se a coluna existe no seu arquivo para evitar erros
    if coluna in df.columns:
        # 1. Converte para texto
        # 2. Substitui a palavra escrita "null" por "00000"
        # 3. Se tiver vazio real (NaN), preenche com "00000"
        df[coluna] = df[coluna].astype(str).replace('null', '00000').fillna('00000')


#%%
#===============================Etapa 8=====================================
colunas_para_limpar = ['UGDOC', 'GESTAODOC', 'NUDOCUMENTO', 'COEVENTO', 'NOEVENTO']

for coluna in colunas_para_limpar:
    # Verifica se a coluna existe no seu arquivo para evitar erros
    if coluna in df.columns:
        # 1. Converte para texto
        # 2. Substitui a palavra escrita "null" por "00000"
        # 3. Se tiver vazio real (NaN), preenche com "00000"
        df[coluna] = df[coluna].astype(str).replace('null', '00000').fillna('00000')


#%%
#===============================Etapa 9=====================================
colunas_para_limpar = ['UGDOC', 'GESTAODOC', 'NUDOCUMENTO', 'COEVENTO', 'NOEVENTO']

for coluna in colunas_para_limpar:
    # Verifica se a coluna existe no seu arquivo para evitar erros
    if coluna in df.columns:
        # 1. Converte para texto
        # 2. Substitui a palavra escrita "null" por "00000"
        # 3. Se tiver vazio real (NaN), preenche com "00000"
        df[coluna] = df[coluna].astype(str).replace('null', '00000').fillna('00000')


#%%
#===============================Etapa 10=====================================
# 10.1 Limpeza do valor monetário
# Remove o ponto de milhar (.) e troca a vírgula (,) por ponto (.)
df['VALOR_NUMERICO'] = df['VALANCAMENTO'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
# Converte para número decimal (float)
df['VALOR_NUMERICO'] = pd.to_numeric(df['VALOR_NUMERICO'])

# 10.2 Criar coluna de Ano para separar os cálculos
df['ANO_CALCULO'] = df['DATA'].dt.year

# 10.3 Ordenar: Para o saldo fazer sentido, tem que ser dia após dia
df = df.sort_values(by=['ANO_CALCULO', 'DATA'])

# 10.4 O Cálculo Mágico (groupby + cumsum)
# "Para cada ANO, vá somando o VALOR_NUMERICO linha a linha"
df['SALDO_FINAL'] = df.groupby('ANO_CALCULO')['VALOR_NUMERICO'].cumsum()

# (Opcional) Removendo colunas auxiliares se quiser limpar a visualização
# df = df.drop(columns=['VALOR_NUMERICO', 'ANO_CALCULO'])

