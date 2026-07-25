import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O professor pediu para mudar o nome do aluno de ID 3,
    # Mas o sistema alterou o nome de TODOS os alunos do banco de dados! Correção urgente:
    cursor.execute("UPDATE alunos SET nome = ? WHERE ide_aluno", (novo_nome, id_aluno))

    conexao.commit()
    conexao.close()

id_aluno = int(input("Informe o ID do aluno que deseja alterar: "))
novo_nome = input(""Digite o novo nome: )
print("Nome atualizado!")

#Faltava o 'WHERE' para executar a função apenas no id solicitado
#Faltava a variável dentro dos parênteses de cursor.execute
#Faltava as variáveis pedindo as informações necessárias para a troca de nome