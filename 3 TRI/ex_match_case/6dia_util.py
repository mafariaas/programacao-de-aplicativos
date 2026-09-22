dia = input("Digite um dia da semana: ")

match dia:
    case "sabado" | "domingo":
        print("Fim de samana")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Dia inválido!")