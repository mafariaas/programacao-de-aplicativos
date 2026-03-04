nivel = int(input("Digite seu nível"))
esferas = int(input("Digite a quantidade de esferas"))

if nivel >= 20 and esferas >= 50:
    print("Habilidade supersalto desbloqueada")
elif nivel < 20 and esferas < 50:
    print("Requisitos insuficientes para a nova habilidade")
elif nivel >= 20 and esferas < 50:
    print("Requisitos insuficientes para a nova habilidade")
elif nivel >= 20 and esferas >= 50:
    print("Requisitos insuficientes para a nova habilidade")
    