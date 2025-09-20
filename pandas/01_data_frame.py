#%%
import pandas as pd

# Criando um dicionário com os dados dos produtos
dados_produtos = {
    'Nome': ['Caneta', 'Caderno', 'Lápis', 'Borracha', 'Teclado', 'Mouse'],
    'Categoria': ['Papelaria', 'Papelaria', 'Papelaria', 'Papelaria', 'Eletrônicos', 'Eletrônicos'],
    'Preço': [1.50, 15.00, 0.80, 2.00, 80.00, 50.00],
    'Estoque': [100, 50, 200, 150, 30, 45]
}

# Criando o DataFrame a partir do dicionário
df_produtos = pd.DataFrame(dados_produtos)

#%%
# Exercício 1: Inspeção Básica do DataFrame
# Objetivo: Aprender os comandos essenciais para "sentir" e entender a estrutura de um novo DataFrame
# 1. Visualizar as 5 primeiras linhas
print("--- Primeiras 5 linhas (head) ---")
print(df_produtos.head())

# 2. Obter um resumo técnico (tipos de dados, valores nulos)
print("\n--- Informações do DataFrame (info) ---")
df_produtos.info()

# 3. Ver o número de linhas e colunas (formato)
print(f"\nFormato do DataFrame (linhas, colunas): {df_produtos.shape}")

# 4. Obter um resumo estatístico das colunas numéricas
print("\n--- Resumo Estatístico (describe) ---")
print(df_produtos.describe())

#%%
# Exercício 2: Selecionando Colunas e Linhas (.loc e .iloc)
# Objetivo: Praticar as diferentes formas de selecionar fatias específicas do DataFrame.
# 1. Selecionar uma única coluna ('Preço')
coluna_preco = df_produtos['Preço']
print("--- Selecionando a coluna 'Preço' (resultado é uma Series) ---")
print(type(coluna_preco))
print(coluna_preco)


# 2. Selecionar múltiplas colunas ('Nome' e 'Estoque')
colunas_nome_estoque = df_produtos[['Nome', 'Estoque']]
print("\n--- Selecionando as colunas 'Nome' e 'Estoque' (resultado é um DataFrame) ---")
print(colunas_nome_estoque)


# 3. Selecionar a linha na posição 0 (primeira linha) usando iloc
primeira_linha = df_produtos.iloc[0]
print("\n--- Selecionando a primeira linha por posição (iloc) ---")
print(primeira_linha)

# 4. Selecionar o 'Preço' do produto na linha de posição 3 (quarta linha)
preco_borracha = df_produtos.loc[3, 'Preço']
print(f"\nPreço do produto na linha de índice 3: {preco_borracha}")

#%%
# Exercício 3: Filtragem de Dados com Condições
# Objetivo: Aprender a selecionar linhas de um DataFrame que atendem a critérios específicos.
# 1. Filtrar todos os produtos da categoria 'Papelaria'
produtos_papelaria = df_produtos[df_produtos['Categoria'] == 'Papelaria']
print("--- Produtos da Categoria 'Papelaria' ---")
print(produtos_papelaria)

# 2. Filtrar produtos com estoque abaixo de 50 unidades
baixo_estoque = df_produtos[df_produtos['Estoque'] < 50]
print("\n--- Produtos com Baixo Estoque (< 50) ---")
print(baixo_estoque)

# 3. (Desafio) Filtrar produtos que são de 'Papelaria' E têm preço maior que R$10,00
papelaria_cara = df_produtos[(df_produtos['Categoria'] == 'Papelaria') & (df_produtos['Preço'] > 10)]
print("\n--- Produtos de Papelaria com Preço > R$10,00 ---")
print(papelaria_cara)


#%%
# Exercício 4: Criando Novas Colunas
# Objetivo: Aprender a adicionar colunas ao DataFrame, muitas vezes calculadas a partir de colunas existentes.
# Criar uma nova coluna 'ValorTotalEstoque' = Preço * Estoque
df_produtos['ValorTotalEstoque'] = df_produtos['Preço'] * df_produtos['Estoque']

print("--- DataFrame com a Nova Coluna 'ValorTotalEstoque' ---")
print(df_produtos)

#%%
# Exercício 5: Ordenando o DataFrame
# Objetivo: Aprender a reordenar as linhas do DataFrame com base nos valores de uma ou mais colunas.
# 1. Ordenar os produtos do mais barato para o mais caro
produtos_por_preco = df_produtos.sort_values(by='Preço')
print("--- Produtos Ordenados por Preço (crescente) ---")
print(produtos_por_preco)

# 2. Ordenar os produtos pela quantidade em estoque, do maior para o menor
produtos_por_estoque = df_produtos.sort_values(by='Estoque', ascending=False)
print("\n--- Produtos Ordenados por Estoque (decrescente) ---")
print(produtos_por_estoque)


#%%
novo_indice = [101, 102, 103, 104, 105, 106]
df_produtos.index = novo_indice
df_produtos

#%%

# ESTUDOS LOC

# Exercícios com .loc (Seleção por Rótulo/Indice)
# Exercício 1: Selecionando um Intervalo de Linhas
# Objetivo: Selecionar um bloco contínuo de linhas usando seus rótulos de índice.
# Selecionar todas as linhas desde o rótulo 102 até o rótulo 104
intervalo_loc = df_produtos.loc[102:104]

print("\n--- Exercício 1 (.loc): Intervalo de 102 a 104 ---")
print(intervalo_loc)

# Explicação
# Usamos df_produtos.loc[102:104] para fazer um "fatiamento" (slicing) pelos rótulos.
# O ponto mais importante aqui é que o fatiamento com .loc é INCLUSIVO. 
# Ou seja, ele inclui tanto o rótulo de início (102) quanto o rótulo de fim (104) no resultado.

#%%
# Exercício 2: Selecionando Linhas e Colunas Específicas
# Objetivo: Selecionar dados de forma precisa, escolhendo exatamente quais linhas e quais colunas você quer ver,
# pelos seus nomes.
# Selecionar as linhas de rótulo 101 e 106, e apenas as colunas 'Nome' e 'Estoque'
selecao_especifica_loc = df_produtos.loc[[101, 106], ['Nome', 'Estoque']]

print("\n--- Exercício 2 (.loc): Linhas [101, 106] e Colunas ['Nome', 'Estoque'] ---")
print(selecao_especifica_loc)

# Explicação 
# O .loc aceita uma lista de rótulos para as linhas e uma lista de nomes para as colunas.
# A sintaxe é .loc[[lista_de_rotulos_linhas], [lista_de_nomes_colunas]]. Isso permite extrair "recortes"
# muito específicos do seu DataFrame.


#%%
# Trazer linhas específicas e TODAS as colunas: (Você omite a parte das colunas)
df_produtos.loc[[101, 106]]


#%%
# Trazer TODAS as linhas e colunas específicas: (Você usa : para representar "todas as linhas")
df_produtos.loc[:, ['Nome', 'Estoque']]

#%%

# ESTUDOS ILOC

# A sintaxe geral é [início : fim]. Vamos detalhar como ela funciona no seu exemplo df_produtos.iloc[1:4]:

# Exercícios com .iloc (Seleção por Posição)
# Exercício 1: Selecionando um Intervalo de Linhas
# Objetivo: Selecionar um bloco contínuo de linhas usando suas posições numéricas, independentemente dos rótulos.
# Selecionar as linhas que estão na posição 1, 2 e 3 (ou seja, a segunda, terceira e quarta linha)
intervalo_iloc = df_produtos.iloc[1:4]

print("\n--- Exercício 1 (.iloc): Intervalo da posição 1 até a 4 (exclusive) ---")
print(intervalo_iloc)

# Explicação
# Usamos df_produtos.iloc[1:4]. Aqui, 1 e 4 são as posições das linhas (começando em 0).
# Note que o resultado é o mesmo do Exercício 1 do .loc, mas a forma de pedir é diferente.
# O ponto crucial é que o fatiamento com .iloc funciona como no Python: ele é EXCLUSIVO. Ou seja,
# ele começa na posição 1 e vai até, mas não inclui, a posição 4.

#%%
# Exercício 2: Selecionando Linhas e Colunas Específicas
# Objetivo: Selecionar dados de forma precisa, usando apenas as coordenadas numéricas de linhas e colunas.
# Selecionar a primeira (0) e a última (-1) linha,
# e a primeira (0) e a terceira (2) coluna.
selecao_especifica_iloc = df_produtos.iloc[[0, -1], [0, 2]]

print("\n--- Exercício 2 (.iloc): Linhas [0, -1] e Colunas [0, 2] ---")
print(selecao_especifica_iloc)

# Explicação
# Aqui, estamos pedindo:
# Linhas: A de posição 0 (a primeira) e a de posição -1 (a última). Usar índices negativos é muito útil com .iloc.
# Colunas: A de posição 0 (Nome) e a de posição 2 (Preço).
