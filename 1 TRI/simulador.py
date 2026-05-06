saldo_inicial = 1000.0 
print("1")
print("2")
print("3")
menu = input("Escolha 1 para depósito, 2 para saque ou 3 para extrato: ")


if menu == "1":
    valor = float(input("Digite o valor: "))
    if valor > 0.00: 
        total = valor + saldo_inicial
        print("O valor total do saldo após o deposito é de: ", total)

elif menu == "2":
    valor = float(input("Digite o valor: "))
    if valor > 0 and ( valor <= saldo_inicial or valor == 100.0):
        print("Saque realizado ")


elif menu == "3":
    print("Seu saldo atual é", saldo_inicial)