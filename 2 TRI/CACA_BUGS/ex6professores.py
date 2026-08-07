import sqlite3


def cadastrar_professores():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    nome = input("Digite o nome do professor que deseja cadastrar: ")
    
    cursor.execute("INSERT INTO professores(nome) VALUES (?)", (nome,) )

    print("Professor cadastrado com sucesso")

    conexao.commit()
    conexao.close()


def buscar_professor():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    procurar_prof = int(input("Informe o ID do professor que deseja encontrar: "))
    cursor.execute(
        "SELECT * FROM professores WHERE id = ?",
        (procurar_prof,)
    )


    resultado = cursor.fetchone()

    if resultado:
        print("Professor encontrado:", resultado)
    else:
        print("Professor não encontrado!")

    conexao.close()

cadastrar_professores()
buscar_professor()   