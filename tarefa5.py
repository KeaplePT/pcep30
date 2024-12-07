#1
'''
print("Este código vai te mostrar uma matriz")

matriz = []
numero = 1
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(numero)
        numero += 1
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()
'''

#2
'''
print("Esta é a diagonal diagonal principal de uma matriz 4x4")
matriz = []
numero = 1
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(numero)
        numero += 1
    matriz.append(linha)

print("Elementos da diagonal principal:")
for i in range(4):
    print(matriz[i][i])
'''

#3
'''
print("Esta é a soma de elementos de uma matriz 2*3 fornecida por ti")

matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o número na posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento

print("Soma dos elementos:", soma)
'''

#4
'''
print("Esta é uma matriz 5*5")

matriz_identidade = []
for i in range(5):
    linha = []
    for j in range(5):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_identidade.append(linha)

print("Matriz identidade 5x5:")
for linha in matriz_identidade:
    for elemento in linha:
        print(elemento, end="\t")
    print()
'''

#5
'''
print("Este código vai mostrar a inversão das inhas de uma matriz 3*3")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matriz original:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()

nova_matriz = []
for i in range(len(matriz)-1, -1, -1):
    nova_matriz.append(matriz[i])

print("Matriz após inversão das linhas:")
for linha in nova_matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()
'''

#6
'''
print("Este código vai remover de uma linha de uma matriz 5*2")

matriz = []
for i in range(5):
    linha = []
    for j in range(2):
        numero = int(input(f"Digite o número para a posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)

print("Matriz original:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()

linha_remover = int(input("Digite um número de 1 a 5 para remover a linha correspondente: ")) - 1
matriz.pop(linha_remover)

print("Matriz após remoção:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()
'''

#7
'''
print("Este codigo vai mostrar qual o maior numero de uma matriz 4*3")

matriz = []
for i in range(5):
    linha = []
    for j in range(2):
        numero = int(input(f"Digite o número para a posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)

print("Matriz original:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()

linha_remover = int(input("Digite um número de 1 a 5 para remover a linha correspondente: ")) - 1
matriz.pop(linha_remover)

print("Matriz após remoção:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()
'''

#8
'''
print("Este codigo vai mostrar a matriz transposta da forma pedida no exercicio")

matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o número na posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)

matriz_transposta = []
for j in range(3):
    nova_linha = []
    for i in range(2):
        nova_linha.append(matriz[i][j])
    matriz_transposta.append(nova_linha)

print("Matriz transposta:")
for linha in matriz_transposta:
    for elemento in linha:
        print(elemento, end="\t")
    print()


#teste de defs
'''
'''
num1 = int(input("Indica me um numero seu roto: "))
num2 = int(input("Indica me um segundo numero seu ratoeira: "))
operacao = (input("Indica qual a operação que queres efetuar: ""+ - * /"" : " ))


def soma():
    num_soma = num1 + num2
    print(num1, "somado com", num2, "é igual a", num_soma)

def subtrair():
    num_subtrair = num1 - num2
    print(num1, "subtraido com", num2, "é igual a", num_subtrair)

def multiplicar():
    num_multiplicar = num1 * num2
    print(num1, "multiplicado com", num2, "é igual a", num_multiplicar)

def dividir():
    num_dividir = num1 / num2
    print(num1, "dividido com", num2, "é igual a", int(num_dividir))

if operacao == "+":
    soma()
if operacao == "-":
    subtrair()
if operacao == "*":
    multiplicar()
if operacao == "/":
    dividir()

'''

'''
def nome_completo(nome,sobrenome):
    return nome,sobrenome

nome_completo = input("Sotor dá-me o teuu nome e ultimo nome: ")

print(nome_completo)
'''

def media(num1, num2):
    return (num1 + num2) / 2

num1 = float(input("Sotor manda me aí dois numeros para eu fazer a média, manda aí o primeiro: "))
num2 = float(input("Atira aí com força o segundo: "))

print(media(num1, num2))