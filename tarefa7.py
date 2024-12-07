#1
'''
class Veiculo:
    def __init__(self, marca, modelo, ano, matricula, consumo, tanque, quilometros):
        self.marca = marca 
        self.modelo = modelo  
        self.ano = ano  
        self.matricula = matricula  
        self.consumo = consumo  
        self.tanque = tanque
        self.quilometros_percorridos = quilometros

class Roda:
    def __init__(self, marca, integridade):
        self.marca = marca  
        self.integridade = integridade 

r1 = Roda("Michelin", 0.89)
r2 = Roda("Michelin", 0.91)
r3 = Roda("Continental", 0.94)
r4 = Roda("Continental", 0.95)

c1 = Veiculo("Maserati", "Ghibli", "2023", "AA-00-FF", "12", "70", "20000")



print(r1.integridade)

print(c1.modelo)
'''











#2

class Pessoa:
    def __init__(self, nome, apelido, nacionalidade, data_nascimento, CC, validade_CC, nivel_escolaridade):
        self.nome = nome
        self.apelido = apelido
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento
        self.CC = CC
        self.validade_CC = validade_CC
        self.nivel_escolaridade = nivel_escolaridade

    def getNome(self):
        return self.__nome
    def getApelido(self):
        return self.__apelido
    def getNacionalidade(self):
        return self.__nacionalidade
    def getData_nascimento(self):
        return self.__data_nascimento
    def getCC(self):
        return self.__validade_CC
    def getNivel_escolaridade(self):
        return self.__nivel_escolaridade


p1 = Pessoa("Jose", "Ribeiro", "Russo", "23/12/2001", "30622008", "23/12/2025", "Básico")

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

print(p1.nome)