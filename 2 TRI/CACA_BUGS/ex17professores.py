import sqlite3

def inserir_professor(nome, materia, cpf):
    try:
        conexao = sqlite3.connect('siatema-escola.db')
        cursor = conexao.cursor()
        # Existe um erro de digitação no comando SQL (INSERTO). 
        # Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
        conexao.commit()
    except sqlite3.Error as e:
        print("Erro: Este CPF já está cadastrado no sistema!", e)   
    finally: 
        conexao.close()      

nome = input("Digite o nome desejado: ")
materia = input("Digite a matéria: ")
cpf = input("Informe o cpf: ")

inserir_professor(nome, materia, cpf)