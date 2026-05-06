media = float(input("Digite sua media final: "))
presenca = int(input("Digite sua porcentafgem de presença: "))

if media >= 7.0 and presenca >= 75:
    print("Parabens! Aprovado")
elif media < 7.0 and presenca < 75:
    print("Reprovado! Verifique sua nota ou frequencia")
elif media >= 7.0 and presenca < 75:
    print("Reprovado! Verifique sua nota ou frequencia")
elif media <= 7.0 and presenca <= 75:
    print("Reprovado! Verifique sua nota ou frequencia")