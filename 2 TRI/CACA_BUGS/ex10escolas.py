import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Esse comando vai apagar o banco inteiro se o aluno não prestar atenção.
    cursor.execute(f"DELETE FROM escolas WHERE id? = {id_escola}")

    conexao.commit()
    conexao.close()

# Estava sem o ponto de interrogação que mostra o que tem que ser apagado
# Estava sem o 'f' e as chaves para mostrar a variável 'id_escola'