compras = []
produtos = ""
while produtos != "fim":
    produtos = input("Digite seus produtos: ")
    if produtos != "fim":
        compras.append(produtos)
print("Sua lista:  ")
for produtos in compras:
    print(produtos)
