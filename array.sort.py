numeros = [12, 34, 23, 67, 41, 19, 5, 78, 56, 30, 14, 9, 17, 24, 2]

numeros.sort(key=None, reverse=False)

print("Ordem crescente: ", numeros)

numeros.sort(key=None, reverse=True)

print("\n Ordem decrescente: ", numeros)


nome = ["Clara", "José", "Henrique", "Daniela"]
DataNascimento = ["06/06/2010", "25/08/1984","17/02/1993", "30/10/2008"]
CPF =  ["01290381381", "19752476359", "08860943315", "09564381029"]
RG = ["20227813543", "20052452465", "201057826412", "20219391371"]

nome.sort(key=None, reverse=False)
DataNascimento.sort(key=None, reverse=False)
CPF.sort(key=None, reverse=False)
RG.sort(key=None, reverse=False)

print("Ordem crescente:", nome, DataNascimento, CPF, RG)

nome.sort(key=None, reverse=True)
DataNascimento.sort(key=None, reverse=True)
CPF.sort(key=None, reverse=True)
RG.sort(key=None, reverse=True)

print("\n Ordem decrescente:", nome, DataNascimento, CPF, RG)