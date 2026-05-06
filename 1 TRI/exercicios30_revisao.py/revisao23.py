lista = []
nota1 = int(input("Digite suas notas: "))
nota2 = int(input("Digite suas notas: "))
nota3 = int(input("Digite suas notas: "))
nota4 = int(input("Digite suas notas: "))

lista.append(nota1)
lista.append(nota2)
lista.append(nota3)
lista.append(nota4)

soma = 0


for nota in lista:
    soma += nota 

media = soma / 4
if media >= 70:
    print("Aprovado! Sua media é:", media)
elif media == 50 and media <= 69:
    print("Recuperação! Sua media é:", media)
else:
    print("Reprovado! Sua media é:", media)
