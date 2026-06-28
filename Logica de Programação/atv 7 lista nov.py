while True:

    num1=float(input("Digite o primeiro número:"))
    num2=float(input("Digite o segundo número:"))
    print("==== Calculadora ====")
    print("Qual operação deseja fazer?")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    op=int(input("Digite o numero da operação que deseja fazer:"))

    match op:
        case 1:
                print("A soma dos numeros é :", num1+num2)
        case 2:
                print("A subtração dos numeros é :",num1-num2)
        case 3:
                print("A Multiplicação desses numeros é:", num1*num2)
        case 4:
                print("A divisão desses numeros é:", num1/num2)   
        case _:
                print("Opção inválida escolha uma opção correta")                                  