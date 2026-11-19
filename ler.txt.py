arquivo = open("loremipsum.txt", "r")

conteudo = arquivo.read()

print("Conteúdo completo:", conteudo)

arquivo.close()

arquivo = open("loremipsum.txt", "r")

primeiraLinha = arquivo.readline()
print("\n Primeira linha:", primeiraLinha)

arquivo.seek(0)

tresCaracteres = arquivo.read(3)
print ("\n Primeiros três caracteres:", tresCaracteres)

arquivo.close()

with open("loremipsum.txt", "r") as arquivo:
    conteudoWith = arquivo.read()

print("\n Conteúdo usando with:", conteudoWith)