import random
import time
import matplotlib.pyplot as plt

import sorts.mergesort as mergesort
import sorts.quicksort as quicksort
import sorts.insertionsort as insertionsort

# Generación de una lista aleatoria
def generar_lista_aleatoria(tamaño, rango):
    return [random.randint(0, rango) for _ in range(tamaño)]

# Benchmark de algoritmos de ordenamiento
def benchmark_sorting_algorithms():
    tamaños = [100, 1000, 10000, 100000]  # tamaños de listas a probar
    results = {
        'insertionsort': [],
        'mergesort': [],
        'quicksort': [],
        'sorted': []
    }

    for tamaño in tamaños:
        lista = generar_lista_aleatoria(tamaño, 100000)

        # Benchmarking insertionsort
        start = time.perf_counter()
        insertionsort.insertionsort(lista.copy())  # Llamar a la función de ordenamiento dentro del módulo
        end = time.perf_counter()
        results['insertionsort'].append(end - start)

        # Benchmarking mergesort
        start = time.perf_counter()
        mergesort.mergesort(lista.copy())  # Llamar a la función de ordenamiento dentro del módulo
        end = time.perf_counter()
        results['mergesort'].append(end - start)

        # Benchmarking quicksort
        start = time.perf_counter()
        quicksort.quicksort(lista.copy())  # Llamar a la función de ordenamiento dentro del módulo
        end = time.perf_counter()
        results['quicksort'].append(end - start)

        # Benchmarking sorted (biblioteca estándar)
        start = time.perf_counter()
        sorted(lista.copy())
        end = time.perf_counter()
        results['sorted'].append(end - start)

    return results, tamaños

# Función para generar el gráfico
def generar_grafico(resultados, tamaños):
    plt.figure(figsize=(10, 6))

    for algoritmo, tiempos in resultados.items():
        plt.plot(tamaños, tiempos, label=algoritmo)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')  # Usamos escala logarítmica para los tamaños grandes
    plt.yscale('log')  # Usamos escala logarítmica para los tiempos
    plt.show()

# Ejecutar el benchmark
sort_results, tamaños = benchmark_sorting_algorithms()

# Generar el gráfico
generar_grafico(sort_results, tamaños)
