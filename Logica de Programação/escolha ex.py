#opcao = int(input(" Cardápio \n[1] Carne \n[2] Frangos \n[3] Tira-Gosto \nEscolha uma opção:"))
total= 0
print("Cardápio")

match opcao:

        case 1:
            print("[1] Picanha \n[2]Patinho \n[3]Carneiro\n[4] Voltar para a pagina anterior")
            

        case 2:
            print("Frango à Passarinho \nFrango Assado")

        case 3:
            print("Pão de Alho \nCalabresa \nLinguiça de Frango")

        case _:
            print("Escolha uma opção correta!")