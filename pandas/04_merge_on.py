#%%
import pandas as pd

#%%
# Tabela 1: Planilha do Financeiro
# O ID do funcionário se chama 'ID_Func'
df_financeiro = pd.DataFrame({
    'Id_Funcionario': [101, 102, 103, 104],
    'Salario': [7000, 8200, 6500, 9500]
})

df_financeiro

#%%
# Tabela 2: Ficha do RH
# O ID do funcionário se chama 'ID_Empregado' (um nome diferente!)
df_rh = pd.DataFrame({
    'Id_Empregado': [101, 102, 103, 105], # Note que 104 não está aqui e 105 é novo
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Departamento': ['TI', 'Marketing', 'TI', 'Vendas']
})

df_rh

#%%
# Tabela 3: Alocação em Projetos
# Aqui, a combinação de Nome e Departamento é necessária para identificar alguém
df_projetos = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Ana'],
    'Departamento': ['TI', 'Vendas', 'TI', 'Marketing'], # Note: Ana de TI e Ana de Marketing
    'Projeto': ['Sistema X', 'Campanha Y', 'Sistema Z', 'Feira W']
})

df_projetos

#%%
# Vamos renomear a coluna em df_rh só para este exemplo
df_rh_renomeado = df_rh.rename(columns={'Id_Empregado': 'Id_Funcionario'})
df_rh_renomeado

#%%
# Agora que os nomes são iguais, podemos usar 'on'
relatorio_on = pd.merge(
    df_financeiro,
    df_rh_renomeado,
    on='Id_Funcionario', # Simples e direto
    how='inner'
)
print(relatorio_on)

#%%
relatorio_left_right_on = pd.merge(
    df_financeiro,      # Tabela da Esquerda
    df_rh,              # Tabela da Direita
    left_on='Id_Funcionario',      # Chave na tabela da esquerda
    right_on='Id_Empregado',# Chave na tabela da direita
    how='inner'
)
print(relatorio_left_right_on)

#%%
df_funcionarios = df_rh[['Nome', 'Departamento']] # Pegando só Nome e Depto do RH
df_funcionarios
#%%
relatorio_multiplas_chaves = pd.merge(
    df_funcionarios,
    df_projetos,
    # Passamos uma LISTA de colunas para o 'on'
    on=['Nome', 'Departamento'],
    how='left'
)
print(relatorio_multiplas_chaves)

#%%
# Definindo a coluna 'ID_Empregado' como o índice do DataFrame de RH
df_rh_com_index = df_rh.set_index('Id_Empregado')

print("--- RH com Índice ---")
print(df_rh_com_index)

#%%
# Juntando uma coluna ('ID_Func') com um índice ('ID_Empregado')
relatorio_com_index = pd.merge(
    df_financeiro,
    df_rh_com_index,
    left_on='Id_Funcionario',      # Na esquerda, usamos a coluna
    right_index=True,       # Na direita, usamos o ÍNDICE
    how='inner'
)
print("\n--- Relatório com Índice ---")
print(relatorio_com_index)


#%%
# Outros exemplos praticos
relatorio_ti = pd.merge(
    df_rh,
    df_projetos,
    on=['Nome', 'Departamento'], 
    how='inner'
)
print(relatorio_ti)

#%%
# Outros exemplos praticos
salario_ti = pd.merge(
    relatorio_ti,
    df_financeiro,
    left_on='Id_Empregado', right_on='Id_Funcionario',
    how='inner'
)
salario_ti

#%%
# Exemplo de erro - Todas as colunas que você lista em on devem existir, 
# com o mesmo nome, em ambas as tabelas que estão sendo unidas.
salario_ti = pd.merge(
    relatorio_ti,
    df_financeiro,
    on=['Nome', 'Salario'],
    how='inner'
)
salario_ti