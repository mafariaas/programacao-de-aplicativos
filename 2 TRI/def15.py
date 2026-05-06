rua = input("Digite o nome da sua rua: ")
numero = int(input("Digite o número da sua casa: "))
bairro = input("Digite o bairro que você mora: ")
cep = int(input("Digite seu cep: "))
cidade = input("Digite o nome da sua cidade: ")

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"Rua {rua}, N° {numero}, Bairro {bairro}, cep {cep} e cidade {cidade}"

informacoes = gerar_etiqueta(rua, numero, bairro, cep, cidade)
print(informacoes)
