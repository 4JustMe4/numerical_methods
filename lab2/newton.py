import numpy as np

def find_derivative_coefficients(coefs):
    # Эта функция находит коэффициенты производной функции, представленной в виде многочлена
    derivative_coefficients = [coeff * (len(coefs) - i - 1) for i, coeff in enumerate(coefs[:-1])]
    return derivative_coefficients

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        value = f(x)
        if abs(value) < tol:
            return x
        df_value = df(x)
        if df_value == 0:
            raise ValueError("Derivative is zero. Could not continue.")
        x = x - value / df_value
    # Если метод не сошелся
    raise ValueError("Newton's method did not converge.")


# Задаем многочлен: x^3 - 3x^2 + 2x - 4.
coefs = [1, -3, 2, -4]

# Находим производную
derivative_coefficients = find_derivative_coefficients(coefs)

# Заводим функцию для многочлена через NumPy
f = lambda x: np.polyval(coefs, x)

# Заводим функцию для производной через NumPy
df = lambda x: np.polyval(derivative_coefficients, x)
x0 = 3
root = newton_method(f, df, x0)
print("Root:", root)