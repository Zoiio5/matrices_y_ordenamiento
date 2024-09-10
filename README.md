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

# Generador de Datasets y Benchmarks

Este proyecto incluye herramientas para la generación de datasets y la evaluación del rendimiento de algoritmos de ordenamiento y multiplicación de matrices. Los datasets generados se almacenan en formato binario (`.bin`) y se utilizan para realizar pruebas de rendimiento sobre diferentes algoritmos implementados.

## Estructura del Proyecto

- **Carpeta `matrix/`**: Scripts relacionados con la multiplicación de matrices.
  - `multiplicacionmatrices.py`: Multiplicación de matrices tradicional.
  - `optimizacionmatrices.py`: Multiplicación de matrices optimizada para mejorar la localidad de datos.
  - `Strassen.py`: Implementación del algoritmo de Strassen para multiplicación de matrices.

- **Carpeta `sorts/`**: Scripts de ordenamiento.
  - `insertionsort.py`: Implementación de Insertion Sort.
  - `mergesort.py`: Implementación de Merge Sort.
  - `quicksort.py`: Implementación de Quick Sort.
  - `sort.py`: Contiene la ejecución de diferentes algoritmos de ordenamiento para comparar su rendimiento.
  - `benchmarking_matrix.py`: Pruebas de rendimiento para algoritmos de multiplicación de matrices.
  - `benchmarking_sort.py`: Pruebas de rendimiento para algoritmos de ordenamiento.
  - `benchmarking_sort_aoi.py`: Pruebas de ordenamiento con áreas de interés específicas.
  - `generador_dataset.py`: Generador de datasets de matrices.
  - `grafico_sort.py`: Genera gráficos para los resultados de los benchmarks de ordenamiento.

## Generador de Datasets

El script `generador_dataset.py` permite crear matrices aleatorias o matrices ordenadas que se utilizarán en los benchmarks de multiplicación de matrices. Los datasets generados son matrices de números enteros y se almacenan en la carpeta `Dataset` en formato binario (`.bin`).

### Uso del Generador de Datasets

1. Ejecuta el script:
    ```bash
    python generador_dataset.py
    ```

2. Sigue las instrucciones en pantalla:
    - **Tamaño de las matrices**: Selecciona si deseas generar matrices de tamaño `n x n` o `2^n x 2^n`.
    - **Matrices diferentes o iguales**: Elige si deseas que una matriz se multiplique por sí misma o generar dos matrices diferentes.
    - **Máximo valor de n**: Define el tamaño máximo para las matrices.

3. Los archivos generados se almacenarán automáticamente en la carpeta `Dataset`.

## Benchmarks

### Benchmarks de Ordenamiento

El script `benchmarking_sort.py` ejecuta pruebas de rendimiento sobre varios algoritmos de ordenamiento, como Insertion Sort, Merge Sort, Quick Sort, y el método estándar `sorted()` de Python. Los benchmarks se ejecutan en listas generadas aleatoriamente, ordenadas, y en orden inverso.

**Ejemplo de ejecución:**

```bash
python benchmarking_sort.py
```
### Benchmarks de Multiplicación de Matrices
El script `benchmarking_matrix.py` realiza pruebas de rendimiento en varios algoritmos de multiplicación de matrices, incluyendo:

- Multiplicación cúbica tradicional.
- Multiplicación optimizada para mejorar la localidad de datos.
- Algoritmo de Strassen (que añade padding a las matrices cuando no son de tamaño potencia de 2).

**Ejemplo de ejecución:**

```bash
python benchmarking_matrix.py
```


