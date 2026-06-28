hora= float(input("Quanto por hora trabalhada você ganha:"))
hora2= int(input("Quantas horas você trabalhou este mês:"))
salbruto= hora*hora2
desc1= salbruto %0.11
desc2= salbruto %0.08
desc3= salbruto %0.05
liquido= salbruto - desc1 - desc2 - desc3

print("Seu salario liquido é de: R$", liquido)
print("O desconto do IR é de: R$", desc1)
print("O desconto do INSS é de: R$", desc2)
print("O desconto para o sindicato é de: R$", desc3)
