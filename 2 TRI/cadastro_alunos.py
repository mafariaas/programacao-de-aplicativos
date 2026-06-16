import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
                )''')

nome_aluno = input("Insira o nome do aluno a seguir: ")
telefone_aluno = input("insira o telefone do aluno a seguir: ")
turma_aluno = input ("Insira a turma do aluno a seguir: ")
idade_aluno = int(input("Insira a idade do aluno a seguir: "))
cpf_aluno = input("Informe o cpf do aluno a seguir: ")

comando_inserir = (f'''
                    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}')''')

cursor.execute(comando_inserir)
conexao.commit()
conexao.close() 