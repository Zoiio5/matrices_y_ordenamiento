import random

# Algoritmo de Merge Sort
def mergesort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        mitad_izquierda = lista[:medio]
        mitad_derecha = lista[medio:]

        mergesort(mitad_izquierda)
        mergesort(mitad_derecha)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1
    return lista