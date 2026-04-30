nota_teste = int(input("Digite sua nota: "))
anos_xp = int(input("Digite quantos anos de experiência possui: "))
possui_certificacao = input("Possui certificação? (Responda com S/N): ")

def verificar_aprovação(nota_teste, anos_xp, possui_certificacao):
    if (nota_teste >= 80 and anos_xp >= 2) or possui_certificacao == "S":
        print("Contratar")
    else:
        print("Descartar")

verificar_aprovação(nota_teste, anos_xp, possui_certificacao)