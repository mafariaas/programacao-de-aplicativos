usuario = input("Digite seu usuario")
senha = int(input("Digite sua senha"))

if (usuario == "adimin" or "root") and senha == 12345:
    print("Acesso liberado")
else: 
    print("Acesso negado")

