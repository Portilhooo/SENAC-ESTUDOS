class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = 0.0
        self.set_preco(preco)
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, novo_preco):
        if novo_preco >=0:
            self.__preco = novo_preco
        else:
            print("Erro: O preço não pode ser negativo!")

meu_produto = Produto("Mouse", 100)

print(f"{meu_produto.get_preco()}")

meu_produto.set_preco(800)
