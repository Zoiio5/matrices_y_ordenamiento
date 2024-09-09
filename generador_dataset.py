import numpy as np
import os

# Crear la carpeta principal "Dataset" si no existe
os.makedirs('Dataset', exist_ok=True)

# Vaciar la carpeta eliminando todos los archivos
def vaciar_carpeta(carpeta):
    for archivo in os.listdir(carpeta):
        archivo_path = os.path.join(carpeta, archivo)
        try:
            if os.path.isfile(archivo_path):
                os.unlink(archivo_path)  # Eliminar el archivo
        except Exception as e:
            print(f'No se pudo eliminar {archivo_path}. Error: {e}')

# Función para generar una matriz aleatoria y guardarla en un archivo binario
def generar_matriz(tamaño, nombre_archivo):
    matriz = np.random.randint(0, 10, (tamaño, tamaño), dtype=np.int32)
    matriz.tofile(nombre_archivo)  # Guardar la matriz en formato binario
    print(f"Matriz de {tamaño}x{tamaño} guardada en {nombre_archivo}")

# Generar matrices de tamaño n o 2^n
if __name__ == "__main__":
    # Vaciar la carpeta Dataset antes de generar nuevas matrices
    vaciar_carpeta('Dataset')

    eleccion = input("Deseas generar matrices de tamaño n o 2^n? (1/2): ").strip()
    generar_diferentes = input(
        "Deseas generar dos matrices diferentes o la misma para multiplicarse por sí misma? (d/m): ").strip()
    max_n = int(input("Hasta qué potencia de n deseas generar matrices?: ").strip())

    for n in range(1, max_n + 1):
        if eleccion == '2':
            tamaño = 2 ** n  # Matriz de tamaño 2^n
        elif eleccion == '1':
            tamaño = n  # Matriz de tamaño n
        else:
            eleccion = input("Opción inválida, elige de nuevo (1/2): ").strip()
            continue

        tipo = "misma" if generar_diferentes == 'm' else "diferente"

        # Generar las matrices y guardarlas en la carpeta "Dataset" con nombres dinámicos
        archivo_A = os.path.join('Dataset', f'matriz_A_{tamaño}x{tamaño}_{tipo}.bin')
        generar_matriz(tamaño, archivo_A)

        if generar_diferentes == 'd':
            archivo_B = os.path.join('Dataset', f'matriz_B_{tamaño}x{tamaño}_{tipo}.bin')
            generar_matriz(tamaño, archivo_B)
        else:
            archivo_B = archivo_A  # Usar la misma matriz para multiplicarse por sí misma
