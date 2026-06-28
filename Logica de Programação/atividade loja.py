carrinho = ""
compra= 0
tenisqtd= 50
calcaqtd= 2
relogioqtd=10
final="S"
itens= ["1- Tenis: R$200.00", "2- Calça Jeans: R$300.00", "3- Relogio: R$750.00"]
while True:
    print("====Lojinha do Seu Zé====")
    print("1 - Ver Produtos")
    print("2 - Comprar Produtos")
    print("3 - Ver Carrinho")
    print("4 - Ver Estoque")
    print("5 - Sair")
    opcao=int(input("Escolha a opção que deseja:"))

    match opcao:
        case 1:
            for item in itens:
                print(item)          
        case 2:
            for item in itens:
                print("1 - Tenis\n2 - Calça Jeans\n3 - Relogio\n4 - Sair")
                esc=int(input("Escolha o produto que deseja comprar:"))               
                if esc== 1:
                    compra +=200
                    tenisqtd -=1
                    carrinho += "\nTênis"
                    print("Você adicionou Tênis ao carrinho")
                elif esc== 2:
                    compra +=300
                    calcaqtd -=1
                    carrinho += "\nCalça Jeans"
                    print("Você adicionou Calça Jeans ao carrinho")
                    if calcaqtd<0:
                        print("Ação anterior negada! Voltando para o menu inicial")
                elif esc== 3:
                    compra +=750
                    relogioqtd -=1
                    carrinho += "\nRelogio"
                    print("Você adicionou Relogio ao Carrinho")
                elif esc== 4:
                    print("Você voltou para o menu principal")
                    break
                else:
                    print("Você digitou uma opção inválida, tente novamente!")
        case 3:
            print("=== Carrinho ===")
            print("O valor de sua compra é:", compra - compra%0.10)
            print("Produtos:", carrinho)
            final=input(str("Deseja Finalizar a compra? (S/N):")).upper()
            if final=="S":
                print("Finalizando Compra...")
                break
            elif final== "N":
                input("Pressione enter para entrar no menu principal")
                print("Você voltou para o menu principal")
        case 4:
            print("Quantidade de tênis:", tenisqtd)
            print("Quantidade de calças Jeans", calcaqtd)
            print("Quantidade de relogios:", relogioqtd)
            input("Pressione enter para voltar para o menu principal")
        case 5:
            print("Obrigado por usar nossos serviços")    
        case _:
            print("Opção inválida! Escolha alguma válida")           