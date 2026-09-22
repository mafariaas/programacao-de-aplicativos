nota = input("Informe a nota da empresa (A, B, C, D ou F): ")

match nota:
    case "A" | "B":
        print("Excelente desempenho")
    case "C" | "D":
        print("Desempenho mediano")
    case "F":
        print("Reprovado")
    case _:
        print("Conceito inválido")