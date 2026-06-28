class Cliente:
    def __init__(self, nome, saldo):
        self.nome=nome
        self.__saldo = saldo

    def get_saldo(self): return self.__saldo
    
    def depositar(self, valor):
        if valor >0: self.__saldo += valor
        else:
            print("O valor deve ser positivo")
    def sacar (self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    def trasferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Sucesso: {self.nome} transferiu R${valor} para {destino.nome}.")
        else:
            print(f"Falha: Saldo insuficiente para transferir R${valor}.")    

meusaldo = Cliente("Carlos",1500)      

print(f"{meusaldo.get_saldo()}")      
            