def numero_maior():
    a=int(input("Digite o primeiro numero"))
    b=int(input("Digite o segundo numero"))
    if a>b:
        return a
    else:
        return b
resultado = numero_maior()
print("O maior numero é:", resultado)