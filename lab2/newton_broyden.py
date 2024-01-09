import numpy as np

def find_derivative(coefs, x):
    # Вычисляет значение производной в x.
    n = len(coefs) - 1
    derivative = 0
    for i in range(n):
        derivative += (n - i) * coefs[i] * x ** (n - i - 1)
    return derivative

def newton_broyden_method(f, x0, c=1, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        value = f(x)
        if abs(value) < tol:
            return x
        der_value = find_derivative(coefs, x)
        if der_value == 0:
            raise ValueError("Derivative is zero. Cannot continue.")
        x = x - c * value / der_value
    # Если метод не сошелся
    raise ValueError("Newton-Broyden method did not converge.")

# Задайте коэффициенты многочлена: x^3 - 3x^2 + 2x - 4.
coefs = [1, -3, 2, -4]
f = lambda x: np.polyval(coefs, x)

x0 = 3
c = 1.5  # Пример выбора параметра c_k
root = newton_broyden_method(f, x0, c)
print("Root:", root)