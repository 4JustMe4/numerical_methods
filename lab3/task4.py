import numpy as np

tolerance = 1e-9
max_iter = 100

def seidel_iteration(matrix, constants):
    size = len(matrix)
    x = np.zeros(size, dtype=float)

    for _ in range(max_iter):
        next = np.copy(x)
        for i in range(size):
            sum1 = np.dot(matrix[i][:i], next[:i])
            sum2 = np.dot(matrix[i][i + 1:], x[i + 1:])
            try:
                next[i] = (constants[i] - sum1 - sum2) / matrix[i][i]
            except ZeroDivisionError:
                raise ValueError("Division by zero happended. The matrix has zero diagonal elements.")

        if np.allclose(next, x, atol=tolerance):
            return next

        x = np.copy(next)

    raise ValueError("Seidel method did not converge within the specified tolerance and maximum iterations.")

size = int(input("Количество уравнений: "))
matrix = [[float(input(f"Коэффициент a_{i + 1}_{j + 1}: ")) for j in range(size)] for i in range(size)]
constants = [float(input(f"Введите значение для уравнения {i + 1}: ")) for i in range(size)]

try:
    result = seidel_iteration(matrix, constants)
    print("Решение системы:")
    for i, x in enumerate(result, start=1):
        print(f'x_{i} = {x}')
except ValueError as e:
    print(f"Ошибка: {e}")