ID = int(input("Qual p seu ID? "))
temperatura = float(input("Qual a temperatura? "))
tempo_uso = int(input("Qual o tempo de uso? "))

if (ID % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"Funcionário {ID}, você foi escalado para a manutenção preventiva hoje.")
else:
        print(f"Funcionário {ID}, sua máquina opera dentro dos padrões normais.")