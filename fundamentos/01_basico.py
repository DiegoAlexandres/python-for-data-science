#%%
# Nível Básico (Foco em if/else e Listas)
# Exercício 1: Classificação de Idade
# Objetivo: Praticar a estrutura if, elif e else para tomar decisões baseadas em diferentes faixas de valores.
idade = 25

if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 65:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Com {idade} anos, a pessoa é classificada como: {categoria}")

# Explicação
# O código avalia a variável idade em sequência:
# if idade < 13: Se a idade for menor que 13, categoria se torna "Criança" e o bloco termina.
# elif idade < 18: Se a primeira condição for falsa, ele testa se a idade é menor que 18. Em caso afirmativo, categoria vira "Adolescente".
# elif idade < 65: Se as anteriores forem falsas, testa se a idade é menor que 65.
# else: Se nenhuma das condições acima for verdadeira, o código executa o bloco else, classificando como "Idoso".

#%%
# Exercício 2: Verificando Números Pares em uma Lista
# Objetivo: Combinar um loop for para percorrer uma lista com um if/else para analisar cada item.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Analisando a lista de números:")
for numero in numeros:
    # O operador '%' (módulo) retorna o resto de uma divisão.
    # Se o resto da divisão por 2 for 0, o número é par.
    if numero % 2 == 0:
        print(f"- O número {numero} é PAR.")
    else:
        print(f"- O número {numero} é ÍMPAR.")
        
# Explicação
# for numero in numeros:: O loop for passa por cada item da lista numeros, um de cada vez. A cada passagem, o item atual é armazenado na variável numero.
# if numero % 2 == 0:: Dentro do loop, esta condição verifica se o número atual é par. O operador módulo (%) é perfeito para isso.
# O if/else então imprime a mensagem apropriada para cada número da lista.


#%%
# Exercício 3: Média para Aprovação de Aluno
# Objetivo: Usar operadores lógicos (and) dentro de uma estrutura if/elif/else.
nota_final = 8.5
frequencia = 0.90  # Representa 90%

if nota_final >= 7.0 and frequencia >= 0.75:
    status = "Aprovado"
elif nota_final >= 5.0 and frequencia >= 0.75:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f"O status do aluno é: {status}")

# Explicação
# Este exemplo usa o operador and para garantir que ambas as condições sejam verdadeiras.
# Para ser "Aprovado", a nota precisa ser maior ou igual a 7 E a frequência maior ou igual a 75%.
# Se isso falhar, o elif verifica a condição para "Recuperação".
# Se nenhuma das condições de aprovação ou recuperação for atendida, o aluno é "Reprovado".