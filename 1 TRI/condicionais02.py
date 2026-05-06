poder_de_ataque = int(input("Digite os pontos"))
poder_de_defesa = int(input("Digite os pontos"))
dano = poder_de_ataque - poder_de_defesa

if dano <= 0:
    print("O vilão bloqueou o ataque! Dano = 0 ")
elif dano > 0:
    print("Ataque crítico! Você causou dano ao vilão de", dano)
    