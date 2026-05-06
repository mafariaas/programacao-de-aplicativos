texto = str(input("Digite seu cargo aqui:"))
codigo = int(input("Digite seu cóigo aqui:"))
botao_pressionado = input("Botão de emergência pressionado? Responda com S/N:")
equipamento_de_protecao = input("Está com o EPI completo? Responda com S/N:")

if (texto == "engenheiro" or "tecnico") and codigo == "1234" or botao_pressionado  == "S": 
    print("Acesso liberado")

else:
    print("Acesso negado! Risco de segurança")


