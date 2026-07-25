import sqlite3

def buscar_professores(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O python reclama de "Incorrect number of bindings".
    # Estamos passando a variável, por que ocorre o erro?
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close

# O erro acontece pois faltava uma vírgula dentro do SELECT porque ele só executa com duas variáveis e para "burlar" isso utilizamos a vírgula