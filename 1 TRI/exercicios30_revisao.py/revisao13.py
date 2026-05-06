senha_correta = "1234"
tentativas = 0
acertou = False

while tentativas < 3 and acertou == False:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido")
        acertou = True
    else:
        print("Senha incorreta")
        tentativas = tentativas + 1

if acertou == False:
    print("Acesso bloqueado")