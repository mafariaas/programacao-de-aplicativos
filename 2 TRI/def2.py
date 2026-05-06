perg = input("Digite sua senha: ")

def senha_valida(senha):

    while len(senha) < 6:
        senha = input("Digite sua senha: ")
    print("Senha cadastrada com sucesso!")

senha_valida(perg)


