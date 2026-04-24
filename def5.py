vida_inicial = 100
valor_dano = 0 

def sofrer_dano(vida_inicial, valor_dano):
    while vida_inicial != 0:
       valor_dano = float(input("informe o dano causado pelo monstro: "))
       vida_inicial = vida_inicial - valor_dano
       print(f"Saldo de vida atual atualizado: {vida_inicial}")
    print("GAME OVER!")

sofrer_dano(vida_inicial, valor_dano)
