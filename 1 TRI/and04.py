usuario = input("Digite o seu nome ")
codigo = int(input("Digite o codigo "))

if usuario == "admin" and codigo == 999:
    print("Acesso ao servidor liberado. Sistema online")
else:
    print("Falha na autenticação. Alerta de segurança ligado")
