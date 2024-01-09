import numpy as np

def piecewise_linear_interpolation():
    x = np.array([3, 4, 5, 6], dtype=float)
    f = np.array([1, 0, 4, 2], dtype=float)

    X = 4.5
    i = 1

    P1 = (X - x[i + 1]) / (x[i] - x[i + 1])
    P2 = (X - x[ i ]) / (x[i + 1] - x[i])
    ans = 0

    if (P1 + P2 == 1):
        ans = P1 * f[i] + P2 * f[i + 1]
    return ans