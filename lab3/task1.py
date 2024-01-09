def gauss_elimination(mat, n, result):
    for i in range(n):
        result[i] /= mat[i][i]
        for j in range(n - 1, i - 1, -1):
            mat[i][j] /= mat[i][i]

        for k in range(i + 1, n):
            factor = mat[k][i]
            for j in range(i, n):
                mat[k][j] -= factor * mat[i][j]
            result[k] -= factor * result[i]

    for i in range(n - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            factor = mat[k][i]
            for j in range(n):
                mat[k][j] -= factor * mat[i][j]
            result[k] -= factor * result[i]

    return result

n = int(input("Размерность матрицы: "))
mat = []
result = []

print("Введите матрицу:")
for i in range(n):
    row = [float(x) for x in input().split()]
    mat.append(row)

print("Введите вектор правой части:")
result = [float(x) for x in input().split()]

answer = gauss_elimination(mat, n, result)
print("Ответ:", answer)