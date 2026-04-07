lista_vip = []
nome = ""
while nome != "fim":
    nome = input("Digite seu nome (Ou 'fim' para encerrar ): ")
    if nome != "fim":
        if nome[0] == "A":
            lista_vip.append(nome)
            print("Lista VIP:", lista_vip)
        else:
            print("Apenas nomes com A são permitidos no VIP!")
print("Encerrando programa...")