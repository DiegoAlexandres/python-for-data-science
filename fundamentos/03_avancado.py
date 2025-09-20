#%%
# Nível Avançado (Foco em Funções def e while)
# Exercício 7: Função de Calculadora Simples
# Objetivo: Encapsular uma lógica if/elif/else dentro de uma função (def) que pode ser reutilizada.
def calculadora(num1, num2, operador):
    """Realiza uma operação matemática simples entre dois números."""
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return num1 / num2
    else:
        return "Operador inválido. Use '+', '-', '*' ou '/'."

# Testando a função
resultado1 = calculadora(10, 5, '+')
resultado2 = calculadora(10, 0, '/')
print(f"10 + 5 = {resultado1}")
print(f"10 / 0 = {resultado2}")

# Explicação
# def calculadora(...): Definimos uma função chamada calculadora que aceita três argumentos (num1, num2, operador).
# if/elif/else: A lógica interna verifica qual operador foi passado e executa a operação correspondente.
# return: A palavra-chave return envia o resultado do cálculo de volta para onde a função foi chamada. Se um operador inválido for usado, ela retorna uma mensagem de erro. Incluímos uma verificação especial para a divisão por zero.

#%%
# Exercício 8: Jogo de Adivinhação com while
# Objetivo: Usar um loop while para repetir uma ação até que uma condição específica seja atendida.
import random

numero_secreto = random.randint(1, 20)
palpite = 0

print("Jogo de Adivinhação! Tente adivinhar um número entre 1 e 20.")

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")

print(f"Parabéns! Você acertou. O número era {numero_secreto}.")


# Explicação
# import random: Importamos a biblioteca random para gerar um número aleatório.
# while palpite != numero_secreto:: O loop while continuará executando enquanto o palpite do usuário for diferente do número secreto.
# input(): A cada volta, pedimos um novo palpite ao usuário.
# if/elif: Dentro do loop, damos dicas se o palpite foi alto ou baixo.
# Quando o usuário finalmente acerta, a condição palpite != numero_secreto se torna False, e o loop termina, exibindo a mensagem de parabéns.


#%%
# Exercício 9: Validação de Entrada com while e try/except
# Objetivo: Um uso prático do while: forçar o usuário a digitar um dado válido antes de continuar.
while True: # Inicia um loop infinito
    try:
        idade_str = input("Por favor, digite sua idade (apenas números): ")
        idade_num = int(idade_str) # Tenta converter o texto para número
        
        if 0 < idade_num < 120:
            break # Se for um número válido e dentro do range, quebra o loop
        else:
            print("Por favor, digite uma idade realista.")

    except ValueError:
        # Se a conversão para int() falhar (ex: usuário digitou "abc")
        print("Entrada inválida. Por favor, digite apenas números.")

print(f"Obrigado! Sua idade é {idade_num}.")

# Explicação
# while True:: Criamos um loop que, a princípio, rodaria para sempre. A única forma de sair é com um break.
# try...except: Este é um bloco de tratamento de erros.
# O código dentro do try é executado. Tentamos converter a entrada do usuário para um int.
# Se o usuário digitar algo que não é um número (ex: "trinta"), a conversão int() dará um ValueError. O bloco except captura esse erro específico e imprime uma mensagem amigável, em vez de o programa quebrar.
# if 0 < idade_num < 120:: Se a conversão for bem-sucedida, verificamos se o número está em um intervalo razoável.
# break: Se a entrada for um número e estiver no intervalo válido, o break é executado, quebrando o loop while, e o programa continua. Se não, uma mensagem de erro é exibida e o loop recomeça, pedindo a entrada novamente.