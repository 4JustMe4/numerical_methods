# Метод простой итерации

import math


def g(x, a):
    return 0.5 * (x + a / x)


a = int(input())
x = 1
y = g(x, a)
eps = 1e-9


def sqrt(x, a, y):
    while abs(y - x):
        x = y
        y = g(x, a)
    return x


print(sqrt(x, a, y))