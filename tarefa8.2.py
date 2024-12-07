#1
'''
texto = open("Ficheiro_1.txt", "w", encoding="utf-8")
texto.write("Tá a formaaaaaaaaaar!!!!!\n")
texto.write("Tá a empurrar a terra oh trambolho\n")
texto.write("Não consegues chegar a horas então chega 5 minutos mais cedo!\n")

texto.close()

texto = open("Ficheiro_1.txt", "r", encoding="utf-8")

primeira_linha = texto.readline()
print(primeira_linha)
texto.close()
'''

#2
'''
texto = open("Ficheiro_1.txt", "w", encoding="utf-8")
texto.write("Tá a formaaaaaaaaaar!!!!!\n")
texto.write("Tá a empurrar a terra oh trambolho\n")
texto.write("Não consegues chegar a horas então chega 5 minutos mais cedo!\n")

texto.close()

texto = open("Ficheiro_1.txt", "r", encoding="utf-8")

primeira_linha = texto.readline()
print(primeira_linha.upper())

texto.close()
'''
#3
''''
texto = open("Ficheiro_1.txt", "w", encoding="utf-8")
texto.write("Tá a formaaaaaaaaaar!!!!!\n")
texto.write("Tá a empurrar a terra oh trambolho\n")
texto.write("Não consegues chegar a horas então chega 5 minutos mais cedo!\n")

texto.close()

texto = open("Ficheiro_1.txt", "r", encoding="utf-8")

numero_linhas = len(texto.readline())
print(numero_linhas)
texto.close()
'''
#4
'''
try:
    texto = open("Ficheiro_2.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Ficheiro_2.txt não encontrado. Criando o ficheiro...")
    texto = open("Ficheiro_2.txt", "w", encoding="utf-8")
    texto.write("Este é um exemplo de texto.\nContém várias palavras para testar.\n")
    texto.close()
    texto = open("Ficheiro_2.txt", "r", encoding="utf-8")

conteudo = texto.read()
texto.close()

palavras = conteudo.split()
numero_palavras = len(palavras)

print(f"O número de palavras no ficheiro é: {numero_palavras}")
'''

#5
'''
texto = open("Ficheiro_2.txt", "r", encoding="utf-8")
conteudo = texto.read()
texto.close()

numero_caracteres = len(conteudo)

print(f"O número total de caracteres no ficheiro é: {numero_caracteres}")
'''

#6
texto = open("Ficheiro_2.txt", "r", encoding="utf-8")
conteudo = texto.read()
texto.close()

conteudo_modificado = conteudo.replace("dor", "emoção")

print(conteudo_modificado)

