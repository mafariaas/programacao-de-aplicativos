import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None
    try:
        #SE A LINHA ABAIXO FALHAR POR FALTA DE PERMISSÃO NA PASTA,
        #O BLOCO 'FINALLY' VAI TENTAR FECHAR ALGO QUE NÃO ABIU. COMO CORRIGIR?
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome, id_escola))
        conexao.commit()
    except sqlite3.Error as e:
        print("Erro técnico:", e)
    finally:
        if conexao:
            conexao.close()
        


# Dava erro porque se a conexão falhasse, o 'finally' tentaria fechar uma variável que nem existia na memória ainda.
# Criar 'conexao = None' no início resolve isso porque garante que a variável exista desde o começo.
# Se o banco não abrir, a variável continua valendo como vazia (None).
# O 'if conexao:' percebe que ela está vazia e não tenta fechar nada, impedindo o erro de acontecer.