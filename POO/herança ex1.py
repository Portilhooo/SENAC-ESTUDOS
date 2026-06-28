class Animal:
    def respirar(self):
        print("Respirando..")
class Cachorro(Animal):
    def latir(self):
        print("Au au!")
class Passaro(Animal):
    def cantar(self):
        print("*Passaro cantando*")
print("=================")
passaro= Passaro()
passaro.cantar()
dog = Cachorro()
dog.respirar() #Herdado
dog.latir() #Proprio        
print("=================")
class Pessoas:
    def fala(self):
        print("*Pessoas Falando*")
class Vendedor(Pessoas):
    def vendas(self):
        print("Vendedor:Promoção ilimitada corram pra aproveitar!")
pessoa= Pessoas()
pessoa.fala()
vendedor= Vendedor()
vendedor.vendas()
print("==================")