saldo =200
def sistema ():
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Verificar saldo")
    opcao=(input("Escolha oque deseja fazer:"))
    match opcao:
        case 1:
            print("Qual valor deseja sacar?")
            valor=(input("Digite o valor:"))
            saldo = saldo-valor
            return sistema()
    
sistema()        
