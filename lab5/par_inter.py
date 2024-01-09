import numpy as np

def piecewise_parabolic_interpolation():
    def p1(x, X, i):
        return ((X - x[i + 1]) * (X - x[i + 2])) / ((x[i] - x[i + 1]) * (x[i] - x[i + 2]))

    def p2(x, X, i):
        return ((X - x[i]) * (X - x[i + 2])) / ((x[i + 1] - x[i]) * (x[i + 1] - x[i + 2] ))

    def p3(x, X, i):
        return ((X - x[i]) * (X - x[i + 1])) / ((x[i + 2] - x[i]) * (x[i + 2] - x[i + 1]))

    x = np.array([3, 4, 5, 6], dtype=float)
    f = np.array([1, 0, 4, 2], dtype=float)

    X = 4.5

    i = 1

    l1 = p1(x, X, i - 1) * f[i - 1] + p2(x, X, i - 1) * f[i] + p3(x, X, i - 1) * f[i+1]
    l2 = p1(x, X, i) * f[i] + p2(x, X, i) * f[i+1] + p3(x, X, i) * f[i + 2]

    ans = (l1 + l2) / 2
    return ans