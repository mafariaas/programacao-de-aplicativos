print("---SEGURANÇA DA FABRICA---")
prenca_hidraulica = input("Digite se concluiu o curso de segurança com S/N: ")

if prenca_hidraulica == "S": 
     instrutor = input("O instrutor esta presente? Responda com S/N: ")
     if instrutor == "S":
        print("Acesso liberado! Operação iniciada.")
     else:
         print("Aguarde o instrutor para ligar a maquina. ")
else:
    print("Acesso negado faça o treinamento primeiro. ")




    