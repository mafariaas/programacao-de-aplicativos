nomes = ["Maria", "Helena", "Carlos", "Julia"]
print("LIsta de nomes:", nomes)
antigo = input("Qual nome deseja mudar? ")
novo = input("Digite o novo nome: ")

posicao = 0 

while posicao < len(nomes):
    if nomes[posicao] == antigo:
        nomes[posicao] = novo 

    posicao = posicao + 1 
print("Lista atualizada:", nomes)
