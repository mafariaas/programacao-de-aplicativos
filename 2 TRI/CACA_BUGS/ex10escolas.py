import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))
    
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,)
        )

        conexao.commit()
        print("Escola deletada!")

    except sqlite3.Error:
        print("Erro: Escola não deletada.")

    finally:
        conexao.close()

deletar_escola_antiga()

# Sem o ? o código entende que não existe uma informação expecífica para deletar e apaga tudo com o comando