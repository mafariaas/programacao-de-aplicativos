codigo = int(input("Informe o código: "))

match codigo:
    case 1 | 2:
        print("Alimentos perecíveis")
    case 3 | 4:
        print("Bebidas")
    case 5:
        print("Produtos de limpeza")
    case _:
        print("Código não cadastrado")