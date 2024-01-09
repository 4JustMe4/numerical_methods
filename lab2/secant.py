def secant_method(f, x0, x1, eps=1e-6, max_iter=100):
    for i in range(max_iter):
        x0_value = f(x0)
        x1_value = f(x1)

        if abs(x1_value) < eps:
            return x1  # Заврешаемся - уже значение на второй точке близко к нулю.

        # Считаем следующее.
        x2 = x1 - x1_value * (x1 - x0) / (x1_value - x0_value)

        if abs(x2 - x1) < eps:
            return x2  # Заврешаемся - значения не сильно отличаются.

        x0, x1 = x1, x2

    # Если метод не сошелся
    raise ValueError("Secant method did not converge.")


# Пример использования:
# Определяем функцию f(x)
f = lambda x: x**3 - 3*x**2 + 2*x - 4

x0 = 3  # Начальное приближение
x1 = 4  # Второе начальное приближение
eps = 1e-6  # Критерий окончания

root = secant_method(f, x0, x1, eps)
print("Root:", root)