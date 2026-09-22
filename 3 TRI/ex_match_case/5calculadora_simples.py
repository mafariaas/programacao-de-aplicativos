num_1 = int(input("Informe um número inteiro: "))
num_2 = int(input("Informe outro número inteiro: "))

ask = input("informe a operacão desejada (+ ou -): ")

match ask:
    case "+":
        print("Resultado:", num_1 + num_2)
    case "-":
        print("Resultado:", num_1 - num_2)
    case _:
        print("Operação inválida!")
        