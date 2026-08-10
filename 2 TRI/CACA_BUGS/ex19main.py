import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    tabelas_aceitas = ["alunos", "professores", "turma"]

    if nome_tabela not in tabelas_aceitas:
        print("Tabela inexistente!")
        return 

    comand = "SELECT * FROM {nome_tabela} WHERE id = ?" 

    cursor.execute(comand,(id_registro,))

    conexao.commit()

    print(cursor.fetchone())
    conexao.close()

buscar_dados_dinamicos

# O '?' não é aceito pois ele é utilizado para valores e não para parâmetros
# Criar uma lista apenas com as tabelas aceitas e caso a tabela desejada não seja nenhuma, o return fecha a função imediatamente