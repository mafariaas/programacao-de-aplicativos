import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    # Se o usuário digitar "Turma B" em vez do número do ID, o sistema quebra.
    # O try/except abaixo falhou em capturar esse erro. Qual o problema? 
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except ValueError:
        print("Erro! Digite apenas o número do ID!")
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        conexao.close()

# O erro acontece porque o except tratava apenas erros do proprio banco de dados, e quando se trata de operação inválida para a operação se utiliza 'ValueError'
# Então adicionamos um except de ValueError e dessa forma o código não é quebrado