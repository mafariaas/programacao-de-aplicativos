import json # Traz para o seu programa uma biblioteca pronta que sabe como salvar e ler arquivos de texto do tipo JSON.
import os # Ele permite que o programa descubra se um arquivo existe, crie pastas ou apague arquivos no computador.

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
        return # encerra a função

    for aluno in alunos: # percorre item por item da lista 'alunos'
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # mostra no terminal "Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}" com todas as informações ditas pelo usuario anteriormente

def atualizar(): #  função de atualizar
    print("\n--- Atualizar Aluno ---") # mostra --- Atualizar Aluno --- no terminal 
    if not os.path.exists(BANCO_DADOS): # serve para verificar se o arquivo não existe 
        print("Nenhum aluno cadastrado no sistema.") # mostra no terminal "Nenhum aluno cadastrado no sistema."
        return # encerra a função 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  # abre o arquivo na função read (leitura)
        alunos = json.load(f)  # lê o arquivo 
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ") # variável para informar o cpf que deseja atualizar
    
    for aluno in alunos: # percorre item por item da lista
        if aluno['cpf'] == cpf_busca: #Verifica se o CPF do aluno atual é igual ao CPF que está sendo procurado.
            print(f"Editando dados de: {aluno['nome']}") #Mostra na tela o nome do aluno que foi encontrado para edição.
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] #Atualiza o nome do aluno 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #Atualiza o telefone 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # Atualiza a turma 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) #Atualiza a idade 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] #Atualiza o CPF 

            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo na função write para subscrever
                json.dump(alunos, f, indent=4, ensure_ascii=False) #subscreve no arquivo
            print("Dados atualizados com sucesso!") # mostra no terminal "Dados atualizados com sucesso!"
            return # Interrompe a execução da função
            
    print("Aluno não encontrado.") # mostra a menssagem "Aluno não encontrado." caso os dados não existam 

def excluir(): #função de excluir
    print("\n--- Excluir Aluno ---") # mostra --- Excluir Aluno --- no terminal
    if not os.path.exists(BANCO_DADOS): # caso os dados não existam no arquivo
        print("Nenhum aluno cadastrado no sistema.") # mostra "Nenhum aluno cadastrado no sistema."
        return # encerra imediatamente a função 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo na função read (ler)
        alunos = json.load(f) # lê o arquivo
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ") #comando para pedir ao usuario digitar o cpf que deseja remover
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca] #  Copia todos os alunos para a nova lista, exceto o CPF buscado.
    if len(nova_lista) < len(alunos): # se a nova_lista for maior que a antiga ele vai verificar 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #comando para abrir o arquivo no modo de sobrescrever
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # escreve no arquivo
        print("Aluno removido com sucesso!") # mostra a frase "Aluno removido com sucesso! no terminal
    else:
        print("Aluno não encontrado.") # caso a lista de alunos não seja maior que a nova_lista significa que o cpf não existe e mostra "Aluno não encontrado." no terminal 

def menu(): #função para mostrar o menu 
    if not os.path.exists(BANCO_DADOS): #  verifica se o arquivo ainda não existe 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # comando para abrir o arquivo no modo write (escrita) para começar do zero
            json.dump([], f) #escreve no arquivo começando com uma lista vazia 

    while True: # loop que so para quando a informação for falsa
        print("\n=== SISTEMA ESCOLAR ===") # mostra no terminal "\n=== SISTEMA ESCOLAR ==="
        print("1. Cadastrar Aluno") #mostra no terminal "1. Cadastrar Aluno"
        print("2. Listar Alunos") #mostra no terminal "2. Listar Alunos"
        print("3. Atualizar Aluno") #mostra no terminal "3. Atualizar Aluno"
        print("4. Excluir Aluno") #mostra no terminal "4. Excluir Aluno"
        print("5. Sair") #mostra no terminal "5. Sair"
        
        opcao = input("Escolha uma opção: ") # pede para o usuario digitar a opção desejada
        
        if opcao == '1': cadastrar() # caso o usuario digite 1 o programa executa a função de cadastrar
        elif opcao == '2': listar() # caso o usuario digite 2 o programa executa a função de listar
        elif opcao == '3': atualizar() # caso o usuario digite 3 o programa executa a função de atualizar
        elif opcao == '4': excluir() # caso o usuario digite 4 o programa executa a função de excluir
        elif opcao == '5': break # caso o usuario digite 5 break quebra o loop e encerra o programa
        else: print("Opção inválida!") # caso o usuario digite 6 mostra no terminal "Opção inválida!" pois não existe função para essa opção

menu() #chama a função menu