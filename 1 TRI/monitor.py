temperatura = float(input("Digite a temperatura atual: "))
if temperatura <= 30:
    print("Clima estável")
else:
     print("Temperatura elevada!")

umidade = float(input("Digite a umidade da estufa: "))
if umidade < 40:
    print("Ligar irrigação!")
else:
    print("Ligar apenas os ventiladores.")