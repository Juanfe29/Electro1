# Electro1
# Solución de la Ecuación de Laplace en 2D

Este repositorio contiene dos implementaciones para resolver la ecuación de Laplace en 2D: una solución analítica y una solución numérica utilizando el método de relajación.

## Solución Analítica

La solución analítica se basa en una serie infinita que representa la solución exacta de la ecuación de Laplace. El código proporcionado utiliza esta serie para calcular la solución para un dominio rectangular específico.

### Código y Uso

El código se encuentra en `solucion_analitica.py`. Para utilizarlo, sigue las siguientes instrucciones:

1. Asegúrate de tener `numpy` y `matplotlib` instalados.
2. Importa el módulo y llama a la función `solucion_analitica(N, M, dx, v0, terminos)`, donde:
    - `N`: Número de puntos en el eje x.
    - `M`: Número de puntos en el eje y.
    - `dx`: Tamaño de paso en la malla.
    - `v0`: Valor utilizado en el cálculo.
    - `terminos` (opcional): Número de términos a sumar en la solución analítica.

El resultado es una matriz de coordenadas `X` e `Y`, y la solución `V` de la ecuación de Laplace.

## Solución Numérica

La solución numérica se basa en el método de relajación, que iterativamente actualiza el valor del potencial en cada punto de una malla hasta que la diferencia entre iteraciones consecutivas es menor que una tolerancia especificada.

### Código y Uso

El código de la solución numérica se encuentra en `laplace_solver.py`. Sigue estas instrucciones para utilizarlo:

1. Asegúrate de tener `numpy` y `matplotlib` instalados.
2. Importa el módulo y llama a la función `laplace_solver(dx, V, V_boundary, tolerance, max_iterations)`, donde:
    - `dx`: Tamaño de paso en la malla.
    - `V`: Valores de potencial inicial.
    - `V_boundary`: Valores de potencial en la frontera.
    - `tolerance` (opcional): Tolerancia para la convergencia.
    - `max_iterations` (opcional): Número máximo de iteraciones.

El resultado es la matriz de potencial `V` después de resolver la ecuación de Laplace.

## Ejecución

El script `main.py` utiliza ambas implementaciones y muestra los resultados gráficamente. Puedes ejecutarlo para ver la solución analítica y la solución numérica para un caso de ejemplo.

```bash
python main.py
