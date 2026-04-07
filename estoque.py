ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]

pergunta = input("Digite o nome da ferramenta que está procurando: ")
   
for ferramenta in ferramentas:
    if ferramenta == pergunta:
        posição = ferramentas.index(pergunta)
        print(f"Peça encontrada na posição: ", {posição})

if pergunta not in ferramentas:

    controle = input("Deseja adicionar o item a lista? ")

    while controle != "sair":
        ferramenta = input("Digite o nome que deseja adicionar: ")
        ferramentas.append(ferramenta)
        controle = input("Deseja adicionar o item a lista? ")
    print(ferramentas)