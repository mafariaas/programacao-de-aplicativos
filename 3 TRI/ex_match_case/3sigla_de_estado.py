sigla = input("Informe a sigla: ")

match sigla:
    case "PR":
        print("Paraná")
    case "SC":
        print("Santa Catarina")
    case "RS":
        print("Rio Grande")
    case _:
        print("Estado fora da região Sul")