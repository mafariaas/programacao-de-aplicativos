cliente = input("Nome do cliente: ")
valor_original = float(input("Valor da compra: R$ "))
distancia = int(input("Distancia (km): "))
tem_cupom = input("Possui cupom? (S/N): ")

desconto = 0.0

if valor_original >= 1000.0 and tem_cupom == "S":
    desconto = valor_original * 0.20
elif valor_original > 500.0 and tem_cupom == "S":
    desconto = valor_original * 0.10

valor_com_desconto = valor_original - desconto 

frete = 40.0
if distancia <= 50 and valor_com_desconto > 200.0:
    frete = 0.0

total_final = valor_com_desconto + frete 

print("-" * 30)
print("RELATORIO DE COMPRA - ", cliente)
print("Valor original: R$ ", valor_original)
print("Desconto: R$ ", frete)
print("Frete: R$ ", frete)
print("TOTAL A PAGAR: R$ ", total_final)

if desconto == (valor_original * 0.20):
    print("SURPRESA: VOCÊ GANHOU UM MOUSEPED GAMER DE BRINDE")
    
