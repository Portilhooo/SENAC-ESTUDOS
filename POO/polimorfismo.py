#Classe Pai
class Funcionario:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario=salario
    def trabalhar(self):
        return f"{self.nome} está trabalhando..."

class Desenvolvedor(Funcionario):

    def codar(self):
        return f"{self.nome} está codando um sistema"
    
class Administrador(Funcionario):
    def gerenciando(self):
        return f"{self.nome} esta gerenciando"    

ger= Administrador("Pedro", 4500)
print(ger.trabalhar())
print(ger.gerenciando())
dev = Desenvolvedor("Mateus", 5000)
print(dev.trabalhar()) #Herdado do Pai
print(dev.codar())     #Específico do Filho        