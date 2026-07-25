import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Se o id_prof não existir, ocorre um IntegrityError.
    # Se o erro acontecer, o que ocorre com a linha com a linha conexao.close()?
    try:
        cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUE (?, ?, ?)", (nome, id_serie, id_professor)) 
        conexao.commit()
    except sqlite3.IntegrityError:
        ("Professor inexistente!")
    finally: 
        conexao.close()
        
# Se lo erro acontecer o conexao.close não é executado
# Para resolver, adicionamos o try e o except, assim caso o professor solicitado não exista mostrará uma mensagem e o programa fechara sem perder as outras informações