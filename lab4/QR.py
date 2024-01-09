import numpy as np

def qr_decomposition_method(matrix, max_iter=100, tol=1e-6):
    for _ in range(max_iter):
        q, r = np.linalg.qr(matrix)
        matrix = r @ q

    eigen_values = np.diag(matrix)
    return eigen_values