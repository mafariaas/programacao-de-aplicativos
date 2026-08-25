import sqlite3 
conexao = sqlite3.connect('sistema_academia.db')
cursor = conexao.cursor()

def criar_tabelas():
    conexao = sqlite3.connect('sistema_academia.db')
    cursor = conexao.cursor()
    conexao = None

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS redes_academia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_rede TEXT NOT NULL,
                plano_master TEXT NOT NULL
        )
    ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                localizacao TEXT NOT NULL, 
                id_rede INTEGER,
                FOREIGN KEY (id_rede) REFERENCES redes_academia(id)
        )
    ''')  

    except sqlite3.Error as e:
        print("Erro no banco de dados!", e) 

    finally:
        if conexao:
            conexao.commit() 
            conexao.close()

criar_tabelas()

def cadastrar_redes():
    try:
        nome_d_redes = input("Insira o nome da rede de academia: ")
        plano_master = input("Informe o nome do plano: ")
        comando_inserir = "INSERT INTO redes_academia (nome_rede, plano_master) VALUES (?, ?)"

        print("Cadastro concluido!")
        cursor.execute(comando_inserir, nome_d_redes, plano_master)
        conexao.commit()

    except ValueError as e:
        print("Digite apenas nomes! ", e)
    except sqlite3.IntegrityError as e:
        print("Erro! Informações já cadastradas! ", e)

    finally:
        conexao.close()   

def listar_redes():
    cursor.execute("SELECT * FROM redes_academia")

    info_redes = cursor.fetchall()

    print("=== REDES CADASTRADASTRADAS ===")

    if not info_redes:
        print("Nenhuma informação encontrada!")

    else:
        for inf in info_redes:
            print(f"ID: {inf[0]}")
            print(f"Rede: {inf[1]}")
            print(f"Plano: {inf[2]}")

def atualizar_redes():
    listar_redes()

    try:
        id_rede = int(input("Insira o id da rede que deseja alterar: "))
        nova_rede = input("Informe o nome da nova rede: ")
        novo_plano = input("Informe o novo plano: ")
        cursor.execute("UPDATE redes_academia SET nome_rede = ?, plano_master = ? WHERE id = ?", (nova_rede, novo_plano, id_rede))

        conexao.commit()
        print("Nome atualizado com sucesso!")

    except sqlite3.Error as e:
        print("Não foi possivel atualizar!", e)

    finally:
        conexao.close()
    
    
def excluir_redes():
    listar_redes()


    try:
        id_rede = int(input("Informe o id da escola que deseja excluir: "))
        cursor.execute("DELETE FROM redes_academia WHERE id = ?", (id_rede,))


        conexao.commit()
        print("Rede deletada com sucesso!")

    except sqlite3.Error as e:
            print("Erro: Escola não deletada.", e)

    finally:
        conexao.close()
            

def menu_redes():
    opcao = 0
    while opcao != 5:
        print("\n---CADASTRO DE REDES---")
        print("\n1-Cadastrar")
        print("2-Listar")
        print("3-Atualizar")
        print("4-Deletar")
        print("5-Sair")

        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1: cadastrar_redes()
        elif opcao == 2: listar_redes()
        elif opcao == 3: atualizar_redes()
        elif opcao == 4: excluir_redes()
        elif opcao == 5:
            print("Programa encerrado!")
            break
menu_redes()

def cadastrar_unidades():
    conexao = sqlite3.connect('sistema_academia.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")
                   
    try:
        localizacao = input("Insira a localização da unidade: ")
        id_rede = int(input("Informe o id da rede: "))
        comando_inserir = "INSERT INTO unidades (localizacao, id_rede) VALUES (?, ?)"

        print("Cadastro concluido!")
        cursor.execute(comando_inserir, localizacao, id_rede)
        conexao.commit()

    except ValueError as e:
        print("Digite apenas nomes! ", e)
    except sqlite3.IntegrityError as e:
        print("Erro! Informações já cadastradas! ", e)

    finally:
        conexao.close()

def listar_unidades():
    cursor.execute("SELECT * FROM unidades")

    info_unidades = cursor.fetchall()

    print("=== UNIDADES CADASTRADASTRADAS ===")

    if not info_unidades:
        print("Nenhuma informação encontrada!")

    else:
        for inf in info_unidades:
            print(f"ID: {inf[0]}")
            print(f"Localização: {inf[1]}")

def atualizar_unidades():
    listar_redes()

    try:
        id_unidade = int(input("Insira o id da unidade que deseja alterar: "))
        nova_localizacao = input("Informe a nova localização: ")
        cursor.execute("UPDATE unidades SET localizacao = ? WHERE id", (nova_localizacao, id_unidade))

        conexao.commit()
        print("Unidade atualizada com sucesso!")

    except sqlite3.Error as e:
        print("Não foi possivel atualizar!", e)

    finally:
        conexao.close()

def excluir_unidades():
    listar_redes()


    try:
        id_unidade = int(input("Informe o id da unidade que deseja excluir: "))
        cursor.execute("DELETE FROM unidades WHERE id_unidade = ?", (id_unidade,))

        conexao.commit()
        print("Unidade deletada com sucesso!")

    except sqlite3.Error as e:
            print("Erro: unidade não deletada.", e)

    finally:
        conexao.close()

def menu_unidades():
    opcao = 0
    while opcao != 5:
        print("\n---CADASTRO DE UNIDADES---")
        print("\n1-Cadastrar")
        print("2-Listar")
        print("3-Atualizar")
        print("4-Deletar")
        print("5-Sair")

        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1: cadastrar_unidades()
        elif opcao == 2: listar_unidades()
        elif opcao == 3: atualizar_unidades()
        elif opcao == 4: excluir_unidades()
        elif opcao == 5:
            print("Programa encerrado!")
            break
menu_unidades()





