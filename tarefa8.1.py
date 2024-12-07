'''f = open("teste1.txt", "w")

f.write("Ola seu rato\n")
f.write("Pega la mais um problema para resolver")

f.close()

f1 = open("teste1.txt", "r")

for line in f1:
    print(line)

f1.close
'''
'''
def print_menu():
    print("Menu muito fixe:\n1) Criar utilizador\n2) Listar utilizadores\n3) Sair")
    opcao = input("Escolhe uma opção:")
    return opcao

def criarUtilizador():
    nome = input("Qual o teu nome pah: ")
    apelido = input("Qual o apelido: ")
    contacto = input("Qual o contacto: ")
    file = open("utilizadores.csv", "a")
    file.write(f"{nome},{apelido},{contacto}\n")
    file.close()
    print("Utilizador criado com sucesso!") 

def listarUtilizadores():
    f = open("utilizadores.csv")
    for linha in f:
        print(linha, end="")
    f.close()

while True:
    opcao = print_menu()
    if opcao == "1":
        criarUtilizador()
    elif opcao == "2":
        listarUtilizadores()
    else:
        break
'''

#1

historia = open("Ficheiro_2saida.txt", "w")
historia.write("―Podias fazer o favor de me dizer para onde devo ir a partir de agora?")
historia.write("―Isso depende muito de para onde é que queres ir ―disse o Gato.")
historia.write("―Nãão me importa muito onde... ―respondeu Alice.")
historia.write("―Entãão tambéém nãão importa por onde váás ―disse o Gato.")
historia.write("―... desde que chegue a algum lado ―explicou Alice.")
historia.write("―Oh, com certeza que chegas ―disse o Gato― se andares o suficiente")

historia.close()

historia = open("Ficheiro_2saida.txt", "r")
for line in historia:
    print(line, end="")

historia.close()

#2

entrada = open("Ficheiro_2.txt", "r")


for _ in range(3):
    linha = entrada.readline()
    if not linha:
        break
    linha.append(linha)

entrada.close()


sair = open("Ficheiro_2Saída_2.txt", "w",)

sair.writelines(linha)
sair.close()

print("As 3 primeiras linhas foram copiadas para Ficheiro_2Saída_2.txt")

#3

entrada = open("Ficheiro_2.txt", "r")

linhas = []
for _ in range(3):
    linha = entrada.readline()
    if not linha:
        break
    linhas.append(linha)

entrada.close()

saida = open("Ficheiro_2Saída_2.txt", "w")

saida.writelines(linhas)
saida.close()

print("As 3 primeiras linhas foram copiadas para Ficheiro_2Saída_2.txt")

#4

sair = open("Ficheiro_3.txt", "w")

for i in range(1, 11):
    saida.write(f"Linha {i}: Esta é a linha {i}\n")

sair.close()

print("O Ficheiro3 foi criado e preenchido com sucesso sotor.")




