import sqlite3

def verficar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    inf = cursor.fetchall()

    #PORQUE O SEGUNDO PRINT NÃO MOSTRA ABSOLUTAMENTE NADA NO CONSOLE?
    print("Primeiro print:", inf)
    print("Segundo print:", inf)

    conexao.close()

# Como não estava sendo armazenado em nenhuma variável assim que era mostrado no primeiro print ele era esvaziado e consequentemente o segundo print ficaria vazio
# Criando uma variável ele é armazenado nela e pode ser usado quando for preciso, assim no segundo print ele será mostrado