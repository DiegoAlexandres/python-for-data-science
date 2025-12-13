#%%
def calcular_dobro(numero):
    resultado = numero * 2
    return resultado

#%%
valor = calcular_dobro(50)
valor

#%%
def verificar_meta(vendas, meta):
    if vendas >= meta:
        return "Meta Batida!"
    else:
        falta = meta - vendas
        return f"Não bateu. Faltam R$ {falta}"

#%%
resultado_jan = verificar_meta(15000, 20000)
resultado_jan


# #%%
# def calcular_yoy_seguro(linha):
#     # Extrai os valores da linha que está sendo lida agora
#     valor_2024 = linha["Resultado Primário 2024"]
#     valor_2025 = linha["Resultado Primário 2025"]
    
#     # 1. Proteção: Se 2024 for zero, retorna 0 para não quebrar
#     if valor_2024 == 0:
#         return 0.0
    
#     # 2. Proteção: Se 2025 for zero (dados futuros), retorna 0 ou NaN
#     if valor_2025 == 0:
#         return 0.0

#     # 3. Cálculo (usando abs() no divisor para corrigir o problema dos negativos)
#     variacao = ((valor_2025 - valor_2024) / abs(valor_2024)) * 100
    
#     return variacao

# #%%
# # Supondo que seu DataFrame se chame 'df' ou 'tabela_final'

# # Cria a nova coluna 'Variação % YoY' aplicando a função
# df["Variação % YoY"] = df.apply(calcular_yoy_seguro, axis=1)

# # Visualizar o resultado
# print(df)