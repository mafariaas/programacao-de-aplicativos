print("| 1- Café | 2- Chá | 3- Suco |")

opcao = int(input("Informe a opção desejada: "))

match opcao:
    case 1:
        print("Você escolheu CAFÉ")
    case 2:
        print("Você escolheu CHÁ")
    case 3:
        print("Você escolheu SUCO")
    case _:
        print("OPÇÃO INVÁLIDA!")

