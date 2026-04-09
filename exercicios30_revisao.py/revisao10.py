usuarios = ["Maria", "Helen", "Alice", "Carlos"] #Adicionar
perg = input("Digite o nome desejado ou digite 'sair' para encerrar: ")

while perg != "sair":
    if perg in usuarios:
        print(f"O nome {perg} já está cadastrado!", usuarios)
        perg = input("Digite outro nome: (Caso não queira digite 'sair' para encerrar) ")

    else:
        perg2 = input("Nome não cadastrado! Deseja adicionar este novo nome a lista de usuarios? 'S' para sim ou 'sair' para encerrar o programa): ")
        if perg2 == "S":
            usuarios.append(perg)
            print("Usuario adicionado! Lista atualizada:", usuarios)
            perg = input("Digite outro nome: (Caso não queira digite 'sair' para encerrar) ")

print("Encerrando programa...")