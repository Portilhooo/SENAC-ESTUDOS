contatos = {}
def cadastrar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    contatos[nome] = telefone
    print("Contato cadastrado com sucesso!")
def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for nome, telefone in contatos.items():
            print(f"{nome}: {telefone}")
def remover_contato():
    nome = input("Nome do contato a remover: ")
    if nome in contatos:
        del contatos[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado.")
while True:
    print("\nSistema de Agenda de Contatos")
    print("1. Cadastrar contato")
    print("2. Listar contatos")
    print("3. Remover contato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        remover_contato()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")