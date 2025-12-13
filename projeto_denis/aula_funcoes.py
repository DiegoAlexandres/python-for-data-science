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
#===============================Atualizando o nome das colunas=====================================
despesas = despesas.rename(columns={"VAR $": "VAR R$", "VAR. %": "VAR %"})
despesas

#%%
#===============================Filtros dos dados=====================================
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
#===============================Relatório sem função=====================================
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
#===============================Função de formatação=====================================
def formatacao(df):

    return df.style.format(
        precision=2,
        decimal=",",
        thousands="."
    )

#%%
formatacao(resultado_df)

#%%
#===============================Criando um função=====================================
def relatorio(receitas_ano, despesas_ano):

    resultado_df = pd.concat([receitas_ano, despesas_ano], axis=1)

    resultado_df["Resultado Primário"] = receitas_ano - despesas_ano
    
    colunas_nomes = ["Receita Primária", "Despesas Primárias", "Resultado Primário"]
    resultado_df.columns = colunas_nomes
    
    # resultado_df = resultado_df.style.format(precision=2, decimal=",", thousands=".")
    
    return resultado_df

#%%
fx_resultado_2024 = relatorio(fx_receitas_2024, fx_despesas_2024)
fx_resultado_2024

#%%
fx_resultado_2025 = relatorio(fx_receitas_2025, fx_despesas_2025)
fx_resultado_2025

#%%
#===============================Resultado Primeiro YoY=====================================
resultado_primario_2024 = fx_resultado_2024["Resultado Primário"]
resultado_primario_2024

#%%
resultado_primario_2025 = fx_resultado_2025["Resultado Primário"]
resultado_primario_2025

#%%
#===============================Relatório sem função=====================================
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
#===============================Resultado Primeiro YoY=====================================
def fx_resultado_primario(receitas_ano_anterior, receitas_ano):

    relatorio_resultado = pd.concat([receitas_ano_anterior, receitas_ano], axis=1)

    relatorio_resultado.columns = ["Resultado Primário 2024", "Resultado Primário 2025"]

    relatorio_resultado["Variação % YoY"] = (relatorio_resultado["Resultado Primário 2025"] / relatorio_resultado["Resultado Primário 2024"] - 1) * 100

    relatorio_resultado = relatorio_resultado[relatorio_resultado["Resultado Primário 2025"] !=0]
    
    # relatorio_resultado = resultado_df.style.format(precision=2, decimal=",", thousands=".")
    
    return relatorio_resultado

#%%

xxx = fx_resultado_primario(resultado_primario_2024, resultado_primario_2025)

#%%
formatacao(fx_resultado_primario(resultado_primario_2024, resultado_primario_2025))

#%%
formatacao(xxx)

