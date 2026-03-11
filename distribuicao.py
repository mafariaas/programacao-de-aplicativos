print("---DIVISÃO DE CARGAS---")

codigo_pacote = int(input("Digite o codigo: "))
peso = float(input("Digite o peso: "))

print("----------------------------")


if peso < 5 and (codigo_pacote % 10 == 0):
    print(f"Pacote {codigo_pacote}: ENTREGA EXPRESSA.")
elif peso > 50:
    print(f"Pacote {codigo_pacote}: CAIXA PESADA.")
else:
    print("Informações inválidas!")
