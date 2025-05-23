import math
import matplotlib.pyplot as plt

#Funcion
def f(x):
    return math.exp(-x) - x

#Metodo de la Secante
def metodo_secante(f, x0, x1, tol, max_iter):
    print("Iteracion |    x0    |    x1    |    x2    |   f(x2)   | Error")
    for i in range(max_iter):
            fx0 = f(x0)
            fx1 = f(x1)
            if fx1 - fx0 == 0:
                print("Error: Division por cero.")
                return None

            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            error = abs(x2 - x1)

            print(f"{i+1:^9} | {x0:.6f} | {x1:.6f} | {x2:.6f} | {f(x2):.6f} | {error:.6e}")

            if error < tol:
                print(f"\nRaiz aproximada encontrada: {x2:.6f} en {i+1} iteraciones")
                return x2

            x0, x1 = x1, x2

#Crear la grafica
def graficar(f, raiz, intervalo):
    import numpy as np
    x = np.linspace(intervalo[0], intervalo[1], 400)
    y = [f(val) for val in x]

    plt.axhline(0, color='gray', linewidth=0.8)
    plt.plot(x, y, label='f(x)', color='blue')
    plt.plot(raiz, f(raiz), 'ro', label='Raiz aproximada')
    plt.title("Metodo de la secante")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

#Entrada de datos por consola
def leer_datos():
    print("---Metodo de la secante---")
    x0 = float(input("Introduce x0: "))
    x1 = float(input("Introduce x1: "))
    tol = float(input("Introduce la tolerancia (ej: 1e-6): "))
    max_iter = int(input("Introduce el numero maximo de iteraciones: "))
    return x0, x1, tol, max_iter



#Programa principal
x0, x1, tol, max_iter = leer_datos()
raiz = metodo_secante(f, x0, x1, tol, max_iter)
#Mostrar la grafica
if raiz is not None:
     graficar(f, raiz, (min(x0, x1) - 1, max(x0, x1) + 1))
