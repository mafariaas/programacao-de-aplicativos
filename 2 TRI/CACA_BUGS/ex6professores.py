import sqlite3

def buscar_professores(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

        nome_prof = input("Informe o nome do professor")
        conexao.commit()
        cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,) )

    resultado = cursor.fetchone()
    print(resultado)
    conexao.close

    if resultado:
        print("Professor encotrado:", resultado[0])
    else:
        print("Professor não encontrado!")

    conexao.close()

buscar_professores(1)