produto_novo=[]
while True:
    print("Sistema de produtos")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Calcular valor total do estoque")
    opcao=int(input("Digite a opção que deseja:"))

    match opcao:
        case 1:
            produto_novo=(input("Digite o nome do produto que sera cadastrado:"))
            valor_prod=float(input("Digite o valor do produto:"))
        case 2:
            for produto in produto_novo:
                print("Nome:", {produto})    


