# Algoritmos de Ordenamiento y Multiplicación de Matrices

Este proyecto implementa y compara diferentes algoritmos de **ordenamiento** y **multiplicación de matrices** en Python. A través de scripts y datasets generados, se ejecutan benchmarks para evaluar el rendimiento de cada algoritmo.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Generador de Datasets](#generador-de-datasets)
- [Descripción de los Scripts](#descripción-de-los-scripts)
- [Ejecución de los Benchmarks](#ejecución-de-los-benchmarks)

## Instalación

### Requerimientos
El proyecto depende de varias bibliotecas de Python. Para asegurarte de que todo funcione correctamente, instala las dependencias utilizando el archivo `requirements.txt`.


1. Clona este repositorio:
   ```bash
   git clone https://github.com/Zoiio5/matrices_y_ordenamiento.git

2. Crear un entorno virtual(opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Instalar las dependencias desde requeriments.txt:
   ```bash
   pip freeze > requirements.txt

## Generador de Datasets

El proyecto incluye un generador de datasets que permite crear matrices aleatorias o ordenadas para realizar las pruebas de rendimiento de los algoritmos de multiplicación de matrices. Los datasets generados son matrices almacenadas en formato binario (.bin).

## Cómo funciona el generador de datasets

El script `generar_datasets.py` se encarga de generar matrices de tamaño n x n o de tamaño 2^n x 2^n. Puedes elegir generar:

- Dos matrices diferentes para multiplicarlas entre sí.
- Una única matriz que se multiplicará por sí misma.

### Ejemplo de uso:

1. Ejecuta el script:
    ```bash
    python generar_datasets.py
    ```
2. Sigue las instrucciones en pantalla:
    - **Tamaño de las matrices**: Elige si deseas generar matrices de tamaño n x n o 2^n x 2^n.
    - **Matrices diferentes o iguales**: Selecciona si deseas que la matriz A se multiplique por sí misma o si prefieres generar una matriz B para la multiplicación.
    - **Máximo valor de n**: Define hasta qué potencia o tamaño deseas generar las matrices.

Los archivos generados se almacenarán en la carpeta `Dataset`.

## Descripción de los Scripts

### `generar_datasets.py`

Este script genera matrices de números enteros dentro del rango [0, 10] para ser utilizados en los benchmarks de multiplicación de matrices. Se pueden generar matrices de tamaño n x n o 2^n x 2^n, y se almacenan en formato binario (.bin) en la carpeta `Dataset`.

**Funciones clave:**
- `vaciar_carpeta(carpeta)`: Vacía la carpeta de datasets antes de generar nuevos archivos.
- `generar_matriz(tamaño, nombre_archivo)`: Genera una matriz aleatoria y la guarda en un archivo binario.
- `main`: Interactúa con el usuario para configurar los parámetros de generación de matrices.

### `benchmark_sort.py`

Este script ejecuta benchmarks de varios algoritmos de ordenamiento, incluyendo Insertion Sort, Mergesort, Quicksort, y la función estándar `sorted()` de Python. Prueba los algoritmos en tres tipos de listas: aleatorias, ordenadas y en orden inverso.

**Funciones clave:**
- `generar_lista_aleatoria(tamaño, rango)`: Genera una lista de números enteros aleatorios.
- `benchmark_sorting_algorithms()`: Ejecuta el benchmark de los algoritmos sobre diferentes tamaños de listas.

Los resultados se imprimen en consola y pueden ser exportados a archivos para análisis posterior.

### `benchmark_multiplicacion_matrices.py`

Este script realiza pruebas de rendimiento de algoritmos de multiplicación de matrices. Los algoritmos probados son:

- Multiplicación iterativa cúbica tradicional.
- Multiplicación iterativa cúbica optimizada (mejora la localidad de los datos).
- Algoritmo de Strassen (con padding para tamaños de matrices no potencia de 2).

**Funciones clave:**
- `cargar_matriz(nombre_archivo, tamaño)`: Carga matrices almacenadas en formato binario.
- `hacer_padding(matriz)`: Añade padding a matrices para que su tamaño sea una potencia de 2.
- `ejecutar_prueba(archivo_A, archivo_B, tamaño, misma_matriz)`: Ejecuta las pruebas y mide los tiempos de los tres algoritmos.

### `graficar_resultados.py`

Este script se encarga de graficar los resultados obtenidos de los benchmarks. Utiliza matplotlib y seaborn para visualizar los tiempos de ejecución de los algoritmos en diferentes tamaños de listas y matrices.

**Funciones clave:**
- `graficar_ordenamiento()`: Crea gráficos comparativos de los tiempos de ejecución de los algoritmos de ordenamiento.
- `graficar_matrices()`: Genera gráficos que comparan los tiempos de ejecución de los algoritmos de multiplicación de matrices.

## Ejecución de los Benchmarks

Para ejecutar los benchmarks de algoritmos de ordenamiento o multiplicación de matrices, utiliza los siguientes comandos:

### Benchmarks de Ordenamiento:
```bash
python benchmark_sort.py

