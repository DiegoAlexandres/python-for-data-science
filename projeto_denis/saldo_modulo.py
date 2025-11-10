#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
from receitas import receitas
from despesas import tabela

#%%
#===============================Lendo as tabelas=====================================
receitas

#%%
despesas = tabela
despesas

#%%
#===============================Tratando a tabela de despesas=====================================
despesas = despesas.rename(columns={"VAR $": "VAR R$", "VAR. %": "VAR %"})
despesas

#%%
#===============================Caminho 1 - Merge e Limpeza=====================================
df = pd.merge(receitas, despesas, on="MES", how="left", suffixes=(" RECEITAS", " DESPESAS"))
df

#%%
#===============================Criando o Relatório=====================================
colunas_para_remover = [
    '2024 RECEITAS',
    'VAR R$ RECEITAS',
    'VAR % RECEITAS',
    '2024 DESPESAS',
    'VAR R$ DESPESAS',
    'VAR % DESPESAS'
]

#%%
df_1 = df.drop(columns=colunas_para_remover)
df_1

#%%
df_1['SALDO'] = df_1['2025 RECEITAS'] - df_1['2025 DESPESAS']
df_1

#%%
#===============================Caminho 2 - Criando um novo DataFrame=====================================
receitas

#%%
despesas

#%%
receitas_2025 = receitas[2025]
receitas_2025

#%%
despesas_2025 = despesas[2025]
despesas_2025

#%%
saldo = pd.concat([receitas_2025, despesas_2025], axis=1)
saldo

#%%
saldo["Resultado Primario"] = receitas_2025 - despesas_2025
saldo

#%%
novas_colunas = ["Receita Primária", "Despesas Primárias", "Resultado Primário"]

#%%
saldo.columns = novas_colunas
saldo

#%%
saldo.index.name = 'Mes_Referencia'
saldo

#%%
saldo.reset_index()

#%%
#===============================Subindo o total=====================================
linha_total = saldo.loc[['Total']]
linha_total

#%%
linhas_meses = saldo.drop('Total')
linhas_meses

#%%
saldo_final = pd.concat([linha_total, linhas_meses])
saldo_final

#%%
saldo_final.reset_index()

#%%
#===============================Formatação de Milhares=====================================
# pip install jinja2

saldo_final.style.format(
    precision=2,      # 2 casas decimais
    decimal=',',      # Separador decimal será vírgula
    thousands='.'     # Separador de milhar será ponto
)