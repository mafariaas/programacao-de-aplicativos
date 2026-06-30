import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cusor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUOINCREMENT,
            nome TEXT NOT NULL
    )
''')

# o banco não está salvando as alterações. Por quê?
conexao.close()