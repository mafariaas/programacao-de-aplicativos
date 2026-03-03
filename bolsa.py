media_escolar = float(input("Digite sua media " ))
renda_familiar = float(input("Digite sua renda" ))
escola = input("É de escola publica? responda com S/N" )

if (media_escolar >= 8.0 and renda_familiar <= 2.000) or escola == "S" :
    print("Parabens ganhou a bolsa!")
else: 
    print("Infelizmente não ganhou bolsa!")

