# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hfgj23-yqDMJWQuNvh59mUAAkGb6uQiS
"""

import numpy as np
import matplotlib.pyplot as plt

# Primer código: Solución analítica
def solucion_analitica(N:int, M:int, dx:float, v0:float, terminos:int=50):
    """
    Calcula la solución analítica de la ecuación de Laplace en 2D.

    Parámetros:
        N : int
            Número de puntos en el eje x.
        M : int
            Número de puntos en el eje y.
        dx : float
            Tamaño de paso en la malla.
        v0 : float
            Valor utilizado en el cálculo.
        terminos : int, opcional
            Número de términos a sumar en la solución analítica.

    Devuelve:
        X : numpy.array
            Coordenadas en el eje x.
        Y : numpy.array
            Coordenadas en el eje y.
        V : numpy.array
            Solución analítica de la ecuación de Laplace.
    """
    a = N * dx
    b = M * dx
    x = np.linspace(0, a, N)
    y = np.linspace(0, b, M)
    X, Y = np.meshgrid(x, y)
    V = 0

    for n in range(1, terminos + 1):
        k = n * np.pi / a
        D = -2 * v0 * (1 - (-1) ** n) / (n * np.pi)
        #Valor de D obtenido analíticamente
        C = -D * (1 / np.sinh(k * b) + np.cosh(k * b) / np.sinh(k * b))
       #Valor de C obtenido analitcamente
        V += np.sin(k * X) * (C * np.sinh(k * Y) + D * np.cosh(k * Y))

    return X, Y, V

def plot_analytic_solution():
    """
    Genera y muestra un gráfico de la solución analítica de la ecuación de Laplace.
    """
    N = 100
    M = 100
    dx = 0.5
    v0 = 10

    X, Y, V = solucion_analitica(N, M, dx, v0)

    plt.figure(figsize=(10, 8))
    plt.contourf(X, Y, V, levels=100, cmap='viridis')
    plt.colorbar(label='V(x, y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución Analítica de la ecuación de Laplace')
    plt.grid(True)
    plt.show()

# Segundo código: Solución numérica
def laplace_solver(dx,V, V_boundary, tolerance=1e-6, max_iterations=10000):
    """
    Resuelve la ecuación de Laplace utilizando el método de relajación.

    Parámetros:
        V : numpy.array
            Valores de potencial inicial.
        V_boundary : numpy.array
            Valores de potencial en la frontera.
        tolerance : float, opcional
            Tolerancia para la convergencia.
        max_iterations : int, opcional
            Número máximo de iteraciones.

    Devuelve:
        V : numpy.array
            Valores de potencial después de resolver la ecuación de Laplace.
    """
    nx, ny = V.shape
    V_new = np.copy(V)

    for iteration in range(max_iterations):
        max_difference = 0.0

        for i in range(nx):
            for j in range(ny):
                if i == 0 or i == nx - 1 or j == 0 or j == ny - 1:
                    V_new[i, j] = V_boundary[i, j]
                else:
                    V_new[i, j] = 0.25 * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1])

                difference = abs(V_new[i, j] - V[i, j])
                if difference > max_difference:
                    max_difference = difference

        V = np.copy(V_new)

        if max_difference < tolerance:
            print(f"Convergencia alcanzada después de {iteration + 1} iteraciones.")
            break
    else:
        print("Advertencia: Se alcanzó el número máximo de iteraciones sin convergencia.")

    return V

def plot_potential(V):
    """
    Genera y muestra un gráfico de los valores de potencial.

    Parámetros:
        V : numpy.array
            Valores de potencial.
    """
    plt.imshow(V, cmap='viridis', origin='lower', extent=(0, V.shape[0], 0, V.shape[1]))
    plt.colorbar(label='Potencial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Distribución de Potencial')
    plt.show()

def main():
    # Solución analítica
    plot_analytic_solution()

    # Solución numérica
    nx = 50
    ny = 50
    V = np.zeros((nx, ny))
    V_boundary = np.zeros((nx, ny))
    V_boundary[0, :] = -10
    V_boundary[-1, :] = 10
    V_boundary[:, 0] = 0
    V_boundary[:, -1] = 0
    dx=0.001
    V[1:-1, 1:-1] = np.random.rand(nx - 2, ny - 2)
    V = laplace_solver(dx,V, V_boundary)
    plot_potential(V)

if __name__ == "__main__":
    main()