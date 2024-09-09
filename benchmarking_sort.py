import random
import time

import sorts.mergesort as mergesort
import sorts.quicksort as quicksort
import sorts.insertionsort as insertionsort

# Generación de una lista aleatoria
def generar_lista_aleatoria(tamaño, rango):
    return [random.randint(0, rango) for _ in range(tamaño)]

# Benchmark de algoritmos de ordenamiento
def benchmark_sorting_algorithms():
    tamaños = [100, 1000, 10000, 100000]  # tamaños de listas a probar
    results = {}

    for tamaño in tamaños:
        lista = generar_lista_aleatoria(tamaño, 100000)

        # Benchmarking insertionsort
        start = time.perf_counter()
        insertionsort.insertionsort(lista.copy())  # Llamar a la función de ordenamiento dentro del módulo
        end = time.perf_counter()
        results[f'insertionsort_{tamaño}'] = end - start

        # Benchmarking mergesort
        start = time.perf_counter()
        mergesort.mergesort(lista.copy())  # Llamar a la función de ordenamiento dentro del módulo
        end = time.perf_counter()
        results[f'mergesort_{tamaño}'] = end - start

        # Benchmarking quicksort
        start = time.perf_counter()
        quicksort.quicksort(lista.copy())  # Llamar a la función de ordenamiento dentro del módulo
        end = time.perf_counter()
        results[f'quicksort_{tamaño}'] = end - start

        # Benchmarking sorted (biblioteca estándar)
        start = time.perf_counter()
        sorted(lista.copy())
        end = time.perf_counter()
        results[f'sorted_{tamaño}'] = end - start

    return results

# Ejecutar el benchmark
sort_results = benchmark_sorting_algorithms()
print("\nResultados de benchmark de ordenamiento:")
for key, value in sort_results.items():
    print(f"{key}: {value:.6f} segundos")
