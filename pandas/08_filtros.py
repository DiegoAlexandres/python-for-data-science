#%%
import pandas as pd
import numpy as np

#%%
dados = {
        "data": ["01/01/2025", "02/01/2025", "03/01/2025", "04/01/2025", "05/01/2025"],
        "valor": [100, 200, 300, 400, 500],
        "categoria": ["A", "B", "A", "B", "A"]
        }

#%%
df = pd.DataFrame(dados)
df

#%%
df.info()

#%%
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df.info()