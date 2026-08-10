import sqlite3

def criar_tabela_aluno():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_serie INTEGER,
        FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')
    conexao.close()
    
def vincular_aluno_turma():
    
    try:
        nome = input("Nome do aluno: ")
        id_serie = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO alunos (nome, id_serie) VALUES (?, ?)", (nome, id_serie))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")

    except ValueError:
        print("Erro! Digite apenas o número do ID!")
    except sqlite3.Error as e:
        print("Erro no banco de dados!", e)
    finally:
        conexao.close()

vincular_aluno_turma()
criar_tabela_aluno()

# O id é um INT, o except dado para tratar erros corrige apenas erros internos do banco de dados,
# para resolver isso adicionamos outro except que capture erros de valor, 'ValueError'