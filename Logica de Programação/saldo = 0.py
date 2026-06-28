def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("=== Conversor de Temperatura ===")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = input("\nEscolha uma opção (1 ou 2): ")

if opcao == "1":
    temp_c = float(input("Digite a temperatura em Celsius: "))
    temp_f = celsius_para_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f:.2f}°F")
elif opcao == "2":
    temp_f = float(input("Digite a temperatura em Fahrenheit: "))
    temp_c = fahrenheit_para_celsius(temp_f)
    print(f"{temp_f}°F = {temp_c:.2f}°C")
else:
    print("Opção inválida!")
