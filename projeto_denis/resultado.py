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
#===============================Selecionando as colunas necessarias=====================================
receitas_2025 = receitas[2025]
receitas_2025

#%%
despesas_2025 = despesas[2025]
despesas_2025

#%%
#===============================Concatenando em um novo dataframe=====================================
resultado = pd.concat([receitas_2025, despesas_2025], axis=1)
resultado

#%%
resultado["Resultado Primario"] = receitas_2025 - despesas_2025
resultado

#%%
#===============================Renomeando as colunas=====================================
novas_colunas = ["Receita Primária", "Despesas Primárias", "Resultado Primário"]

#%%
resultado.columns = novas_colunas
resultado

#%%
resultado.index.name = 'Mês Referência'
resultado

#%%
resultado.reset_index()

#%%
#===============================Subindo o total=====================================
linha_total = resultado.loc[['Total']]
linha_total

#%%
linhas_meses = resultado.drop('Total')
linhas_meses

#%%
resultado_final = pd.concat([linha_total, linhas_meses])
resultado_final

#%%
resultado_final.reset_index()

#%%
#===============================Formatação de Milhares=====================================
# pip install jinja2

resultado_final.style.format(
    precision=2,      # 2 casas decimais
    decimal=',',      # Separador decimal será vírgula
    thousands='.'     # Separador de milhar será ponto
)

#%%
type(resultado_final)

#%%
#===============================Resultado 2024=====================================
receitas

#%%
despesas

#%%
receitas_2024 = receitas[2024]
receitas_2024

#%%
despesas_2024 = despesas[2024]
despesas_2024

#%%
resultado_2024 = pd.concat([receitas_2024, despesas_2024], axis=1)
resultado_2024

#%%
resultado_2024["Resultado Primário"] = receitas_2024 - despesas_2024
resultado_2024

#%%
colunas_2024 = ["Receita Primária", "Despesas Primárias", "Resultado Primário"]

#%%
resultado_2024.columns = colunas_2024
resultado_2024

#%%
resultado_2024.style.format(
    precision = 2,
    decimal= ",",
    thousands="."
)










#%%
#===============================Criando um função=====================================
receitas

#%%
despesas

#%%
fx_receitas_2024 = receitas[2024]
fx_receitas_2024

#%%
fx_despesas_2024 = despesas[2024]
fx_despesas_2024

#%%
fx_receitas_2025 = receitas[2025]
fx_receitas_2025

#%%
fx_despesas_2025 = despesas[2025]
fx_despesas_2025

#%%
resultado_df = pd.concat([fx_receitas_2024, fx_despesas_2024], axis=1)
resultado_df

#%%
resultado_df["Resultado Primário"] = fx_receitas_2024 - fx_despesas_2024
resultado_df

#%%
colunas_nomes = ["Receita Primária", "Despesas Primárias", "Resultado Primário"]
resultado_df.columns = colunas_nomes

#%%
resultado_df

#%%
def resultado_primario(receitas_ano, despesas_ano):

    resultado_df = pd.concat([receitas_ano, despesas_ano], axis=1)

    resultado_df["Resultado Primário"] = receitas_ano - despesas_ano
    
    colunas_nomes = ["Receita Primária", "Despesas Primárias", "Resultado Primário"]
    resultado_df.columns = colunas_nomes
    
    # resultado_df = resultado_df.style.format(precision=2, decimal=",", thousands=".")
    
    return resultado_df

#%%
fx_resultado_2024 = resultado_primario(fx_receitas_2024, fx_despesas_2024)
fx_resultado_2024

#%%
fx_resultado_2025 = resultado_primario(fx_receitas_2025, fx_despesas_2025)
fx_resultado_2025

#%%
#===============================Formação como função=====================================
def formatacao(df):

    return df.style.format(
        precision=2,
        decimal=",",
        thousands="."
    )


#%%
#===============================Resultado Primeiro YoY=====================================
resultado_primario_2024 = fx_resultado_2024["Resultado Primário"]
resultado_primario_2024

#%%
resultado_primario_2025 = fx_resultado_2025["Resultado Primário"]
resultado_primario_2025

#%%
relatorio_resultado = pd.concat([resultado_primario_2024, resultado_primario_2025], axis=1)
relatorio_resultado

#%%
relatorio_resultado.columns = ["Resultado Primário 2024", "Resultado Primário 2025"]
relatorio_resultado

#%%
relatorio_resultado["Variação % YoY"] = (relatorio_resultado["Resultado Primário 2025"] / relatorio_resultado["Resultado Primário 2024"] - 1) * 100
relatorio_resultado

#%%
relatorio_resultado = relatorio_resultado[relatorio_resultado["Resultado Primário 2025"] !=0]
relatorio_resultado

#%%
formatacao(relatorio_resultado)
















#%%
#===============================Separando Colunas=====================================
dados = pd.read_excel("../dados/Base_Receitas-x.xlsx")
dados

#%%
dados[["Fonte_Mae Cod e Descricao"]]

#%%
dados[["Fonte_Mae Codigo", "Fonte_Mae Descricao"]] = dados["Fonte_Mae Cod e Descricao"].str.split(" - ", n=1, expand=True)
dados

#%%
# .str.get(0) pega o primeiro item da lista criada pelo split
dados["Fonte_Mae Cod e Descricao"] = dados["Fonte_Mae Cod e Descricao"].str.split(" - ", n=1).str.get(0)
dados

#%%
# .str.get(1) pega o segundo item da lista criada pelo split
dados["Fonte_Mae Cod e Descricao"] = dados["Fonte_Mae Cod e Descricao"].str.split(" - ", n=1).str.get(1)

#%%
#===============================Separando Colunas e Criando Novas=====================================
# 1. Faz o split UMA VEZ e salva a Série de listas
split_resultado = dados["Fonte_Mae Cod e Descricao"].str.split(" - ", n=1)
split_resultado

#%%
# 2. Pega o item 0 (código) e SOBRESCREVE a coluna original
dados["Fonte_Mae Cod e Descricao"] = split_resultado.str.get(0)

#%%
# 3. Pega o item 1 (descrição) e CRIA a nova coluna
dados["Fonte_Mae Descricao"] = split_resultado.str.get(1)

#%%
dados

