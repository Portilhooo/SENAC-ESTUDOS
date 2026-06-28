usuario= "junior"
senha= "123"
tentativa=3

while tentativa>0:
            
    user=str(input("Informe seu user:"))
    senha=int(input("Informe sua senha:"))
    if user== usuario and senha== 123:
        print("Login bem sucedido")
        break
    else:
        tentativa-=1
        print(f"Dados incorretos tente novamente! Nº de tentativas:{tentativa}")
if tentativa==0:
    print("Você ta bloqueado!")