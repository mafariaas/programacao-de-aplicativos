temperatura = float(input("Digite a temperatura: "))
if temperatura >= 80:
    print("PERIGO! Desligando servidor por superaquecimento. ")
elif temperatura >= 50 < 80:
    print("Alerta: ventoinhas ligadas no maximo")
elif temperatura < 50:
    print("Temperatura estável. Sistema operando normalmente")
    
