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
        

# Dava erro pois a conexão tem possibilidade de dar erro e se der, o finally fecha algo com erro
# Então adicionamos uma variável de conexão vazia