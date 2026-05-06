livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
print("Livros disponíveis", livros_disponiveis)
livros_emprestados = []

pergunta = input("Digite o livro que deseja emprestar: ")
if pergunta in livros_disponiveis:
    livros_emprestados.append(pergunta)
    livros_disponiveis.remove(pergunta)
    print("Emprestimo realizado com sucesso!")
else:
    print("Desculpe, esse livro não esta a cervo")

pergunt = input("Digite o nome do livro que eseja devolver: ")
if pergunt in livros_emprestados:
    livros_disponiveis.append(pergunt)
    livros_emprestados.remove(pergunt)
    print("Devolução feita com sucesso!")
else:
    print("Desculpe, este livro não consta como emprestado!")
del livros_disponiveis[0:2]
print("lista de livros disponíveis atualizada: ", livros_disponiveis) 