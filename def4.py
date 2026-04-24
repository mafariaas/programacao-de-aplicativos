nomes = ["Banana", "Maçã", "Laranja", "Mamão", "Abacaxi", "Melancia", "Manga", "Uva", "Abacate", "Morango"]
busca = input("Digite a fruta que deseja buscar na lista: ")

def esta_na_lista(frutas, buscar):
    for item in frutas:
        if item == buscar:
            return "Encontrado!" 
    return "Não encontrado!"   



msg = esta_na_lista(nomes, busca)
print(msg)

                
            