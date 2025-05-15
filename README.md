---Metodo de la Secante en Python---

Este proyecto implementa el metodo de la secante que es un algoritmo numérico utilizado para encontrar raíces de funciones no lineales. El usuario introduce los datos necesarios desde la consola y el programa muestra paso a paso las iteraciones, junto con una visualización gráfica del resultado final.

---Formula usada---
La fórmula usada es:

x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))

Este método requiere dos valores iniciales (x0 y x1) y no usa derivadas, lo que lo hace útil cuando la derivada es difícil de obtener.

---Instrucciones de uso---
1. Tener Python instalado.
2. Instala la librería para graficar:
pip install matplotlib
3. Ejecuta el archivo desde la terminal:
python metodo_secante.py
4. Introduce los siguientes datos cuando se te pidan:
- Valor inicial x0
- Segundo valor x1
- Tolerancia
- Número máximo de iteraciones
5. El programa:
- Mostrará los pasos de cada iteración.
- Indicará si encontró una raíz aproximada.
- Mostrará una gráfica con la función y la raíz encontrada.
  
---Personalizacion---
Puedes editar la función en el archivo "metodo_secante.py" modificando esta parte:
def f(x):
 return math.exp(-x) - x
Simplemente cambia la expresión por la función que desees resolver.
