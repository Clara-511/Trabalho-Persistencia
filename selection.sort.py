numeros = [12, 34, 23, 67, 41, 19, 5, 78, 56, 30, 14, 9, 17, 24, 2]

for i in range(len(numeros)):
    min = i
    for j in range(i + 1, len(numeros)):
        if numeros[min] > numeros[j]:
          min = j
          var = numeros[i]
          numeros[i] = numeros[min]
          numeros[min] = var

print("Array ordenado:", numeros)