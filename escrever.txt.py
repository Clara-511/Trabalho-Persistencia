arquivo = open("texto.txt", "w")

texto = list()

texto.append("respeitar")
texto.append("\namar")
texto.append("\nproteger")
texto.append("\nconsolar")
texto.append("\nimportar")

arquivo.writelines(texto)

arquivo.close