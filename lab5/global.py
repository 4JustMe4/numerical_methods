import numpy as np

def global_approximation():
    def gaussMethod(M):
        for nLine, line in enumerate(M):
            pivot = line[nLine]
            line /= pivot
            for lower_line in M[nLine + 1:]:
                coeff = lower_line[nLine]
                lower_line -= coeff * line
        for nLine in range(len(M) - 1, 0, -1):
            line = M[nLine]
            for upper_line in M[:nLine]:
                coeff = upper_line[nLine]
                upper_line[-1] -= coeff * line[-1]
                upper_line[nLine] = 0
        return M

    x_values = np.array([3, 4, 5, 6], dtype=float)
    y_values = np.array([1, 0, 4, 2], dtype=float)

    w = np.array([[x_values[i] ** j for j in range(len(x_values))] for i in range(len(x_values))])
    W = np.c_[powers_matrix, y_values.T]

    coeff = gauss_elimination(augmented_matrix)[:, -1]

    x_input = 4.5
    result = sum(coeff[i] * x_input ** i for i in range(len(coeff)))

    return result