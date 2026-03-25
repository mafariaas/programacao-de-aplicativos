cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome = input("Digite o nome de uma cidade: ")
if nome in cidades :
    print(f"A cidade {nome} está na posição", cidades.index(nome))
else:
    print(f"A cidade {nome} não está autorizada!")
