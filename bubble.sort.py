def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                var = array[j]
                array[j] = array[j + 1]
                array[j + 1] = var

numeros = [12, 34, 23, 67, 41, 19, 5, 78, 56, 30, 14, 9, 17, 24, 2]
bubblesort(numeros)

print("Array ordenado: ", numeros)