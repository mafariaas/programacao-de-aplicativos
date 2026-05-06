valor_da_compra = float(input("Digite o valor total"))
cupom = input("Digite o nome do cupom")

desconto = valor_da_compra * 0.10
total = valor_da_compra - desconto


if cupom == "DEV10":
    print("Novo valor: ", total)
else:
    print("Cupom inválido. Valor original: R$" , valor_da_compra)
