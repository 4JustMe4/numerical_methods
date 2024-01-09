# Метод половинного деления

import random
import sympy


def Hmetod(func2, eps, L, R, max_it=100):
    Border(L, R, func2)
    for _ in range(max_it):
        M = (L + R) / 2
        if abs(func2(M)) < eps:
            return M
        elif func2(L) * func2(M) < 0:
            R = M
        else:
            L = M

def func1(x):
    return (x**3 + 2)
def func3(x):
    return (x**3 + 2 * (x**2) - 3)
def func2(x):
    return (x**2 - 3 * x - 9)

L = -100
R = 100
step = 0.5
eps = 1e-3

def Border(L, R, func):
    while func(L) * func(R) > 0 and L > R:
        L += step

root = Hmetod(func2, eps, L, R)
print(f"Корень: {root}")