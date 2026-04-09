num = int(input("Digite um valor para tabuada de 1 a 10: "))
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"tabuada do {num}")

for numero in lista_numeros:
    resultado = num * numero
    print(f"{num} x {numero} = {resultado}")
