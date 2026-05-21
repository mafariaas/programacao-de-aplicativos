import json

alunos = []

def menu():
    nome = input("Informe seu nome a seguir: ")
    cpf = int(input("Digite seu cpf (apenas números, sem símbolos): "))
    tel = int(input("Digite seu número de telefone: "))
    turma = input("informe sua turma: ")
    idade = int(input("Diga a seguir sua idade: "))

def cadastrar_aluno():
    aluno = {
        "nome": nome,
        "CPF": cpf,
        "telefone": tel,
        "turma": turma,
        "idad": idade
    }

def listar_alunos():

def atualizar_dados():

def remover_aluno():

def exibir_menu(menu):
    while menu != 5:
        print("\n1- CADASTRAS ALUNOS")
        print("2- LISTAR ALUNOS")
        print("3- ATUALIZAR DADOS")
        print("4- REMOVER ALUNO")
        print("\n5- SAIR")
 
        menu = int(input("Digite a opção desejada: "))

        if menu == 1:
            

    

