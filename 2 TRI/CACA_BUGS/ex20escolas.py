import sqlite3

def cadastrar_escola_manual():

    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",  (id_escola, nome)
    )

        conexao.commit()
        print("Escola cadastrada!")

    except sqlite3.IntegrityError:
        print("Erro! ID já cadastrado")

    except sqlit3.Error as e:
        print("Erro no banco de dados", e)

    finally:
        conexao.close()

cadastrar_escola_manual()

# Para tratar o erro usamos o try para inserir na tabela escola e except para caso tentem utilizar o mesmo id 