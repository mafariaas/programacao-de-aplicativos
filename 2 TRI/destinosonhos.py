def criar_arquivo():
    open('viagens.txt' , 'w').close()

def add():
    destino = input("Digite os lugares que deseja visitar: ")
    with open('viagens.txt' , 'a') as m:
        m.write(destino + '\n')
    print("Lugares cadastrados!")

def ler():
    with open('viagens.txt' , 'r') as m:
        lugares = m.readlines()

        i = 0
        for lugar in lugares:
            print(f"\n{i} - {lugar.strip()}")
            i += 1

def atualizar():
    ler()
    idx = int(input("Digite o id do lugar que deseja alterar: "))
    novo_lugar = input("Novo lugar: ")

    with open('viagens.txt' , 'r') as m:
        linhas = m.readlines()


    linhas[idx] = novo_lugar + '\n'

    with open('viagens.txt' , 'w') as m:
        m.writelines(linhas)
        print("Lugar atualizado com sucesso!")

def deletar():
    ler()
    idx = int(input("Digite o ID do lugar que deseja excluir: "))
    
    with open('viagens.txt', 'r') as m:
        linhas = m.readlines()
    
    del linhas[idx]
    
    with open('viagens.txt', 'w') as m:
        m.writelines(linhas)
    print("Lugar removido!")

while True:
    print("\n---PLANEJADOR DE VIAGENS---")
    print("\n1-Adicionar destino")
    print("2-Listar Sugestões")
    print("3-Editar Sugestão")
    print("4-Remover Sugestão")
    print("5-Sair")

    opcao = input("\nEscolha: ")

    if opcao == '1': add()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5':
        print("Programa encerrado!")
        break


