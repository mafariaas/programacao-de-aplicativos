garrafas = int(input("Qual o total de garrafas que ja passaram pela esteira: "))

if garrafas == 500:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")
    print("CONTROLE DE QUALIDADE: Retire a amostra para o teste! ")

if garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente! ")

elif garrafas % 100 == 0:
    print("CONTROLE DE QUALIDADE: Retire a amostra para o teste! ")

elif garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente! ")

else:
    print(f"Produção em dia. Garrafa número {garrafas} processada.")
