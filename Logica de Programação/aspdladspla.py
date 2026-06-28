def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def calcular_maior_valor(numeros):
    if not numeros:
        return None
    return max(numeros)

def calcular_menor_valor(numeros):
    if not numeros:
        return None
    return min(numeros)

def calcular_soma_total(numeros):
    return sum(numeros)

# Sistema de Relatórios
numeros = list(map(float, input("Digite os números separados por espaço: ").split()))

print(f"Média: {calcular_media(numeros)}")
print(f"Maior valor: {calcular_maior_valor(numeros)}")
print(f"Menor valor: {calcular_menor_valor(numeros)}")
print(f"Soma total: {calcular_soma_total(numeros)}")