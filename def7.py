largura = int(input("Digite a largura do terreno: "))
comprimento = int(input("Digite o comprimento do terreno: "))
area = largura * comprimento
contador = 0 

def calcular_area(largura, comprimento):
    while contador < 3:
        largura = int(input("Digite a largura do terreno: "))
        comprimento = int(input("Digite o comprimento do terreno: "))
        area = largura * comprimento
        print()
    print("Encerrando programa...")

