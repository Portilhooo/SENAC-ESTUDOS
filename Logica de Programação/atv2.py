n1= float(input("Digite a primeira nota do aluno:"))
n2= float(input("Digite a segunda nota do aluno:"))
n3= float(input("Digite a terceira nota do aluno:"))

soma= n1+n2+n3
media= soma/3

if media>=7:
        print("A nota do aluno é:", media, "o aluno está aprovado")
elif media>=5<=6.9:

        print("A nota do aluno é", media, "o aluno está de recuperação")       
else:
        print("A nota do aluno é:", media, "O aluno está de reprovado")        
