class Motor:
    def ligar(self):
        return "Vrum Vrum!"
class Carro:
    def __init__(self, marca):
        self.marca= marca
        self.motor= Motor() #Associação (Composição)

meu_carro = Carro("Toyota")
print(meu_carro.motor.ligar())
print(meu_carro.marca)        
