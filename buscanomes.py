nomes = ["maria", "melissa", "eduarda", "isadora", "joao", "gustavo"]
verificar = input("digite o nome de verificaçao: ")
if verificar in nomes:
    print(f"O nome {verificar} está na lista!")
else:
    print(f"O nome {verificar} não foi encontrado na lista!")
