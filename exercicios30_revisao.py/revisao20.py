produtos = []
entrada = ""

while entrada != "sair":
    entrada = input("Digite o produto ou (sair) para sair. ")

    if entrada != "sair":
        produtos.append(entrada)


print(f"Sua lista de produtos é {produtos}")
