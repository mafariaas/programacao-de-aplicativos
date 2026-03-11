print("---OPERADOR DE PRENSA HIDRAULICA---")
curso = input("Você concluiu o curso de segurança? S/N: ")

if curso == "S":
    instrutor = input("O instrutor está na sala? S/N: ")
    if instrutor == "S":
        print("Acesso liberado. Operação iniciada.")
    else:
        print("Aguarde o instrutor para ligar a máquina.")
else:
    print("Acesso negado! Faça o treinamento primeiro.")
