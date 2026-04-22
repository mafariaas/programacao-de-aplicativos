nota = int(input("Digite sua nota: "))

def avaliar_desempenho (nota):
    if nota >= 9:
        print("Exelente")
    elif nota >= 7:
        print("Bom")
    else:
        print("Insuficiente")
    
avaliar_desempenho(nota)