#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
df = pd.read_excel("../dados/Base_Receitas.xlsx")
df.head()

#%%
df.info()

#%%
#===============================Etapa 1=====================================
df["ANOMES"] = pd.to_datetime(df["ANOMES"], format="%Y%m")

#%%
df.info()

#%%
df["Cod_Natureza"] = df["Cod_Natureza"].astype(str)

#%%
df.info()

#%%
#===============================Etapa 2=====================================
codigo_rpps = [1801261, 2801261, 1802262, 2802262, 1802202, 2802202]     

df["RPPS"] = "Não"

#%% 
df.loc[df["COD_FONTE_MAE_RPPS"].isin(codigo_rpps), "RPPS"] = "Sim"

#%%
df["RPPS"].value_counts()

#%%
#===============================Etapa 3=====================================
# 1321%; 2230%; 21%; 23%; 1990111%; 1922012%; 1990992%

padroes = '^(13|22|21|23)|^1990111|^1922012|^1990992'

#%%
df["PRIMARIO"] = "P"

df.head()

#%%
df.loc[df["Cod_Natureza"].str.contains(padroes, na=False), "PRIMARIO"] = "F"

df.head()
#%%
df["PRIMARIO"].value_counts()

#%%
#===============================Etapa 4=====================================
df_financeiro = df[df["PRIMARIO"] == "F"]
df_financeiro
#%%
df_financeiro["Cod_Natureza"].value_counts()

#%%
df

#%%
#===============================Relatório Etpa 1=====================================
df_novo = df[(df["RPPS"] == "Não") & (df["PRIMARIO"] == "P")].copy()
df_novo

#===============================Relatório Etpa 2=====================================
df_novo["ANO"] = df_novo["ANOMES"].dt.year
df_novo["MES"] = df_novo["ANOMES"].dt.month

df_novo

#%%
#===============================Relatório Etpa 3=====================================
relatorio = df_novo.groupby(["ANO", "MES"])["Receita Líquida"].sum().reset_index()
relatorio

#%%
#===============================Relatório Etpa 4=====================================
relatorio_2 = relatorio.pivot_table(index="MES", columns="ANO", values="Receita Líquida").fillna(0)
relatorio_2

#%%
#===============================Relatório Etpa 4=====================================
relatorio_2["VAR R$"] = relatorio_2[2025] - relatorio_2[2024] 
relatorio_2

#%%
relatorio_2["VAR %"] = relatorio_2["VAR R$"] / relatorio_2[2024] * 100
relatorio_2

#===============================Relatório Etpa 5 = Última Etapa=====================================
#%%
meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
         7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}

#%%
relatorio_2.index = relatorio_2.index.map(meses)
relatorio_2.index

#%%
total_2024 = relatorio_2[2024].sum()
total_2025 = relatorio_2[2025].sum()

#%%
total_variacao_rs = relatorio_2["VAR R$"].sum()

#%%
total_variacao = (total_variacao_rs / total_2024) * 100

#%%
relatorio_2.loc["Total"] = [total_2024, total_2025, total_variacao_rs, total_variacao]

#%%
receitas = relatorio_2

#%%
receitas

#%%
# receitas.to_excel("receitas.xlsx")