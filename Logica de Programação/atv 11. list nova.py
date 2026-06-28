idade= int(input("Digite sua idade:"))
if idade<=12:
    print("Você esta na classificação de crianças!")
elif idade<=17:
    print("Você esta na classificação de adolescentes")
elif idade<=59:
    print("Você está na classificação de adultos")
else:
    print("Você está na classificação de idosos")            