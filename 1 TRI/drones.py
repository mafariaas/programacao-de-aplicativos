drone = int(input("Digite o código do drone: "))
autorizacao = input("Possui autorização da torre? S/N: ")

if drone == 999 or autorizacao == "S":
    print("Pouso autorizado")

    print("-----------------------------")

    bateria = int(input("Qual a bateria do drone: "))
    clima = input("Qual o clima ensolarado/chuvoso: ")
    vento = int(input("Qual a velocidade dos ventos: "))

    if bateria < 10:
        print("AUTORIZE O POUSO IMEDIATAMENTE! ")

    elif bateria >= 10:
        if (clima == "ensolarado" and vento < 30) or(clima == "chuvoso" and vento < 10):
                print("POUSO AUTORIZADO: Iniciando descida")
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas.")
else:
        print("ERRO 01: Drone não identificado. Retornando à base. " )






