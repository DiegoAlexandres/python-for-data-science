#%%
import pandas as pd

#%%
pd.options.display.float_format = '{:,.2f}'.format

#%%
df = pd.read_excel("../dados/RazaoContasBanco_14102.xlsx")
df.head()

#%%
df.info()

#%%
#==============================Etapa 0==============================
colunas = ["COCONTACONTABIL", "DALANCAMENTO"]

df[colunas] = df[colunas].astype(str)

#%%
#==============================Etapa 1==============================
df["FR"] = df["COCONTACORRENTE"].str.slice(1, 8)
df.head()

#%%
filtro = df["COCONTACONTABIL"] == "1111102050000"

#%%
filtro.value_counts()

#%%
df.loc[filtro, "FR"] = df.loc[filtro, "COCONTACORRENTE"].str.slice(7, 14)
df.tail()

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 python
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 excel

#%%
#==============================Etapa 2==============================
df["BANCO"] = df["COCONTACORRENTE"].str.slice(-14)
df.head()

#%%
df.loc[df["COCONTACONTABIL"] == "1111102010000", "BANCO"] = "23703739162000"
df.head()

#%%
contas = ["1111130010000", "1111130020000"]

df.loc[df["COCONTACONTABIL"].isin(contas), "BANCO"] = "Agente Arrecadador"
df.tail()

#==============================Etapa 4==============================
df["DALANCAMENTO"] = df["DALANCAMENTO"].str.replace("00$", "01", regex=True)
df.head()

#%%
#==============================Etapa 3==============================
df["DALANCAMENTO"] = pd.to_datetime(df["DALANCAMENTO"], format="%Y%m%d", errors="coerce")
df.head()

#%%
#==============================Etapa 5 a 9==============================
colunas_2 = ["UGDOC", "GESTAODOC", "NUDOCUMENTO", "COEVENTO", "NOEVENTO"]
df[colunas_2] = df[colunas_2].astype(str)

#%%
df[colunas_2] = df[colunas_2].replace("nan", "0000").fillna("0000")
df.head()

#%%
df["UGDOC"].value_counts()

#==============================Etapa 10==============================
df["ANO"] = df["DALANCAMENTO"].dt.year
df.head()

#%%
fr_25 = df[df["ANO"] == 2025].groupby("FR")["VALANCAMENTO"].sum().reset_index()
fr_25

#%%
saldo_bancario_25 = fr_25["VALANCAMENTO"].sum()
saldo_bancario_25

#%%
#==============================Etapa 11==============================
filtro_dia_31 = df[df["DALANCAMENTO"] == "2025-01-31"]
filtro_dia_31

#%%
fluxo_dia_31 = filtro_dia_31.groupby("FR")["VALANCAMENTO"].sum().reset_index()
fluxo_dia_31 = fluxo_dia_31["VALANCAMENTO"]

fluxo_dia_31

#%%
fr_25["Saldo Inicial"] = saldo_bancario_25 - fluxo_dia_31

#%%
fr_25

#%%
saldo_bancario_25

#Saldo Final - Qual o saldo final do dia 20? Res: Primeiro dia do ano até o dia do filtro (Dia 20) - classificado FR
#Saldo Inicial é Saldo Final - 1 dia (Até dia 19) - classificado FR

#Selecionando dia 20
#Saldo inicial (Dia anterior - (Dia 1 a 19)) - Fluxo de Caixa (Dia Selecionado (Só dia 20)) - Saldo Final (Saldo do dia Selecionado (Dia 1 a 20))

#%%
#==============================Etapa Análise Dinamica==============================
#Define o escopo da analise
dia_analise = pd.Timestamp("2025-01-31")
dia_analise

#%%
#Novo dataframe com o escopo da análise
df_escopo = df[
    (df["DALANCAMENTO"].dt.year == 2025) & 
    (df["DALANCAMENTO"] <= dia_analise)
].copy()

df_escopo

#%%
#Validando o dados do dia 01 ate dia 20
df_escopo["DALANCAMENTO"].value_counts().sort_index() # Pordão ascending=True





#%%
#Calcular SALDO INICIAL (Acumulado do ano até o dia anterior, dia 19)
saldo_inicial = df_escopo[df_escopo["DALANCAMENTO"] < dia_analise].groupby("FR")["VALANCAMENTO"].sum().reset_index(name="Saldo Inicial")
saldo_inicial

#%%
#Calcular FLUXO DE CAIXA (Apenas movimentações do dia 20)
fluxo_caixa = df_escopo[df_escopo["DALANCAMENTO"] == dia_analise].groupby("FR")["VALANCAMENTO"].sum().reset_index(name="Fluxo de Caixa")
fluxo_caixa

#%%
#Calcular SALDO FINAL (Acumulado do ano até o dia 20)
saldo_final = df_escopo.groupby("FR")["VALANCAMENTO"].sum().reset_index(name="Saldo Final")
saldo_final

#%%
#Primeiro pegamos todos os FRs únicos que tiveram movimento até o dia 20
frs_unicos = pd.DataFrame(df_escopo["FR"].unique(), columns=["FR"])
frs_unicos

#Se precisar de todos os FR do ano
#frs_existentes_2025 = df[df["ANO"] == 2025]["FR"].unique()
#frs_unicos = pd.DataFrame(frs_existentes_2025, columns=["FR"])

#%%
#Fazemos o merge (junção) com as tabelas calculadas
relatorio = frs_unicos.merge(saldo_inicial, on="FR", how="left")
relatorio = relatorio.merge(fluxo_caixa, on="FR", how="left")
relatorio = relatorio.merge(saldo_final, on="FR", how="left")

#%%
relatorio = relatorio.fillna(0)

#%%
relatorio

#%%
#==============================Linha de total==============================
colunas_relatorios = ["Saldo Inicial", "Fluxo de Caixa", "Saldo Final"]

#%%
somas = relatorio[colunas_relatorios].sum()

#%%
linha_total = pd.DataFrame(somas).T #O .T é uma abreviação para Transpor (Transpose)
linha_total

#%%
linha_total["FR"] = "Total"

#%%
relatorio_final = pd.concat([relatorio, linha_total], ignore_index=True)
relatorio_final

#%%
#==============================Linha de total forma já utilizada em DESPESAS==============================
total_saldo_inicial = relatorio["Saldo Inicial"].sum()
total_fluxo = relatorio["Fluxo de Caixa"].sum()
total_saldo_final = relatorio["Saldo Final"].sum()

#%%
# Usamos o len(relatorio) para criar um índice numérico novo (ex: linha 10)
relatorio.loc[len(relatorio)] = ["Total_Diego", total_saldo_inicial, total_fluxo, total_saldo_final]

#%%
relatorio

#%%
#relatorio_final = relatorio_final.drop(87)

#%%
relatorio_final

#%%
#==============================Validação==============================
#Validação (Prova Real): Saldo Inicial + Fluxo deve ser igual ao Saldo Final
relatorio["Validacao"] = (relatorio["Saldo Inicial"] + relatorio["Fluxo de Caixa"]) - relatorio["Saldo Final"]
relatorio

#%%
relatorio[relatorio["Validacao"].abs() > 0.01] # Mostra apenas se houver erro matemático

#%%
#relatorio = relatorio.drop(columns=["Validacao"])

#%%
def milhar(milhar):
    return milhar.style.format(
    precision=2,
    decimal=",",
    thousands="."
)
    
#%%
milhar(relatorio_final)


#%%
#==============================Função Contass Bancarias==============================
