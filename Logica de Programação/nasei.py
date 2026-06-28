##Cadastre 5 numeros em uma lista
#mostre apenas os numeros pares#
#exiba a soma de todos os numeros

#Variaveis
numeros = []
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.append(6)
pares=[]
soma= 0
#Exibição da lista de numeros.
print("Lista de numeros", numeros)
#Usando o for para percorrer a lista de numeros e verificar quais são pares, e somar os numeros.
for i in numeros:
    if i % 2 == 0:
        print("numeros pares:", i)
    soma = soma + i
print("A soma de todos os numeros é:", soma)