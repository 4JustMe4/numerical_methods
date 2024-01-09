def substitution_method(coefs, constants):
    n = len(constants)
    solutions = [0] * n

    for i in range(n):
        solutions[i] = constants[i]

        for j in range(n):
            if i != j:
                solutions[i] -= coefs[i][j] * solutions[j]

        solutions[i] /= coefs[i][i]

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

ans = substitution_method(coefs, constants)

print("Решение системы:")
print(ans)