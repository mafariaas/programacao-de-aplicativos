import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL,
                    escola TEXT
                    )''')
    nome_professor = input("Informe o nome do professor: ")
    telefone_professor = input("Informe o telefone do professor: ")
    materia_professor = input("Informe a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("Digite o cpf do professor: ")
    salario = float(input("Digite o salário do professor: "))
    nome_escola = input("Informe o nome da escola: ")
    
    comando_inserir = (f'''
                    INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, escola)
                    VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', '{idade_professor}', '{cpf_professor}', '{salario_professor}', '{nome_escola}')''')

cursor.execute(comando_inserir)
conexao.commit()
conexao.close() 

def listar():
    cursor.execute("SELECT * FROM professores")

    todos_professores = cursor.fetchall()

    print("=====PROFESSORES CADASTRADOS=====")

    if not todos_professores:
        print("Nenhum professore cadastrado!")

    else:
        for prof in todos_professores:
            print(f"ID: {professor[0]}")
            print(f"Nome: {professor[1]}")
            print(f"Telefone: {professor[2]}")
            print(f"Matéria: {professor[3]}")
            print(f"Idade: {professor[4]}")
            print(f"CPF: {professor[5]}")
            print(f"salario: {professor[6]}")
            print(f"Nome escola: {professor[7]}")
            print("-" * 30)

    conexao.close()
