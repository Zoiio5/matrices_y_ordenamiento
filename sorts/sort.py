import random

def generar_lista_aleatoria(tamaño, rango):
    return [random.randint(0, rango) for _ in range(tamaño)]

def imprimir_lista(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Ejemplo de uso1
tamaño_lista = 10
rango_valores = 100
arr = generar_lista_aleatoria(tamaño_lista, rango_valores)
print("Lista aleatoria generada:")
imprimir_lista(arr)
sorted(arr)
print("Lista ordenada:")
imprimir_lista(arr)
