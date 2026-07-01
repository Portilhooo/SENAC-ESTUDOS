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
        self.__quantidade = 50                                          # Encapsulamento
        self.set_quantidade(quantidade)

                                                                     # ENCAPSULAMENTO
    def get_quantidade(self):
        return self.__quantidade
        
    def set_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro: A quantidade não pode ser negativa!")

    # Exibe as informações do produto    
    def exibir_informacoes(self):
        return f"Produto: {self.nome} | Estoque: {self.get_quantidade()}"
    

# ASSOCIAÇÃO: Estoque NÃO herda de Produto. Ele possui uma lista de Produtos.
class Estoque:
    def __init__(self):
        self.produtos_armazenados = []  # Aqui acontece a associação

    def adicionar_produto(self, produto: Produto):  # Associando o objeto Produto
        self.produtos_armazenados.append(produto)

    def listar_produtos(self):
        print("\n--- Lista de Produtos no Estoque ---")
        for produto in self.produtos_armazenados:
            print(produto.exibir_informacoes())


# --- Testando o Código ---

# Criando o estoque da empresa
meu_estoque = Estoque()

# Criando produtos
prod1 = Produto("Farofa", 10)
prod2 = Produto("Arroz", 25)

# Associando os produtos ao estoque
meu_estoque.adicionar_produto(prod1)
meu_estoque.adicionar_produto(prod2)

# Listando produtos associados
meu_estoque.listar_produtos()              
    
print("\n--- Funcionários ---")
ger = Gerente("Carlos (Gerente)")
print(ger.trabalhar())  # Adicionado os parênteses () para chamar a função
print(ger.gerenciar())

estoq = Estoquista("João (Estoquista)")
print(estoq.trabalhar())  # Adicionado os parênteses () para chamar a função
print(estoq.estocar())