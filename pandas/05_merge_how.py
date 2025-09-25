#%%
import pandas as pd
#%%
# Entendendo o metodo how

# how="inner" é o padrão se não passar nada no how
# how='left'
# how='right'
# how='outer'

# 'left'	Prioridade para a tabela da Esquerda Todos da Esquerda + Correspondentes da Direita
# 'right'	Prioridade para a tabela da Direita	Todos da Direita + Correspondentes da Esquerda
# 'inner'	Apenas a Intersecção	Apenas quem está em Ambas as tabelas
# 'outer'	A União de todos	Quem está em Qualquer uma das tabelas
# 'cross'	Produto Cartesiano	Todas as combinações possíveis entre as tabelas
# 'left_anti'	Filtro de Exclusão	Apenas quem está na Esquerda, mas NÃO na Direita
# 'right_anti'	Filtro de Exclusão	Apenas quem está na Direita, mas NÃO na Esquerda

#%%
# Entendendo o metodo how na pratica
# Tabela 1: Vendas realizadas
data_vendas = {
    'VendaID': ['V101', 'V102', 'V103', 'V104', 'V105'],
    'ClienteID': [1, 2, 1, 5, 3],  # Note: ClienteID 5 não existe no cadastro
    'Valor': [250, 180, 320, 100, 450]
}
df_vendas = pd.DataFrame(data_vendas)
df_vendas

#%%
# Tabela 2: Clientes cadastrados
data_clientes = {
    'ClienteID': [1, 2, 3, 4], # Note: ClienteID 4 (Ana) nunca comprou
    'Nome': ['João', 'Maria', 'Carlos', 'Ana'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador']
}
df_clientes = pd.DataFrame(data_clientes)
df_clientes

#%%
# Tabela 3: Promoções do Mês
data_promocoes = {
    'Promocao': ['Dia do Cliente', 'Aniversário da Loja'],
    'Desconto': ['10%', '15%']
}
df_promocoes = pd.DataFrame(data_promocoes)
df_promocoes

#%%
relatorio_vendas_completo = pd.merge(
    df_vendas,      # Tabela da Esquerda (nossa base)
    df_clientes,
    on='ClienteID',
    how='left'
)
print(relatorio_vendas_completo)

#%%
relatorio_clientes_com_vendas = pd.merge(
    df_vendas,
    df_clientes,    # Tabela da Direita (nossa base)
    on='ClienteID',
    how='right'
)
print(relatorio_clientes_com_vendas)

#%%
vendas_de_clientes_validos = pd.merge(
    df_vendas,
    df_clientes,
    on='ClienteID',
    how='inner'
)
print(vendas_de_clientes_validos)


#%%
auditoria_completa = pd.merge(
    df_vendas,
    df_clientes,
    on='ClienteID',
    how='outer'
)
print(auditoria_completa)

#%%
campanha_marketing = pd.merge(
    df_clientes,
    df_promocoes,
    how='cross'
)
print(campanha_marketing)

#%%
vendas_sem_cadastro = pd.merge(
    df_vendas,
    df_clientes,
    on='ClienteID',
    how='left_anti'
)
print(vendas_sem_cadastro)

#%%
# É o mesmo que fazer pd.merge(df_clientes, df_vendas, how='left_anti')
clientes_inativos = pd.merge(
    df_vendas,
    df_clientes,
    on='ClienteID',
    how='right_anti'
)
print(clientes_inativos)