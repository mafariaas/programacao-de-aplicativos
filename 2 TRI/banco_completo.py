import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def listar_professor():
    cursor.execute("SELECT * FROM professores")

    todos_professores = cursor.fetchall()

    print("=====PROFESSORES CADASTRADOS=====")

    if not todos_professores:
        print("Nenhum professor cadastrado!")

    else:
        for professor in todos_professores:
            print(f"ID: {professor[0]}")
            print(f"Nome: {professor[1]}")
            print(f"Telefone: {professor[2]}")
            print(f"Matéria: {professor[3]}")
            print(f"Idade: {professor[4]}")
            print(f"CPF: {professor[5]}")
            print(f"salario: {professor[6]}")
            print(f"Nome escola: {professor[7]}")
            print(f"Endereço: {professor[8]}")
            print("-" * 30)

def criar_tabela():
    listar_professor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    professor_id INTEGER,
                    endereco_aluno TEXT,
                    cidade_aluno TEXT,
                    estado_aluno TEXT,
                    FOREIGN KEY (professor_id) REFERENCES professores(id) 
                    )''')

    nome_aluno = input("Insira o nome do aluno a seguir: ")
    telefone_aluno = input("insira o telefone do aluno a seguir: ")
    turma_aluno = input ("Insira a turma do aluno a seguir: ")
    idade_aluno = int(input("Insira a idade do aluno a seguir: "))
    cpf_aluno = input("Informe o cpf do aluno a seguir: ")
    professor_id = int(input("Digite o ID do professor: ")) 
    endereco_aluno = input("Insira o endereço do aluno: ")
    cidade_aluno = input("Digite a cidade do aluno: ")
    estado_aluno = input("Digite o estado do aluno: ")
    comando_inserir = (f'''
                        INSERT INTO alunos (nome, telefone, turma, idade, cpf, professor_id, endereco_aluno, cidade_aluno, estado_aluno   )
                        VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}', {professor_id}, '{endereco_aluno}', '{cidade_aluno}', '{estado_aluno}')''')

    cursor.execute(comando_inserir)
    conexao.commit()

def listar():
    cursor.execute("SELECT * FROM alunos")

    todos_alunos = cursor.fetchall()

    print("-----ALUNOS CADASTRADOS-----")

    if not todos_alunos:
        print("Nenhum aluno cadastrado!")

    else:
        for aluno in todos_alunos:
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Telefone: {aluno[2]}")
            print(f"Turma: {aluno[3]}")
            print(f"Idade: {aluno[4]}")
            print(f"CPF: {aluno[5]}")
            print(f"Endereço: {aluno[6]}")
            print(f"Cidade: {aluno[7]}")
            print(f"Estado: {aluno[8]}")
            print("-" * 30)

def alterar():
    
    id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_cpf = input("Digite o novo CPF: ")

    sql = f'''
    UPDATE Alunos
    SET nome = '{novo_nome}',
        cpf = '{novo_cpf}'
    WHERE id = {id_aluno}
    '''

    cursor.execute(sql)

    conexao.commit()

    if cursor.rowcount > 0:
        print("Aluno atualizado com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID.")

def alterar():
    listar()
    id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

    sql = f"DELETE FROM Alunos WHERE id = {id_aluno}"

    cursor.execute(sql)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Aluno excluído com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID.")

def excluir():
    listar()
    id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

    sql = f"DELETE FROM Alunos WHERE id = {id_aluno}"

    cursor.execute(sql)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Aluno excluído com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID.")

def menu():
    opcao = 0
    while opcao != 5:
        print("\n---CADASTRO DE ALUNOS---")
        print("\n1-Criar")
        print("2-Listar")
        print("3-Alterar")
        print("4-Excluir")
        print("5-Sair")

        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1: criar_tabela()
        elif opcao == 2: listar()
        elif opcao == 3: alterar()
        elif opcao == 4: excluir()
        elif opcao == 5:
            print("Programa encerrado!")
            break

menu()



def criar_tabela_professor():
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL,
                    escola TEXT,
                    endereco_professor TEXT
                    )''')
    nome_professor = input("Informe o nome do professor: ")
    telefone_professor = input("Informe o telefone do professor: ")
    materia_professor = input("Informe a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("Digite o cpf do professor: ")
    salario_professor = float(input("Digite o salário do professor: "))
    nome_escola = input("Informe o nome da escola: ")
    endereco_professor = input("Digite o endereço do professor: ")
    comando_inserir = (f'''
                    INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, escola, endereco_professor)
                    VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', {idade_professor}, '{cpf_professor}', {salario_professor}, '{nome_escola}', '{endereco_professor}')''')

    cursor.execute(comando_inserir)
    conexao.commit()

def alterar_professor():
    listar()
    id_professor = int(input("Digite o ID do professor que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_cpf = input("Digite o novo CPF: ")

    sql = f'''
    UPDATE Professores
    SET nome = '{novo_nome}',
        cpf = '{novo_cpf}'
    WHERE id = {id_professor}
    '''

    cursor.execute(sql)

    conexao.commit()

    if cursor.rowcount > 0:
        print("Professor atualizado com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")


def excluir_professor():
    listar()
    id_professor = int(input("Digite o ID do professor que deseja excluir: "))

    sql = f"DELETE FROM Professores WHERE id = {id_professor}"

    cursor.execute(sql)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Professor excluído com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")


def menu():
    opcao = 0
    while opcao != 5:
        print("\n---CADASTRO DE PROFESSORES---")
        print("\n1-Criar")
        print("2-Listar")
        print("3-Alterar")
        print("4-Excluir")
        print("5-Sair")

        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1: criar_tabela_professor()
        elif opcao == 2: listar_professor()
        elif opcao == 3: alterar_professor()
        elif opcao == 4: excluir_professor()
        elif opcao == 5:
            print("Programa encerrado!")
            break

menu()

conexao.close() 

