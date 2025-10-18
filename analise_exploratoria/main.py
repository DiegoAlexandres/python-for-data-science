
#%%
import pandas as pd

#%%
df = pd.read_excel("../dados/base_denis.xlsx")
df.head()

#%%
# =================== Etapa 1 ===================
df["ANOMES"] = pd.to_datetime(df["ANOMES"], format="%Y%m")
df = df.rename(columns={"ANOMES": "DATA"})
df.head()

#%%
df.info()

#%%
# =================== Etapa 2 ===================

df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Pessoal"), "COD_GRUPO"] = "1"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Juros"), "COD_GRUPO"] = "2"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Outras"), "COD_GRUPO"] = "3"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Investimentos"), "COD_GRUPO"] = "4"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Inversoes"), "COD_GRUPO"] = "5"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Amortizacao"), "COD_GRUPO"] = "6"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Reserva"), "COD_GRUPO"] = "9"
df.head()


#%%
# =================== Etapa 3 ===================

codigos_rpps = [1801261, 2801261, 1800262, 2800262, 1802202, 2802202]

df["RPPS"] = "Não"

df.loc[df["COD_FONTE_MAE"].isin(codigos_rpps), "RPPS"] = "Sim"
df.head()

#%%
df[df["RPPS"] == "Sim"].head()

#%%
# =================== Etapa 4 ===================

codigos_cateorias = [1, 2, 3]

df["COD_CATEGORIA"] = 4

#%%
df["COD_GRUPO"] = df["COD_GRUPO"].astype(int)
df.info()

#%%
df.loc[df["COD_GRUPO"].isin(codigos_cateorias), "COD_CATEGORIA"] = 3
df.head()

#%%
df["COD_CATEGORIA"].unique()

#%%
# =================== Etapa 5 ===================

colunas = ['COD_CATEGORIA', 'COD_GRUPO', 'COD_MODALIDADE', 'COD_ELEMENTO']

for coluna in colunas:
    df[coluna] = df[coluna].astype(str)

#%%
df["COD_NATUREZA_ELEMENTO"] = df[colunas].agg(''.join, axis=1)
df.head()

#%%
df.info()

#%%
# =================== Etapa 6 ===================

