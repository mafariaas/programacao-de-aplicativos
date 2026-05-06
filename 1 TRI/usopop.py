pendentes = ["Relatório.pdf", "Foto.png", "Planilha.xlsx"]
print("Lista de pendentes", pendentes)
concluidos = []
print("Lista de concluídos",concluidos)
print("----------------------")
remove = pendentes.pop(0)
concluidos.append("Relatório.pdf")
print(f"Lista de pendentes", pendentes)
print(f"Lista de concluidos", concluidos)
