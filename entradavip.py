idade = int(input("Digite sua idade: "))
ingresso = input("Digite se possui o ingreso com S/N: ")
lista_de_convidados = input("Digite se esta na lista de covidados com S/N: ")

if (idade >= 18 and ingresso == "S") or lista_de_convidados == "S":
   print("Acesso liberado, aproveite!")
else: 
    print("Acesso negado")