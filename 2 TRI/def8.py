usuario = input("Digite o nome de usuário: ")

def contar_caracteres(nome):
    while len(nome) < 5: 
        print("Nome de usuário muito curto!")
        nome = input("Digite o nome de usuário: ")
    print("Nome cadastrado com sucesso!")

contar_caracteres(usuario)