import sqlite3

conexao = sqlite3.connect('reserva_laboratorio.db')
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS laboratorio_01(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        
    )
