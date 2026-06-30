class Funcionario:
    def trabalhar(self):
        return "Executando tarefas genéricas."
class Desenvolvedor(Funcionario):
    #Sobrescrita: altera o comportamento do metodo pai
    def trabalhar(self):
        return "Codando novas funcionalidades!"
class Gerente(Funcionario):
    def trabalhar(self):
        return "Gerenciando a equipe e projetos..." 
class Administrador(Funcionario):
    def trabalhar(self):
        return "Gerenciando setores..."    

    #Testando o Polimorfismo

equipe = [Desenvolvedor(), Gerente(), Administrador()]
for membro in equipe:
    print(membro.trabalhar())           