"""
    Даны вещественные числа a, b, c, d, e, f.
    Известно, что система линейных уравнений:
    ax + by = e
    cx + dy = f
    имеет ровно одно решение.
    Выведите два числа x и y, являющиеся решением этой системы.

    Формат ввода
    Вводятся шесть чисел a, b, c, d, e, f - коэффициенты уравнений системы.
"""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = (b * f - d * e) / (b * c - a * d)
y = (a * f - c * e) / (a * d - c * b)
print(x, y)
