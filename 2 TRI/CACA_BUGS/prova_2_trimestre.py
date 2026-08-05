import sqlite3 

def cadastrar_hopital():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL
        )
    ''')
    try:
        nome_hospital = input("Informe o nome do hospital: ")
        cidade_loc = input("Informe a cidade em que o hospital está localizado: ")
        comando_inserir = "INSERT INTO hospitais (nome, cidade) VALUES (?, ?)"
                           
                            
        print("Hospital cadastrado!")
        cursor.execute(comando_inserir, nome_hospital, cidade_loc)
        conexao.commit()
    except ValueError as e:
        print("Digite apenas nomes! ", e)
    except sqlite3.IntegrityError as e:
        print("Erro! Informações já cadastradas! ", e)

    finally:
        conexao.close()

def cadastrar_medicos():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor() 
    
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        crm INTEGER UNIQUE NOT NULL,
        id_hospital INTEGER,
        FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
        ''')
    try:
        nome_medico = input("Informe o nome do médico: ")
        crm = int(input("Informe o crm do médico: "))
        id_hospital = int(input("Informe o id do hospital em que o médico trabalha: "))
        comando_inserir = "(INSERT INTO medicos (nome, crm, id_hospital) ) VALUES (?, ?, ?)"
                            
        print("Médico cadastrado com sucesso!")
        cursor.execute(comando_inserir, nome_medico, crm, id_hospital)
        conexao.commit()

    except ValueError as e:
        print("Digite apenas números!", e)
    
    except sqlite3.IntegrityError as e:
        print("Erro! Informações já cadastradas! ", e)

    finally:
        conexao.close()


cadastrar_hopital()
cadastrar_medicos()

