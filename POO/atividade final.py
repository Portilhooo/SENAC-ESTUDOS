#Sistema de Gestão de Estoque

                                                                        #Polimorfismo
class Funcionario:
    def __init__(self, funcao):
        self.funcao = funcao
    def trabalhar(self):
        return f"{self.funcao} está trabalhando..."

class Estoquista(Funcionario):
    def estocar(self):
        return f"{self.funcao} está estocando" 

class Gerente(Funcionario):
    def gerenciar(self):
        return f"{self.funcao} está gerenciando a empresa"

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.__quantidade = 50
        self.set_quantidade(quantidade)

                                                                        #ENCAPSULAMENTO
    def get_quantidade(self):
        return self.__quantidade
    def set_preco(self, nova_quantidade):
        if nova_quantidade >=0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro: O preço não pode ser negativo!")

#Exibe as informações do produto    
    def exibir_informacoes(self):
        return f"Produto: {self.nome} | Estoque: {self.quantidade}"
    
                                                                                #Herança    
class Estoque(Produto):
    def __init__(self):
        self.estoque= []

    def consultar_produtos(self,produto):
        self.estoque.append(produto)

    def listar_produtos(self):
        for produto in self.estoque:
            print(f"{produto.nome}")   

produtos= Estoque()
produtos.consultar_produtos(Produto("Farofa", 10))
produtos.listar_produtos()               
    
ger= Gerente("Gerente")
print(ger.trabalhar)
print(ger.gerenciar())
estoq= Estoquista("Estoquista")
print(estoq.trabalhar)
print(estoq.estocar())

