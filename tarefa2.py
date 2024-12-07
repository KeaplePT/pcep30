#1
'''
print("Programa que indica que o número é par ou não")

num = int(input("Indica um número:\n"))

paridade = num % 2

if paridade == 0:
    print(num, "é um número par")
elif paridade != 0:
    print(num, "é um número impar!")
else:
    print("Insire um número!")

'''

#2
'''
idade= int(input("Insire a tua idade:\n"))

if 13 <= idade <= 19:
    print("Com", idade, "anos és Adolescente!")
else:
    print("És de alguma outra categoria que o prof não mandou colocar aqui no exercício")

'''

#3
'''
print("Bem vindo à bilheteira!")

idade = int(input("Indica a tua idade para comprares o bilhete!\n"))

if idade < 5:
    print("O bilhete é de graça!")
elif idade >= 5 and idade <= 10:
    print("O bilhete custa 5€!")
elif idade >= 11 and idade < 64:
    print("O bilhete custa 20€!")
elif idade >= 65  and idade <= 99 and idade >= 101 :
    print("O bilhete custa 5€!")
if idade == 100:
    print("O bilhete é de graça!")
'''

#4
'''
print("Indicador de ano bissexto ou não")

ano = int(input("Indica um ano à tua escolha: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")
'''

#5
'''
num = str(input("Indica um número de telefone de 9 digitos: "))

def validar_numero(num):

    if len(num) != 9:
        print("Insere um número com 9 digitos")
    if not num.isnumeric():
        print("Escreve apenas um número")

    if num[0] not in ("9"):
        print("O número tem de começar por 9!")

numero = validar_numero(str(num))

print(numero)

DOUBTS!!!
'''

#6
nota1 = float(input("Insire a primeira nota: "))
nota2 = float(input("Insire a segunda nota: "))
nota3 = float(input("Insire a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3 

if media < 9.5:
    if nota1 or nota2 or nota3 < 7.5:
        print("Reprovado")
else:
    print("Aprovadissimo")