import unittest

def newton_interpolation(x, y, x_i):
    """
    Approximate grid functions through Newton polynomials.

    Args:
    x (list): List of x-coordinates of the grid points
    y (list): List of y-coordinates of the grid points
    x_i (float): The point at which to approximate the grid function

    Returns:
    float: The approximate value of the grid function at x_i
    """
    if len(y) != len(x):
        raise ValueError("The lengths of x and y must be the same")

    n = len(x)

    # Calculate the divided differences
    f = [[y[i]] + [0] * (n - 1) for i in range(n)]
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])

    # Calculate the Newton polynomial
    result = f[0][0]
    for j in range(1, n):
        term = f[0][j]
        for i in range(j):
            term *= (x_i - x[i])
        result += term

    return result

class TestNewtonInterpolation(unittest.TestCase):
    def test_newton_interpolation(self):
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        x_i = 2.5
        self.assertAlmostEqual(newton_interpolation(x, y, x_i), 6.25, places=2)

    def test_invalid_input(self):
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9]  # y has one element less than x
        x_i = 2.5
        with self.assertRaises(ValueError):
            newton_interpolation(x, y, x_i)

if __name__ == '__main__':
    unittest.main()