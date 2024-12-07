'''
#1
nome = input("Diz me o teu nome:\n")
print("Olá", nome, "bem vindo a Programação!")
'''

'''
#2
cor = input("Qual a tua cor favorita?\n")
print("A tua cor favorita é", cor)

'''
#3
'''
nome = input("Qual o teu nome:\n")
idade = input("Qual a tua idade:\n")
cidade = input("Aonde moras:\n")

print("O teu nome é", nome, "tens", idade, "anos e moras em,", cidade)
'''

#5
'''
print("Calculador de Médias\n")

print("Indica 3 notas")
num1 = int(input("1ª nota: "))
num2 = int(input("2ª nota: "))
num3 = int(input("3ª nota: "))

result = ((num1 + num2 + num3) / 3)

print("A média das notas é", result)
'''

#6
'''
print("Calculador de área de um retângulo")

base = int(input("Base: "))
altura = int(input("Altura: "))

result = base * altura

print("A área do retângulo é", result)

'''


#7
'''
print("Bem vindo ao calculador de desconto!")

valor = int(input("Insere que o valor de um item:\n"))
desconto = int(input("Insere aqui o desconto que queres aplicar:\n"))

result = valor * (desconto/100)

print(result)

'''
'''
#8

INTEIRO1 = 8
INTEIRO2 = 2

#9 
print(INTEIRO1 + INTEIRO2)
'''

'''
#10 

nascimento = int(input("Coloca o teu ano de nascimento: "))

#11

ano_atual = 2024

idade = ano_atual - nascimento

print("A tua idade é", idade, "anos.")
'''

'''
#12

print("Bem vindo à conversora de graus Celsius para Fahrenheit!")

celsius = float(input("Insere que número em graus celsius queres converter para Fahrenheit:\n"))

conversao = celsius * float(1.8) + int(32)

print(conversao, "graus Fahrenheit!")
'''

#13
'''
print("Calculadora de temperatura dos grilos")

criscris = int(input("Indica quantos cricris faz o grilo num determinado momento:\n"))

temperatura = int(40) + criscris / int(4)

print("A temperatura do grilo é de", temperatura, "ºF")
'''

'''
#14

a = int(2)
b = int(4)
c = int(10)

#15

produto = a * b
soma = a + b + c
media = soma / int(3)

print("A multiplicação de a e b dá", produto)
print("A soma de a b e c é", soma)
print("A média destes 3 valores é", media)

'''

'''
#16 & #17
DOLAR = float(1.10)

print("Conversor de moeda com taxa dinâmica\n")

euros = float(input("Introduza o valor em euros que quer converter para Dolar:\n"))

resultado = euros * DOLAR

print(euros,"€ em dolar é", resultado, "$")

'''

'''
#18 & 19 

print("Calculador de Números par e impar")

num = int(input("Insere aqui o teu número:\n"))

result = int(num) // 2 * 2

if result == num:
    print("O número", num, "é par!")
else:
    print("O número", num, "é impar!")

'''

#20 & 21
'''
print("Calculador de IMC")

peso = float(input("Indica o teu peso em kg:\n"))
altura = float(input("Indica a tua altura em metros:\n"))

IMC = peso / (altura ** 2)
IMC_FORMATADO = round(IMC, 2)

if IMC < 18.5:
    print(IMC_FORMATADO, "Estás abaixo do peso!")
if IMC >= 18.5 and IMC <= 24.9:
    print(IMC_FORMATADO, "Peso Normal")
if IMC >= 25 and IMC <= 29.9:
    print(IMC_FORMATADO, "Sobrepeso")
if IMC >= 30 and IMC > 40:
    print(IMC_FORMATADO, "Tás gordo comó texugo pah")

'''

#22 #23

a = float(input("Indica um primeiro numero:\n"))
b = float(input("Indica um segundo numero\n"))
multiplo = float(a % b)

if multiplo != 0:
    print("não são multiplos")
if multiplo == 0:
    print("é multiplo")
