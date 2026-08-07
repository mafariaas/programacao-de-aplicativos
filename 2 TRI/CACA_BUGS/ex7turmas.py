import sqlite3

def criar_tabela_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_serie INTEGER,
        id_prof INTEGER,
        FOREIGN KEY (id_serie) REFERENCES series(id),
        FOREIGN KEY (id_prof) REFERENCES professores(id)
        )
    ''')
    conexao.commit()
    print("Tabela turmas criada!")
    conexao.close()


def cadastrar_turma():
    nome = input("Digite o nome do aluno: ")
    id_serie = int(input("Digite o ID da série: "))
    id_prof = int(input("Digite o ID do professor: "))
    
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute("INSERT INTO turmas (nome, id_serie, id_prof) VALUES (?, ?, ?)", (nome, id_serie, id_prof)) 
        conexao.commit()
        print("Turma cadastrada!")

    except sqlite3.IntegrityError as e:
        print("Professor ou série inexistente!", e)
    finally: 
        conexao.close()
        
criar_tabela_turmas()
cadastrar_turma()