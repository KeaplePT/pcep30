#1 
'''
def palavra(palavra):
    return len(palavra)

palavra = input("Camarada, gostaria por ventura escrever me uma palavra?: ")

while palavra.isdigit():
    print("Exmo digitou um numero em vez de uma palavra, prepare-se para ficar a noite toda a empurrar o mundo")
    palavra = input("Vá, escreva outra vez: ")
    
print("A palavra que inseriste tem", len(palavra), "letras.")
'''

#2
'''
def palavra(palavra):
    return palavra

palavra = input("Escreve uma palavra sotor: ")
print(palavra)

'''

#3
'''
def numeros(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


num1 = int(input("1º Número: "))
num2 = int(input("2º Número: "))

print(numeros(num1,num2))
'''

#4
'''
def matriz_lista(matriz):
    comprimento_linha = len(matriz[0])  
    return all(
        len(linha) == comprimento_linha and all(isinstance(x, int) for x in linha)
        for linha in matriz
    )

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("É uma matriz válida?\n", matriz_lista(matriz))
'''

#5
'''
def pares(lista):
    return [x for x in lista if x % 2 == 0]

lista = [int(x) for x in input("Manda para aí numero separados por espaço: ").split()]
print("Os números pares são:", pares(lista))
'''
#6
'''
def existe_substring(string, substring):
    n, m = len(string), len(substring)
    for i in range(n - m + 1):
        if string[i:i + m] == substring:
            return True
    return False

string = input("Escreve uma palavra principal: ")
substring = input("Escreve aí uma palavra mais pequena pah: ")
print("Encontrou uma substring?", existe_substring(string, substring))
'''

#7
'''
def existe_substring(string, substring):
    n, m = len(string), len(substring)
    for i in range(n - m + 1):
        if string[i:i + m] == substring:
            return True
    return False

def filtra_strings(lista, pesquisa):
    return [string for string in lista if existe_substring(string, pesquisa)]

lista = input("Mete ai palavras separadas por espaço: ").split()
pesquisa = input("Por qual parte de palavra queres pesquisar: ")
print("Strings que contêm essa parte da palavra:", filtra_strings(lista, pesquisa))

'''
#8
'''
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Sotor diga ai um numero para verificar se é primo: "))
print("É primo?",eh_primo(n))
'''

#9
'''
def maior_numero(lista):
    maior = lista[0]
    for num in lista[1:]:
        if num > maior:
            maior = num
    return maior

# Teste
lista = [int(x) for x in input("Escreve numeros separados por espaço: ").split()]
print("O maior número desta listagem é:", maior_numero(lista))
'''
#10
'''
def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(x) for x in linha))

# Teste
matriz = [
    [int(x) for x in input(f"Escreve aí uma linha {i+1} separada por espaço: ").split()]
    for i in range(3)
]
print("Matriz:")
imprime_matriz(matriz)
'''

#11
'''
def eleva_ao_quadrado(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2

# Teste
lista = [int(x) for x in input("Exmo escreve aí numeros separados por espaço: ").split()]
eleva_ao_quadrado(lista)
print("Todos os numeros dessa lista ao quadrado:", lista)
'''

#12
'''
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def eleva_ao_quadrado(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def menu():
    print("Escolha uma destas opções exmo camarada:")
    print("1 - Verificar se um número é primo")
    print("2 - Elevar ao quadrado uma lista")
    print("3 - Calcular o Fibonacci, para ver a que preço vai fazer pullback e entrar na trade")

    escolha = input("Diz o número da opção: ")
    if escolha == '1':
        n = int(input("Escreve um número: "))
        print("É primo?", eh_primo(n))
    elif escolha == '2':
        lista = [int(x) for x in input("Escreve os números separados por espaço: ").split()]
        eleva_ao_quadrado(lista)
        print("Lista ao quadrado:", lista)
    elif escolha == '3':
        n = int(input("Escreve um índice Fibonacci: "))
        print("Fibonacci:", fibonacci(n))
    else:
        print("Exmo essa opção não existe!")

menu()
'''

#13
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Teste
n = int(input("Qual o indique que queres calcular no Sotor Fibonacci: "))
print("Fibonacci:", fibonacci(n))
'''

#14
'''
def moda(lista):
    contagem = {}
    for numero in lista:
        contagem[numero] = contagem.get(numero, 0) + 1
    return max(contagem, key=contagem.get)

# Teste
lista = [int(x) for x in input("Escreve numeros separados por espaço, novamente já estou farto de fazer isto: ").split()]
print("A moda da lista é:", moda(lista))
'''

# Tentativa de jogo da forca

import time

# Lista de palavras
palavras = ["python", "programacao", "jogo", "computador", "teclado"]

# Selecionar a palavra baseada no tempo atual
indice = int(str(time.time()).split(".")[1]) % len(palavras)
palavra_escolhida = palavras[indice].lower()

letras_descobertas = ["_" for _ in palavra_escolhida]
tentativas_restantes = 3
letras_erradas = []

print("Bem-vindo ao jogo da forca!")

# Jogo da forca
while tentativas_restantes > 0:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Tentativas restantes:", tentativas_restantes)
    print("Letras erradas:", ", ".join(letras_erradas))
    
    letra = input("Adivinhe uma letra: ").lower()

    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra_escolhida:
        for i, char in enumerate(palavra_escolhida):
            if char == letra:
                letras_descobertas[i] = letra
        print("Boa! A letra está na palavra.")
    else:
        letras_erradas.append(letra)
        tentativas_restantes -= 1
        print("Erro! Essa letra não está na palavra.")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você acertou a palavra:", palavra_escolhida)
        break
else:
    print("\nVocê perdeu! A palavra era:", palavra_escolhida)



