import os
import numpy as np
import time
import matrix.Strassen as S
import matrix.optimizacionmatrices as OM
import matrix.muliplicacionmatrices as MU


# Función para cargar una matriz desde un archivo binario
def cargar_matriz(nombre_archivo, tamaño):
    matriz = np.fromfile(nombre_archivo, dtype=np.int32)
    return matriz.reshape(tamaño, tamaño)


# Función para hacer padding a una matriz hasta el tamaño 2^n
def hacer_padding(matriz):
    filas, columnas = matriz.shape
    max_dim = max(filas, columnas)

    # Asegurarse de que la dimensión sea una potencia de 2
    nuevo_tamaño = 1
    while nuevo_tamaño < max_dim:
        nuevo_tamaño *= 2

    # Crear una matriz con el nuevo tamaño y rellenarla con la original
    matriz_padded = np.zeros((nuevo_tamaño, nuevo_tamaño), dtype=matriz.dtype)
    matriz_padded[:filas, :columnas] = matriz
    return matriz_padded, filas, columnas


# Función para medir tiempos y correr las pruebas
def ejecutar_prueba(archivo_A, archivo_B, tamaño, misma_matriz):
    # Leer las matrices desde archivo
    A = cargar_matriz(archivo_A, tamaño)
    B = A if misma_matriz else cargar_matriz(archivo_B, tamaño)

    # Hacer padding si es necesario para Strassen
    A_padded, original_filas_A, original_columnas_A = hacer_padding(A)
    B_padded, original_filas_B, original_columnas_B = hacer_padding(B)

    # Indicar si es la misma matriz o una diferente
    if misma_matriz:
        print(f"\nMultiplicando la matriz {archivo_A} por sí misma:")
    else:
        print(f"\nMultiplicando la matriz {archivo_A} por la matriz {archivo_B}:")

    # 1. Algoritmo iterativo cúbico tradicional
    start = time.perf_counter()
    C_tradicional = MU.multiplica_matrices(A, B)
    end = time.perf_counter()
    print(f"Tiempo de ejecución (iterativo cúbico tradicional): {end - start:.10f} segundos")

    # 2. Algoritmo iterativo cúbico optimizado
    start = time.perf_counter()
    C_optimizado = OM.matrix_multiply_optimized(A, B)
    end = time.perf_counter()
    print(f"Tiempo de ejecución (iterativo cúbico optimizado): {end - start:.10f} segundos")

    # 3. Algoritmo de Strassen (sobre matrices con padding)
    start = time.perf_counter()
    C_strassen_padded = S.strassen(A_padded, B_padded)
    end = time.perf_counter()

    # Recortar la matriz resultado al tamaño original
    C_strassen = C_strassen_padded[:original_filas_A, :original_columnas_B]
    print(f"Tiempo de ejecución (Strassen): {end - start:.10f} segundos")


# Ejecutar las pruebas de multiplicación
if __name__ == "__main__":
    archivos = sorted(os.listdir('Dataset'))

    for archivo in archivos:
        if 'A' in archivo:
            # Extraer el tamaño y tipo de matriz (misma o diferente) del nombre del archivo
            partes = archivo.split('_')
            tamaño_str = partes[2].split('x')[0]
            tamaño = int(tamaño_str)  # Convertir a entero
            tipo = partes[-1].replace('.bin', '')

            # Definir los archivos de las matrices
            archivo_A = os.path.join('Dataset', archivo)
            archivo_B = archivo_A if tipo == 'misma' else archivo_A.replace('A', 'B')

            misma_matriz = tipo == 'misma'

            print(f"\nPruebas para matrices de tamaño {tamaño}x{tamaño} ({tipo}):")
            ejecutar_prueba(archivo_A, archivo_B, tamaño, misma_matriz)
