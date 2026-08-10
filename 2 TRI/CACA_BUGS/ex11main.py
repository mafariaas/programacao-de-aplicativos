import sqlite3 

def listar_alunos_e_turmas():
    conexao = conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    
    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas ON alunos.id_turma = turmas.id")

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
    conxao.close()
    
# Sem a palavra 'ON' o código não sabe qual aluno pertence a qual turma 