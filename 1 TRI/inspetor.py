print("---INSPETOR DE QUALIDADE---")

comprimento_da_peca = input("Digite se a peça possui o comprimento de 12cm ou 10cm com S/N: ")

if comprimento_da_peca == "S":
    largura = input("Digite se a largura est entre 5cm ou 6cm com S/N: ")
    if largura == "S":
        print("---PEÇA APROVADA!---") 
    else: 
        print("PEÇA REPROVADA! Problemas com a largura.  ")
else:
    print("PEÇA REPROVADA! Problamas com o comprimento.  ")
    
       


