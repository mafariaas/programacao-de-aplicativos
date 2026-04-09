salarios = [2000, 2750, 4400, 1800, 1000]
for s in salarios:
    if s <= 2000.00:
        imposto = s * 0.10
        percentual = "10%"
    else:
        imposto = s * 0.20
    sobra = s - imposto

    print(f"salário {s}, e foi cobrado {percentual}, de imposto")
