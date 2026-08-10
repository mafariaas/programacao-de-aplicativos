import sqlite3

def atualizar_nome_aluno():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE alunos SET nome = ? WHERE id_aluno", (novo_nome, id_aluno))

    conexao.commit()
    conexao.close()

id_aluno = int(input("Informe o ID do aluno que deseja alterar: "))
novo_nome = input("Digite o novo nome: ")
print("Nome atualizado!")

atualizar_nome_aluno()

# O sistema alteroava o nome de todos os alunos pois estava sem o comando 'WHERE' ou seja, não expecificava 
# o que deveria ser alterado, então ele alterava todos os alunos para o novo nome informado