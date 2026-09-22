opcao = int(input("Informe a opção desejada (1 a 4): "))

match opcao:
    case 1:
        print("1- Tela de resultados")
    case 2:
        print("2- Tela de consulta")
    case 3:
        print("3- Tela de relatórios")
    case 4:
        print("4- Saindo do programa")
    case _:
        print("Opção incorreta")

