import json #impportar o arquivo
import os

BANCO_DADOS = 'alunos.json' #definiu a variavel BANCO_DADOS com o arquivo .json 

def cadastrar(): #função para cadastrar
    print("\n--- Novo Cadastro ---") # mostra --- Novo Cadastro --- no terminal
    
    if os.path.exists(BANCO_DADOS): #comando para verificar se o arquivo existe 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo na função read (leitura)
            alunos = json.load(f) # lê o arquivo 
    else:
        alunos = [] #cria uma lista vazia com o nome 'alunos'

    novo_aluno = {                                 #criação do objeto
        "nome": input("Nome: "), #chave para nome
        "telefone": input("Telefone: "),  #chame para telefone
        "turma": input("Turma: "),           #chave para turma  
        "idade": int(input("Idade: ")),      #chave para idade
        "cpf": input("CPF: ")             #chave para cpf
    }
    
    alunos.append(novo_aluno) #adiciona as informações fornecidas no objeto na lista 'alunos'

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:   #abre o arquivo na função write (escrever)
        json.dump(alunos, f, indent=4, ensure_ascii=False)  # escreve no arquivo
        
    print("Aluno cadastrado com sucesso!") # mostra "Aluno cadastrado com sucesso!" no terminal

def listar(): #função para lista 
    print("\n--- Lista de Alunos ---") # mostra --- Lista de Alunos --- no terminal
    
    if os.path.exists(BANCO_DADOS): #comando para verificar se o arquivo existe 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo na função read (leitura)
            alunos = json.load(f)  # lê o arquivo 
    else:
        alunos = [] #cria uma lista vazia com o nome 'alunos'

    if not alunos: # se os dados não existirem
        print("Nenhum aluno cadastrado.") # mostra no terminal aluno não cadastrado
        return #?

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

def atualizar(): #  função de atualizar
    print("\n--- Atualizar Aluno ---") # mostra --- Atualizar Aluno --- no terminal 
    if not os.path.exists(BANCO_DADOS): # verifica se os dados existem no arquivo, se não
        print("Nenhum aluno cadastrado no sistema.") # mostra no terminal "Nenhum aluno cadastrado no sistema."
        return #?

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  # abre o arquivo na função read (leitura)
        alunos = json.load(f)  # lê o arquivo 
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ") # variável para informar o cpf que deseja atualizar
    
    for aluno in alunos: # percorre item por item da lista
        if aluno['cpf'] == cpf_busca: # se a chave cpf no objeto aluno for igual ao cpf buscado
            print(f"Editando dados de: {aluno['nome']}") # mostra no terminal "Editando dados de: {aluno['nome']}"
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
              # atualiza os dados antigos pelos novos fornecidos pelo usuario

            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo na função write para subscrever
                json.dump(alunos, f, indent=4, ensure_ascii=False) #subscreve no arquivo
            print("Dados atualizados com sucesso!") # mostra no terminal "Dados atualizados com sucesso!"
            return
            
    print("Aluno não encontrado.") # mostra a menssagem "Aluno não encontrado." caso os dados não existam 

def excluir(): #função de excluir
    print("\n--- Excluir Aluno ---") # mostra --- Excluir Aluno --- no terminal
    if not os.path.exists(BANCO_DADOS): # caso os dados não existam no arquivo
        print("Nenhum aluno cadastrado no sistema.") # mostra "Nenhum aluno cadastrado no sistema."
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo na função read (ler)
        alunos = json.load(f) # lê o arquivo
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()