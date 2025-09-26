#%%
import pandas as pd

dados = [20, 30, 50, 46, 90, 100]

#%%
type(dados)

#%%
serie = pd.Series(dados)
serie

#%%
# Exercício 1: Explorando os Atributos da Série
# Objetivo: Aprender a inspecionar as propriedades básicas de uma Series para entender sua estrutura.
# Acessando o índice (index) da Série
print("Índice da Série:")
print(serie.index)

#%%
# Acessando os valores como um array NumPy
print("\nValores da Série:")
print(serie.values)

#%%
type(serie.values)

#%%
# Verificando o tipo de dado (dtype)
print(f"\nTipo de Dado (dtype): {serie.dtype}")

#%%
# Verificando o número de elementos
print(f"\nNúmero de Elementos (size): {serie.size}")

#%%
# Exercício 2: Acessando Elementos (Indexação e Fatiamento)
# Objetivo: Praticar como selecionar um ou mais elementos específicos de uma Series.
# Acessar o primeiro elemento (índice 0)
primeiro_elemento = serie[0]
print(f"Primeiro elemento: {primeiro_elemento}")

#%%
# Acessar o último elemento (usando indexação negativa)
ultimo_elemento = serie.iloc[-1]
print(f"Último elemento: {ultimo_elemento}")

#%%
# Acessar os elementos do índice 1 até o 3 (fatiamento ou slicing)
fatia = serie[1:4]
print("\nElementos do índice 1 ao 3:")
print(fatia)

#%%
# Exercício 3: Operações Vetorizadas (Matemática em Lote)
# Objetivo: Entender a principal vantagem do Pandas: aplicar uma operação a todos os elementos de uma vez, sem a necessidade de um loop for.
# Criar uma nova Série onde cada elemento é o valor original + 10
serie_mais_10 = serie + 10

print("--- Série original ---")
print(serie)
print("\n--- Série com cada elemento + 10 ---")
print(serie_mais_10)

#%%
# Exercício 4: Filtragem com Condições (Máscara Booleana)
# Objetivo: Aprender a filtrar a Series para manter apenas os elementos que atendem a uma determinada condição. Esta é uma das técnicas mais poderosas do Pandas.
# 1. Criar a condição (máscara booleana)
condicao = serie > 50
print("--- Máscara Booleana (True onde o valor é > 50) ---")
print(condicao)
#%%
# 2. Aplicar a máscara para filtrar a Série original
valores_altos = serie[condicao]
print("\n--- Apenas os valores maiores que 50 ---")
print(valores_altos)

#%%
# Exercício 5: Estatísticas Descritivas
# Objetivo: Utilizar métodos integrados para calcular rapidamente as principais estatísticas da sua Series.
# Calcular a soma de todos os valores
soma_total = serie.sum()
print(f"Soma total: {soma_total}")

#%%
# Calcular a média dos valores
media = serie.mean()
print(f"Média: {media}")

#%%
# Encontrar o valor máximo
valor_maximo = serie.max()
print(f"Valor máximo: {valor_maximo}")

#%%
# (Bônus) Usar o método describe() para um resumo completo
resumo_estatistico = serie.describe()
print("\n--- Resumo Estatístico Completo ---")
print(resumo_estatistico)