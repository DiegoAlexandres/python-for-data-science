#%%
import pandas as pd

#%%
df_largo = pd.DataFrame({
    'Vendedor': ['Ana', 'Bruno', 'Carla'],
    'Jan': [120, 150, 95],
    'Fev': [110, 140, 105],
    'Mar': [130, 165, 115]
})

df_largo

#%%
df_longo = df_largo.melt(id_vars=["Vendedor"], value_vars=['Jan', 'Fev', 'Mar'], var_name='Mes', value_name='Vendas')
df_longo

#%%
### Com Múltiplos Identificadores
df_largo_2 = pd.DataFrame({
    'Região': ['Sul', 'Sudeste', 'Sul'],
    'Vendedor': ['Ana', 'Bruno', 'Carla'],
    'Produto_A': [5200, 7800, 6100],
    'Produto_B': [3100, 4500, 4200]
})

df_largo_2

#%%
df_longo_2 = df_largo_2.melt(
    id_vars=['Região', 'Vendedor'],
    value_vars=['Produto_A', 'Produto_B'],
    var_name='Produto',
    value_name='Faturamento'
)

df_longo_2

#%%
### Aplicabilidade na pratica e vantagens de usar o melt

# A principal vantagem do formato longo é para análise e visualização.

# Usando o df_longo do primeiro exemplo, agora é muito fácil fazer perguntas como:

# Qual foi a venda média por mês?
# Quem foi o melhor vendedor?

media_mes = df_longo.groupby('Mes')['Vendas'].mean()
media_mes

#%%
# Formatando as saídas
for mes, media in media_mes.items():
  print(f"Mês de {mes}: R$ {media:.2f}")

#%%
# Formatacao com um unico valor de saida
preco = 59.9
print(f'R$ {preco:.2f}')