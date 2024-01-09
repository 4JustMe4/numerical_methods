import numpy as np

def power_iteration_method(matrix, max_iter=100, tol=1e-6):
    n = matrix.shape[0]
    x = np.random.rand(n)
    x /= np.linalg.norm(x)

    for _ in range(max_iter):
        y = matrix @ x
        eigen_value = np.dot(x, y)
        x = y / np.linalg.norm(y)

    return eigen_value