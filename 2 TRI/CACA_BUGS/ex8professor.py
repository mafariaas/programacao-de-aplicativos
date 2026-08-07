import sqlite3

def cadastrar_professores(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS professores
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf  TEXT UNIQUE NOT NULL
        )
    ''')

    conexao.commit()

    cursor.execute('''
    INSERT INTO professores (nome, cpf) VALUES (?, ?)
    ''', ("Gabriel Moya", "000-000-000.00"))

    conexao.commit()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("Lista de professores: ")
    for professor in professores:
        print(professor)

    conexao.close()

cadastrar_professores("Gabriel Moya", "000-000-000.00")

