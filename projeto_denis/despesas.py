#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
df = pd.read_excel("../dados/Base_Despesas.xlsx")
df.head()

#%%
df.info()

#%%
############################Etapa_0############################
# Analise da etapa zero

df["COD_ELEMENTO"] = df["COD_ELEMENTO"].astype(str).str.zfill(2)
df.head()

#%%
############################Etapa_1############################

df["ANOMES"] = pd.to_datetime(df["ANOMES"], format="%Y%m", errors="coerce")
df.head()

#%%
df = df.rename(columns={"ANOMES" : "DATA"})
df.head()

#%%
# ===================================Etapa_2==============================
# Etapa 2 - Criar coluna do cod_grupo

df["COD_GRUPO"] = None
df.head()

#%%
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Pessoal", na=False), "COD_GRUPO"] = "1"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Juros", na=False), "COD_GRUPO"] = "2"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Outras", na=False), "COD_GRUPO"] = "3"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Investimentos", na=False), "COD_GRUPO"] = "4"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Inversoes", na=False), "COD_GRUPO"] = "5"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Amortizacao", na=False), "COD_GRUPO"] = "6"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Reserva", na=False), "COD_GRUPO"] = "9"

df.head(10)


#%%
# Etapa 3
df["RPPS"] = "Não"
df.head()

#%%
codigo_rpps = [1801261, 2801261, 1802262, 2802262, 1802202, 2802202]

#%%
df.loc[df["COD_FONTE_MAE"].isin(codigo_rpps), "RPPS"] = "Sim"
df.tail(10)

#%%
df["RPPS"].unique()


#%%
# Etapa 4
df["COD_CATEGORIA"] = "4"
df.head()

#%%
df.loc[df["COD_GRUPO"].isin(["1", "2", "3"]), "COD_CATEGORIA"] = "3"
df.tail()

#%%
df["COD_CATEGORIA"].unique()


#%%
# Etapa 5

colunas = ["COD_CATEGORIA", "COD_GRUPO", "COD_MODALIDADE", "COD_ELEMENTO"]

#%%
for coluna in colunas:
    df[coluna] = df[coluna].astype(str)
    
#%%

df["COD_NATUREZA"] = df[colunas].agg("".join, axis=1)

df.head()

#%%
# Etapa 6
padroes = '^(32|46|99|45..66)|^45909266$|^45909263$|^45..64$|^45909264$|^45..63$'

#%%
df["PRIMARIO?"] = "P"
df.head()

#%%
df.loc[df["COD_NATUREZA"].str.contains(padroes, na=False), "PRIMARIO?"] = "F"
df.head()

#%%
df["PRIMARIO?"].unique()


#%%
grupo_2 = df[df["COD_GRUPO"] == "2"]

grupo_2["PRIMARIO?"].unique()

#%%

df.head()

#%%
# Etapa 7
df["PAGO_EXERCICIO_ANTERIOR"] = df["PAGO_EXERCICIO_ANTERIOR"].fillna(0)

#%%
df["TOTAL PAGO"] = df["PAGO"] + df["PAGO_EXERCICIO_ANTERIOR"]
df.head()

#%%
df["TOTAL PAGO"].unique()

#%%
df

#%%
# Etapa 8
novo_df = df[
    (df["RPPS"] == "Não") & 
    (df["PRIMARIO?"] == "P")
].copy()

#%%
novo_df.head()

#%%
novo_df["ANO"] = novo_df["DATA"].dt.year
novo_df.head()

#%%
novo_df["MES"] = novo_df["DATA"].dt.month
novo_df.head()

#%%
resumo = novo_df.groupby(["ANO", "MES"])["TOTAL PAGO"].sum().reset_index()
resumo

#%%
tabela = resumo.pivot_table(index="MES", columns="ANO", values="TOTAL PAGO").fillna(0)
tabela

#%%
tabela["VAR $"] = tabela[2025] - tabela[2024]
tabela

#%%
tabela['VAR. %'] = tabela['VAR $'] / tabela[2024] * 100
tabela

#%%
meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
         7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}

#%%
tabela.index = tabela.index.map(meses)
tabela.index

#%%
total_2024 = tabela[2024].sum()
total_2025 = tabela[2025].sum()

#%%
total_variacao_rs = tabela["VAR $"].sum()
total_variacao = (total_variacao_rs / total_2024) * 100

#%%
tabela.loc["Total"] = [total_2024, total_2025, total_variacao_rs, total_variacao]

#%%
tabela

#%%
# tabela.to_excel("despesas.xlsx")