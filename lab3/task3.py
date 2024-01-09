def gauss_elimination(matrix, constants):
    n = len(matrix)

    for i in range(n):
        idx = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[idx][i]):
                idx = k

        matrix[i], matrix[idx] = matrix[idx], matrix[i]
        constants[i], constants[idx] = constants[idx], constants[i]

        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            constants[k] -= factor * constants[i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]

    solutions = [0] * n
    for i in range(n - 1, -1, -1):
        solutions[i] = constants[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            constants[k] -= matrix[k][i] * solutions[i]

    return solutions

def print_solutions(solutions):
    n = len(solutions)
    for i in range(n):
        print(f'x_{i + 1} = {solutions[i]}')

equations_count = int(input("Количество уравнений: "))

# Ввод коэффициентов
coefs = []
for i in range(equations_count):
    row = []
    for j in range(equations_count):
        coefficient = float(input(f"Коэффициент a_{i + 1}_{j + 1}: "))
        row.append(coefficient)
    coefs.append(row)

constants = []
for i in range(equations_count):
    value = float(input(f"Значение для уравнения {i + 1}: "))
    constants.append(value)

ans = gauss_elimination(coefs, constants)

print("Решение системы:")
print(ans)