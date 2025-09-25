#%%
import pandas as pd
#%%
# Importando dados de fontes externas
contas_receber = pd.read_excel("../dados/fContasReceber.xlsx")
contas_receber.head()

#%%
# Convertendo o tipo das colunas de datas para datetime
colunas = ['DataCompetencia', 'DataVencimento', 'DataPagamento']

for coluna in colunas:
  contas_receber[coluna] = pd.to_datetime(contas_receber[coluna], errors='coerce')

contas_receber.head()

#%%
# Objetivo: Descobrir o valor total recebido em cada mês, para entender a sazonalidade do negócio.
# Filtrar apenas as contas com status 'RECEBIDO'
recebidos = contas_receber[contas_receber['Status'] == 'RECEBIDO'].copy()
recebidos

#%%
# Agrupar pela coluna de data de pagamento (extraindo o mês) e somar os valores
faturamento_mensal = recebidos.groupby(recebidos['DataPagamento'].dt.month)['Valor'].sum()
faturamento_mensal

#%%
# (Desafio) Ordenar o resultado para ver os melhores meses
faturamento_mensal_ordenado = faturamento_mensal.sort_values(ascending=False)

print("--- Faturamento Total por Mês ---")
print(faturamento_mensal_ordenado)


#%%
# Objetivo: Encontrar transações que atendam a mais de um critério (neste caso, pagamentos de alto valor já recebidos).
# Definir a condição 1: Status deve ser 'RECEBIDO'
condicao_status = contas_receber['Status'] == 'RECEBIDO'

#%%
# Definir a condição 2: Valor deve ser maior que 1000
condicao_valor = contas_receber['Valor'] > 1000

#%%
# Aplicar o filtro combinado usando o operador '&' (E)
alto_valor_recebido = contas_receber[condicao_status & condicao_valor]

print("\n--- Contas de Alto Valor Recebidas ---")
print(alto_valor_recebido[['DataPagamento', 'CodCliente', 'Valor', 'Status']])

#%%
# Objetivo: Criar uma nova coluna DiasDeAtraso para identificar pagamentos feitos após o vencimento.
# Criar uma cópia para não alterar o DataFrame original diretamente na aula
df_atraso = contas_receber.copy()

# Calcular a diferença entre a data de pagamento e a data de vencimento
df_atraso['DiasDeAtraso'] = (df_atraso['DataPagamento'] - df_atraso['DataVencimento']).dt.days

print("\n--- Análise de Atraso de Pagamento ---")
# Exibir colunas relevantes, incluindo a nova coluna
print(df_atraso[['DataVencimento', 'DataPagamento', 'DiasDeAtraso', 'Status']].head())


#%%
# Importando os dados da tabela de clientes
clientes = pd.read_excel("../dados/dClientes.xlsx")
clientes.head()

#%%
# Objetivo: Identificar os clientes mais valiosos com base no total de valor pago.
# Juntar as tabelas para ter acesso ao nome do cliente
dados_completos = pd.merge(contas_receber, clientes, on='CodCliente', how='left')
dados_completos

#%%
# Analisando quais clientes compraram no mes de maio de 2025
compras_em_maio = contas_receber[contas_receber['DataPagamento'].dt.month == 5]
merge = pd.merge(compras_em_maio, clientes, on='CodCliente', how='left')
merge.head()

#%%
dados_completos['Status'].unique()

#%%
# Filtrar apenas as transações recebidas
recebidos_completos = dados_completos[dados_completos['Status'] == 'RECEBIDO']
recebidos_completos

#%%
# Filtrar apenas as transações pendente
recebidos_completos = dados_completos[dados_completos['Status'] == 'PENDENTE']
recebidos_completos

#%%
# Filtrar apenas as transações atrasado
recebidos_completos = dados_completos[dados_completos['Status'] == 'ATRASADO']
recebidos_completos

#%%
# Agrupar por nome de cliente, somar o valor e pegar os 5 maiores
top_5_clientes = recebidos_completos.groupby('Cliente/Fornecedor')['Valor'].sum().nlargest(5)

print("\n--- Top 5 Clientes por Faturamento ---")
print(top_5_clientes)

