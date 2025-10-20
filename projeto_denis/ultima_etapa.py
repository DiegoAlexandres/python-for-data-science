#######################################################-----8-----#########################################################

filtro = df[(df['RPPS'] == 'Não') & (df['PRIMARIO'] == 'Sim')].copy()
filtro

#%%
filtro['ano'] = filtro['DATA'].dt.year
filtro

#%%
filtro['mes_num'] = filtro['DATA'].dt.month
filtro

#%%
resumo = filtro.groupby(['ano', 'mes_num'])['TOTAL_PAGO'].sum().reset_index()
resumo

#%%
tabela = resumo.pivot_table(index='mes_num', columns='ano', values='TOTAL_PAGO').fillna(0)
tabela
#%%
# AJUSTE: Renomeando a coluna de variação para 'Var. R$'
tabela['Var. R$'] = tabela[2025] - tabela[2024]
tabela

#%%
tabela['Var. %'] = ((tabela['Var. R$'] / tabela[2024].replace(0, float('nan'))) * 100).round(2)
tabela

#%%
meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun', 
         7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}

#%%
tabela.index = tabela.index.map(meses)
tabela.index

#%%
tabela = tabela.rename_axis('Mês')
tabela

#%%
# AJUSTE: Reordenando as colunas para corresponder ao exemplo
tabela_final = tabela[[2024, 2025, 'Var. %', 'Var. R$']]
tabela_final

#%%
# AJUSTE NOVO: Adicionando a linha de "Total"
total_2024 = tabela_final[2024].sum()

#%%
total_2025 = tabela_final[2025].sum()

#%%
total_variacao_rs = tabela_final['Var. R$'].sum()

#%%
# O percentual total é calculado sobre os totais, não somado
total_var_pct = ((total_variacao_rs / total_2024) * 100).round(2) 

#%%
tabela_final.loc['Total'] = [total_2024, total_2025, total_var_pct, total_variacao_rs]

tabela_final