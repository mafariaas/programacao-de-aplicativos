def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do programa")
            break
                         
   
menu()

# O código não quebrava, faltava o comando 'break' para encerrar o código