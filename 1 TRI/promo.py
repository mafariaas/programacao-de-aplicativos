valor_compra = float(input("Digite o valor da compra"))
cliente = input("É cliente prime? Responda com S/N")
frete = 50.00 

if valor_compra >= 500.00 or (cliente == "S" and valor_compra > 100.00):
    print("Parabens ganhou frete gratis") 
    frete = 0.0 
    print("Valor da compra ficou:" , valor_compra)

valor_total = valor_compra + frete 
print("Valor total" , valor_total)

