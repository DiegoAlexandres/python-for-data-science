#%%
import pandas as pd

pd.options.display.float_format = "{:.2f}".format

#%%
receitas = pd.read_excel("receitas.xlsx")
receitas

#%%
despesas = pd.read_excel("despesas.xlsx")
despesas

#%%
despesas = despesas.rename(columns={"VAR $": "VAR R$", "VAR. %": "VAR %"})
despesas

#%%
df = pd.merge(receitas, despesas, on="MES", how="left", suffixes=(" RECEITA", " DESPESAS"))
df