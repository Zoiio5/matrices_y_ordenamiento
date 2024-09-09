import random

# Algoritmo de Insertion Sort

def insertionsort(array):
    for i in range(1, len(array)):
        clave = array[i]
        j = i - 1
        while j >= 0 and clave < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = clave
    return array