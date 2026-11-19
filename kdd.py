import time

palavras = list()

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())


def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j].lower() > array[j + 1].lower():
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

def selectionsort(array):
    for i in range(len(array)):
        menor = i

        for j in range(i + 1, len(array)):
            if array[menor].lower() > array[j].lower():
                menor = j

        temp = array[i]
        array[i] = array[menor]
        array[menor] = temp


lista_bubble = palavras.copy()

inicio = time.perf_counter()
bubblesort(lista_bubble)
fim = time.perf_counter()

print("BUBBLE SORT:")
print(" ".join(lista_bubble))
print("Tempo:", fim - inicio, "segundos\n")

lista_selection = palavras.copy()

inicio = time.perf_counter()
selectionsort(lista_selection)
fim = time.perf_counter()

print("SELECTION SORT:")
print(" ".join(lista_selection))
print("Tempo:", fim - inicio, "segundos\n")

lista_sort = palavras.copy()

inicio = time.perf_counter()
lista_sort.sort(key=str.lower)
fim = time.perf_counter()

print("SORT:")
print(" ".join(lista_sort))
print("Tempo:", fim - inicio, "segundos")
