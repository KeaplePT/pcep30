#1
#Uma estrutura de repetição é um while, e ele repete um conjunto de instruções definida por nós.

#2
'''
print("este programa vai dizer quais são os números pares de 0 a 20.\nEles são:")

for num in range(0,21):
    if num % 2 == 0:
        print(num)
'''

#3

'''
print("Este programa vai dizer a listagens de números de 1 a 100:\n")

i = 0 

while i <= 100:
    print(i, end=", ")
    i = i + 1
print("É esta a listagem!")

'''

#4
'''
for num in range(11,0,-1):
    print(num - 1, end=" ")

'''

#5
'''
for num in range(0,21):
    num1 = num + 1
    if num1 % 3 == 0:
        continue
    print(num1)
'''

#6
'''
num = 1

while num <= 50:
    if num % 7 == 0:
        print("O primeiro número divisível por 7 é", num)
        break
    num += 1
'''

#7 
'''
for num in range(1,16):
    if num % 2 != 0:
        print(num)
        num + 1

'''

#8
'''
num = 0

while num <= 15:
    if num == 9:
        break
    print(num)
    num = num + 1

'''

#9
'''
num = int(input("Insira um número à sua escolha: "))

digits = 0

num = abs(num)

if num == 0:
    digits = 1

while num > 1:
    num //= 10
    digits += 1

print("O número tem apenas", digits,"digito/s")
'''

#10
'''
num1 = int(input("Introduza dois números que quer somar, se quiseres parar o programa, insira um número negativo: \n"))
num2 = int(input("Insira o segundo número:\n"))

num3 = num1 + num2

while int(num1) >= 0 or int(num2) >= 0:
    print(num1 + num2)
    num1 = int(input("Insere outro primeiro número:\n"))
    num2 = int(input("Insere outro segundo numero:\n"))
    if int(num1) < 0 or int(num2) < 0:
        break

print("Inseriste um número negativo, por isso adeus")
'''

#12
'''
pergunta = input("Ex.mo, já chegamos? Diga Sim ou Não: ")

while pergunta != "Sim":
    if pergunta == "Não":
        print("Parece que ainda não chegamos.")
    pergunta = input("E agora já chegamos? Diga Sim ou Não: ")

print("Finalmente pah!")
'''

#13 
'''
perfeitos = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

n = int(input("Ex.mo camarada, diga por favor um numero natural, eu dir-lhe-ei a lista até ao número que quer:\n"))

while n <= 0:
    input("Insere um número maior do que 0:\n")

print(perfeitos[:n])
'''

#14

# Solicita ao usuário um número natural N
N = int(input("Digite um número natural N: "))

# Lista para armazenar os quadrados perfeitos que não são múltiplos de 4
quadrados_nao_multiplos_de_4 = []

# Usando um ciclo for para calcular os quadrados perfeitos
for i in range(1, N + 1):
    quadrado = i ** 2
    if quadrado % 4 != 0:  # Verifica se não é múltiplo de 4
        quadrados_nao_multiplos_de_4.append(quadrado)

# Apresenta os quadrados perfeitos que não são múltiplos de 4
print("Os primeiros", N, "quadrados perfeitos que não são múltiplos de 4 são:", quadrados_nao_multiplos_de_4)

#precisei de copiar do chatgpt este ultimo, considero este o meu  limite, preciso de descansar mais um pouco.



