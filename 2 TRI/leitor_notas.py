# import json

# with open("notas.json", "r", encoding="utf-8") as arquivo:
#     dados = json.load(arquivo)

# soma = dados["matemática"] + dados["portugues"]

# print("Soma das notas:", soma)




import json

nome = input("Digite seu nome: ")

aluno = {
    "nome": nome,
    "matemática": 9.5,
    "português": 9.0,
    "soma": 0
}

soma_valor = aluno["matemática"] + aluno["português"]

aluno ["soma"] = soma_valor

with open("notas.json", 'a', encoding="utf-8") as arquivo: 
    json.dump(aluno, arquivo, ensure_ascii=False)
