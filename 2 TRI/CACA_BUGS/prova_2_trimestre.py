import sqlite3 

def cadastrar_hopital():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitais (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL
        )
    ''')

    nome_hospital = input("Informe o nome do hospital: ")
    cidade_loc = input("Informe a cidade em que o hospital está localizado: ")
    print("Hospital cadastrado!")

    cursor.execute("INSERT INTO hospitais")

def cadastrar_medicos():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor() 
     
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER UNIQUE PRIMARY KEY,
        nome TEXT NOT NULL,
        crm INTEGER UNIQUE NOT NULL,
        id_hospital INTEGER,
        FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
        ''')

    nome_medico = input("Informe o nome do médico: ")
    crm = int(input("Informe o crm do médico: "))
    id_hospital = int(input("Informe o id do hospital em que o médico trabalha: "))


