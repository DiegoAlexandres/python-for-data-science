#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
from receitas import receitas
from despesas import tabela

#%%
receitas

#%%
despesas = tabela
despesas

#%%
despesas = despesas.rename(columns={"VAR $": "VAR R$", "VAR. %": "VAR %"})
despesas

#%%
df = pd.merge(receitas, despesas, on="MES", how="left", suffixes=(" RECEITAS", " DESPESAS"))
df

#%%
df["SALDO"] = df["2025_RECEITAS"] - df["2025_DESPESAS"]
df
