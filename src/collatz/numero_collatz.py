
import matplotlib.pyplot as plt

def collatz_iterations(n):
    """Calcula el número de iteraciones necesarias para que n llegue a 1."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Si es par, se divide por 2
        else:
            n = 3 * n + 1  # Si es impar, se aplica 3n + 1
        count += 1
    return count

# Generar datos para los números del 1 al 10,000
n_values = list(range(1, 10001))  # Números iniciales
iterations = [collatz_iterations(n) for n in n_values]  # Iteraciones necesarias

# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(iterations, n_values, color="blue", s=1, alpha=0.5)  # Gráfico de dispersión

# Etiquetas y título
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número Inicial (n)")
plt.title("Número de Iteraciones de la Conjetura de Collatz (n entre 1 y 10,000)")
plt.grid(True, linestyle="--", alpha=0.6)

# Mostrar gráfico
plt.show()

