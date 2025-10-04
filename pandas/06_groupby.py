#%%
import pandas as pd
import numpy as np

#%%
dclientes = pd.read_excel("../dados/dClientes.xlsx")
dcategorias = pd.read_excel("../dados/dCategorias.xlsx")
fcontas_receber = pd.read_excel("../dados/fContasReceber.xlsx")

#%%
dcategorias = dcategorias.rename(columns={"id_Categoria_Nivel_3": "CodCategoria"})
dcategorias.head()

#%%
colunas = ["DataCompetencia", "DataVencimento", "DataPagamento"]

for coluna in colunas:
    fcontas_receber[coluna] = pd.to_datetime(fcontas_receber[coluna], errors="coerce")

fcontas_receber.head()

#%%
df = fcontas_receber.merge(dcategorias, on="CodCategoria", how="left")
df.head()

#%%
df_full = df.merge(dclientes, on="CodCliente", how="left")
df_full.head()

### Perguntas de negócios sobre os dados full

#%%
#Qual foi o faturamento total já recebido neste conjunto de dados?
status_recebido = df_full["Status"] == "RECEBIDO"  

df_full[status_recebido]["Valor"].sum()

# Resposta: np.float64(267030.93000000005)

