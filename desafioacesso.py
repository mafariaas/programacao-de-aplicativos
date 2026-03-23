autorizados = ["Alice", "Bob", "Carlos"]
nome = input("Digite o nome de um pesquisador: ")
if nome == "Alice" or "Bob" or "Carlos":
    print(f"Acesso Permitido! O pesquisador {nome} está na posição", autorizados.index(nome))
    pergunta = input ("Deseja remover esse pesquisador da lista (Sim/Não)")
if pergunta == "Sim":
    autorizados.remove(nome)
    print(f"Agora os membros da lista são {autorizados}")
else:
    print(f"Acesso negado! O pesquisador {nome} não foi encontrado")
    pergunta2 = input("Deseja cadastrar esse nome como novo pesquisador? (Sim/Não): ")
    if pergunta2 == "Sim":
        autorizados.append(nome)

