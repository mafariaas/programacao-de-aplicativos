def situacao_aluno(media):
 	if media >= 6:
     	return "Aprovado"
 	return "Reprovado"

 assert situacao_aluno(8) == "Aprovado"
 assert situacao_aluno(6) == "Aprovado"
 assert situacao_aluno(5.9) == "Reprovado"
 assert situacao_aluno(0) == "Reprovado"
 assert situacao_aluno(10) == "Aprovado"

 # Crie testes para as médias: 6, 5.9, 0 e 10.
 # Os valores 6 e 5.9 são chamados de limite pois são valores proximos do pedido.

