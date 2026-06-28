saldo = 0.0


def depositar(valor):
    global saldo
    if valor <= 0:
        print('Valor inválido para depósito.')
        return
    saldo += valor
    print(f'Depósito realizado: R$ {valor:.2f}')
    print(f'Saldo atual: R$ {saldo:.2f}')


def sacar(valor):
    global saldo
    if valor <= 0:
        print('Valor inválido para saque.')
        return
    if valor > saldo:
        print('Saldo insuficiente.')
        return
    saldo -= valor
    print(f'Saque realizado: R$ {valor:.2f}')
    print(f'Saldo atual: R$ {saldo:.2f}')


def consultar():
    print(f'Saldo disponível: R$ {saldo:.2f}')


def main():
    while True:
        print('\n--- Sistema Bancário ---')
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Consulta')
        print('4 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            try:
                valor = float(input('Valor para depósito: R$ '))
                depositar(valor)
            except ValueError:
                print('Entrada inválida.')
        elif opcao == '2':
            try:
                valor = float(input('Valor para saque: R$ '))
                sacar(valor)
            except ValueError:
                print('Entrada inválida.')
        elif opcao == '3':
            consultar()
        elif opcao == '4':
            print('Encerrando programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == 'main':
    main()
