senha = input("Digite sua senha: ")
numero_tentativa = int(input("Digite o número da tentativa atual: "))
token = input("Possui token especial VIP? Responda com S/N: ")

if (senha == "admin123") and (numero_tentativa % 3 == 0 or token == "S"):
    print(f"Tentativa n° {numero_tentativa}: ACESSO CONCEDIDO!")
else:
    print(f"Tentativa n° {numero_tentativa}: ACESSO BLOQUEADO POR PROTOCOLO")
