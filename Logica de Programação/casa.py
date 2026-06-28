energia= 100
consumo= 0
statusofftv= "Desligado"
statusontv= "Ligado"
statusoffgel= "Desligado"
statusongel= "Ligado"
statusoffar= "Desligado"
statusonar= "Ligado"
dp1= "Ar-Condicionado"
dp2= "TV"
dp3= "Geladeira"
consumoar=0
consumogeladeira=0
consumotv=0
desligadoar= "Desligado"
desligadotv= "Desligado"
desligadogel= "Desligado"

while True:
    
    print("======================================")
    print("  Casa Inteligente do Teteu e Brunão  ")
    print("======================================")
    print("1 - Visualizar Dispositivos")
    print("2 - Ligar um dispositivo")
    print("3 - Desligar um dispositivo")
    print("4 - Exibir o consumo de energia")
    print("5 - Encerrando programa")
    opcao=int(input("Escolha uma opção:"))
    match opcao:
        case 1:
            print("Dispostivo:", dp1, "; Status:", statusoffar, "; Consumo:",consumoar, "W")
            print("Dispostivo:", dp2, "; Status:", statusofftv, "; Consumo:",consumotv, "W")
            print("Dispostivo:", dp3, "; Status:", statusoffgel, "; Consumo:",consumogeladeira, "W")
            input("Pressione enter para voltar para o menu principal")
        case 2:
            print("1 - Ar-Condicionado")
            print("2 - TV")
            print("3 - Geladeira")
            print("4 - Voltar ao menu")
            esc=int(input("Escolha qual dispositivo deseja ligar:"))
            if esc==1:
                consumoar+=20
                energia-=20
                consumo+=20
                statusoffar=statusonar
                print("Você ligou o ar-condicionado!")
                input("Pressione ENTER para voltar para o menu...") 
            elif esc==2:
                consumotv+=30
                energia-=30
                consumo+=30
                statusofftv=statusongel
                print("Você ligou a TV!")
                input("Pressione ENTER para voltar para o menu...")      
            elif esc==3:
                consumogeladeira+=50
                energia-=50
                consumo+=50
                statusoffgel = statusongel
                print("Você ligou a geladeira")
                input("Pressione ENTER para voltar para o menu...")     
            elif esc==4:
                print("Você escolheu voltar ao menu principal")
            else:
                print("Você escolheu uma opção inválida")
                input("Pressione enter para voltar ao menu principal...")    
        case 3:
            print("1 - Ar-Condicionado")
            print("2 - TV")
            print("3 - Geladeira")
            print("4 - Voltar ao menu")   
            esc2=int(input("Escolha qual dispositivo deseja desligar:"))
            if esc2==1:
                consumoar-=20
                energia+=20
                consumo-=20
                statusoffar= desligadoar
                print("Você escolheu desligar este dispositivo")
                input("Pressione ENTER para voltar para o menu...")
            elif esc2==2:
                consumotv-=30
                consumo-=30
                energia+=30
                statusofftv=desligadotv
                print("Você escolheu desligar este dispositivo")
                input("Pressione ENTER para voltar para o menu...")
            elif esc2==3:
                consumogeladeira-=50
                consumo-=50
                energia+=50
                statusoffgel=desligadogel
                print("Você escolheu desligar este dispositivo")
                input("Pressione ENTER para voltar para o menu...")
            elif esc2==4:
                print("Você escolheu voltar para o menu principal")
            else:
                print("Você digitou uma opçao inválida! Voltando para o menu principal")
                input("Pressione enter para voltar...")        
        case 4:
            if consumo >= 0:
                print("O consumo total de energia é de:", consumo,"W")
                input("Pressione ENTER para voltar")  
            else:
                print("O consumo total de energia é de: 0 W")
        case 5:
            print("Encerrando programa, obrigado por utilizar nossos serviços")
            break
        case _:
            print("Opção inválida tente novamente!")   
            input("Pressione ENTER para voltar")                    