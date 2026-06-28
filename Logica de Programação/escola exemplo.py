total = 0

while True:
    print("\n=== CARDÁPIO ===")
    print("1 - Pizza (R$ 10)")
    print("2 - Salgado (R$ 7)")
    print("3 - Refrigerante (R$ 8)")
    print("0 - Finalizar pedido")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            total += 10
            print("Pizza adicionada!")

        case "2":
            total += 7
            print("Salgado adicionado!")

        case "3":
            total += 8
            print("Refrigerante adicionado!")

        case "0":
            print("\nFinalizando pedido...")
            break

        case _:
            print("Opção inválida!")

    input("\nPressione Enter para continuar...")

print(f"\nTotal do pedido: R$ {total:.2f}")
print("Obrigado pela preferência!")