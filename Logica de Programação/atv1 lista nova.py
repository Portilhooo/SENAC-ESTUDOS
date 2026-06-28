alt=float(input("Informe sua altura:"))
sexo=int(input(" [1] Homem \n [2] Mulher \nInforme seu sexo:"))

if sexo==1:
    alt=(alt*72.7)/2
    print("Seu peso ideal é:",alt)
elif sexo==2:
    alt= (alt*62.1)/2
    print("Seu peso ideal é:", alt)    
