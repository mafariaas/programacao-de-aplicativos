numeros =  [1, 3, 8, 12, 15, 23, 7, 9, 31, 5]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Listas")
print("Lista de numeros: ", numeros)
print("Lista de numeros pares: ", pares)
print("Lista de numeros impares: ", impares)