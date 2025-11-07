#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
df = pd.read_excel("../dados/base_denis.xlsx")
df.sample(10)

#%%
#===================================0===================================
df["COD_ELEMENTO"] = df["COD_ELEMENTO"].astype(str).str.zfill(2)
df.sample(10)

#%%
#===================================1===================================
df["ANOMES"] = pd.to_datetime(df["ANOMES"], format="%Y%m", errors="coerce")
df.sample(10)

#%%
df = df.rename(columns={"ANOMES" : "DATA"})
df.sample(10)

#===================================2===================================
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Pessoal"), "COD_GRUPO"] = "1"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Juros"), "COD_GRUPO"] = "2"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Outras"), "COD_GRUPO"] = "3"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Investimentos"), "COD_GRUPO"] = "4"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Inversoes"), "COD_GRUPO"] = "5"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Amortizacao"), "COD_GRUPO"] = "6"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Reserva"), "COD_GRUPO"] = "9"

df.sample(10)
# %%
#===================================3===================================
df["RPPS"] = "NÃO"

codigos_rpps = [1801261, 2801261, 1800262, 2800262, 1802202, 2802202]

df.head()
#%%
df.loc[df["COD_FONTE_MAE"].isin(codigos_rpps), "RPPS"] = "SIM"
df.sample(10)

#%%
#===================================4===================================
df["COD_CATEGORIA"] = 4

codigo_categoria = ["1", "2", "3"]

df.head()

#%%
df.loc[df["COD_GRUPO"].isin(codigo_categoria), "COD_CATEGORIA"] = 3
df.sample(10)

#%%
#===================================5===================================
colunas = ["COD_CATEGORIA", "COD_GRUPO", "COD_MODALIDADE", "COD_ELEMENTO"]

#%%
for coluna in colunas:
    df[coluna] = df[coluna].astype(str) #.str.zfill(2)

#%%
df["COD_NATUREZA_ELEMENTO"] = df[colunas].agg("".join, axis=1)
df.head(10)

#%%
#===================================6===================================
padroes = '^(32|46|99|45..66)|^45909266$|^45909263$|^45..64$|^45909264$|^45..63$'

df["PRIMARIO"] = "SIM"

#%%
df.loc[df["COD_NATUREZA_ELEMENTO"].str.contains(padroes, na=False), "PRIMARIO"] = "NÃO"
df.sample(10)

#%%
df["PRIMARIO"].value_counts()

#%%
#===================================7===================================
df['TOTAL_PAGO'] = df['PAGO'] + df['PAGO_EXERCICIO_ANTERIOR']
df.sample(20)