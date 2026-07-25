import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema.escola_db')
    cursor = conexao.cursor()

    #O SQLITE ACUSA O ERRO DE SINTAXE PRÓXIMO AO FOREN KEY. CADÊ O ERRO?
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS turmas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_turma TEXT,
                    id_serie INTEGER,
                    FOREIGN KEY (id_serie) REFERENCES series(id)
                    )''')

    conexao.commit()
    conexao.close()


# O erro estava em 'id_serie' que estava sem a palavra 'INTEGER' ou seja não definia o que aquela variável era, por isso dava erro de sintaxe