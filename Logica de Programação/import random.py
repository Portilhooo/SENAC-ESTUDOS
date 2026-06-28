Saldo = 1000
while True: 
    operacoes = 0

    print("Bem-vindo ao caixa eletrônico 24h!")
    print("1 - Consultar Saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    escolha = float(input("Escolha uma opção:"))
    if escolha == 1:
            print("Seu saldo é de R$", Saldo)
    elif escolha == 2:
        valor_saque= float(input("Digite o valor que deseja sacar: "))
        if valor_saque > Saldo:
                print("Saldo insuficiente.")
    else:
        Saldo -= valor_saque
        operacoes += 1
    print("Saque realizado com sucesso. Seu saldo atual é de R$", Saldo)

    if escolha==3:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        Saldo += valor_deposito
        operacoes += 1
        print("Depósito realizado com sucesso. Seu saldo atual é de R$", Saldo)
    if escolha == 4:
        print("Obrigado por usar o caixa eletrônico 24h!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        