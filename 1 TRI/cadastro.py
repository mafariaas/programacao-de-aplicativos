usuarios = ["admin", "convidado", "suporte", "teste"]
print("Lista de usuarios",usuarios)
print("--------------------------------------------------")
usuarios.remove("teste")
print("A lista foi atualizada:", usuarios)
print("--------------------------------------------------")
del usuarios[0]
print("A lista usuários foi atualizada novamente:", usuarios)
