import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
                ALTER TABLE alunos ADD COLUMN estado_aluno
''')

conexao.commit()
conexao.close()