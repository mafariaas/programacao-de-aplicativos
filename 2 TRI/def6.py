velocidade_km = int(input("Digite a velocidade: "))
velocidade_ms = velocidade_km / 3.6 

def converter_km_para_ms(velocidade_km, velocidade_ms):
    velocidade_ms = velocidade_km / 3.6 
    if velocidade_km > 80: 
        print("Reduza a velocidade!")
        return f"Sua velocidade em m/s é {velocidade_ms}"

    return f"Sua velocidade em m/s é {velocidade_ms}"

msg = converter_km_para_ms(velocidade_km, velocidade_ms)
print(msg)

    
