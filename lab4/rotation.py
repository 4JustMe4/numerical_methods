import numpy as np

def rotation_method(matrix, max_iter=100, tol=1e-6):
    n = matrix.shape[0]
    V = np.eye(n)

    for _ in range(max_iter):
        p, q = 0, 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(matrix[i, j]) > abs(matrix[p, q]):
                    p, q = i, j

        if matrix[p, q] < tol:
            break

        theta = 0.5 * np.arctan2(2 * matrix[p, q], matrix[q, q] - matrix[p, p])
        cos_value = np.cos(theta)
        sin_value = np.sin(theta)

        R = np.eye(n)
        R[p, p] = cos_value
        R[p, q] = -sin_value
        R[q, p] = sin_value
        R[q, q] = cos_value

        matrix = R.T @ matrix @ R
        V = V @ R

    eigen_values = np.diag(matrix)
    return eigen_values