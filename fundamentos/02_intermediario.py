#%%
# Nível Intermediário (Foco em Loops for e Dicionários)
# Exercício 4: Contando Categorias de Produtos
# Objetivo: Percorrer um dicionário e usar outro dicionário como um contador.
produtos = {
    'Caneta': 'Papelaria',
    'Caderno': 'Papelaria',
    'Teclado': 'Eletrônicos',
    'Mouse': 'Eletrônicos',
    'Lápis': 'Papelaria'
}

contagem_categorias = {}

# .items() permite percorrer as chaves e os valores do dicionário ao mesmo tempo
for produto, categoria in produtos.items():
    if categoria in contagem_categorias:
        # Se a categoria já existe no nosso contador, incrementa 1
        contagem_categorias[categoria] += 1
    else:
        # Se for a primeira vez que vemos a categoria, adiciona ao contador com valor 1
        contagem_categorias[categoria] = 1

print("Contagem de produtos por categoria:")
print(contagem_categorias)


# Explicação
# contagem_categorias = {}: Iniciamos um dicionário vazio para armazenar nossa contagem.
# for produto, categoria in produtos.items():: O método .items() é a melhor forma de iterar sobre um dicionário, pois ele nos dá a chave (produto) e o valor (categoria) a cada passo.
# if categoria in contagem_categorias:: Verificamos se a categoria do produto atual já é uma chave no nosso dicionário contador.
# Se sim (+= 1), incrementamos a contagem. Se não (= 1), criamos a chave e iniciamos a contagem em 1.


#%%
# Exercício 5: Buscando Dados em uma Lista de Dicionários
# Objetivo: Simular uma busca em dados estruturados, como uma resposta de API em JSON.
lista_usuarios = [
    {'id': 1, 'nome': 'Ana', 'email': 'ana@exemplo.com'},
    {'id': 2, 'nome': 'Bruno', 'email': 'bruno@exemplo.com'},
    {'id': 3, 'nome': 'Carla', 'email': 'carla@exemplo.com'}
]

nome_busca = 'Bruno'
usuario_encontrado = None

for usuario in lista_usuarios:
    if usuario['nome'] == nome_busca:
        usuario_encontrado = usuario
        break # Encontramos o que queríamos, podemos parar o loop

if usuario_encontrado:
    print(f"Usuário encontrado: {usuario_encontrado}")
else:
    print(f"Usuário '{nome_busca}' não encontrado.")

# Explicação
# for usuario in lista_usuarios:: Iteramos sobre a lista. A cada passo, a variável usuario contém um dicionário completo (ex: {'id': 1, ...}).
# if usuario['nome'] == nome_busca:: Acessamos o valor da chave 'nome' no dicionário atual e comparamos com o nome que estamos buscando.
# usuario_encontrado = usuario: Se encontrarmos, guardamos o dicionário inteiro na variável usuario_encontrado.
# break: Uma otimização importante. Assim que encontramos o usuário, o break interrompe o loop imediatamente, pois não precisamos continuar procurando.


#%%
# Exercício 6: Criando um Dicionário a partir de Duas Listas
# Objetivo: Praticar a criação de um dicionário combinando duas listas de mesmo tamanho.
chaves = ['nome', 'idade', 'cidade']
valores = ['Diego', 30, 'São Paulo']

dicionario_final = {}

# A função zip() combina as duas listas, elemento por elemento
for chave, valor in zip(chaves, valores):
    dicionario_final[chave] = valor

print("Dicionário criado a partir das listas:")
print(dicionario_final)

# Explicação
# zip(chaves, valores): A função zip é uma ferramenta elegante do Python. Ela "zera" duas ou more listas, criando pares de elementos correspondentes a cada iteração do loop. Na primeira volta, chave é 'nome' e valor é 'Diego', e assim por diante.
# dicionario_final[chave] = valor: Dentro do loop, simplesmente criamos uma nova entrada no nosso dicionário usando o par chave/valor fornecido pelo zip.
