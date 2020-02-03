"""
Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
ax + by = e
cx + dy = f

Формат ввода
Вводятся 6 чисел a, b, c, d, e, f — коэффициенты уравнений.

Формат вывода. Вывод программы зависит от вида решения этой системы:

Если система не имеет решений, то программа должна вывести только число 0.

Если система имеет бесконечно много решений, каждое из которых имеет
вид y=px+q,то программа должна вывести число 1, а затем значения p и q.

Если система имеет единственное решение (x₀,y₀), то программа должна
вывести число 2, а затем значения x₀ и y₀.

Если система имеет бесконечно
много решений вида x=x₀, y — любое, то программа должна вывести число 3,
а затем значение x₀.

Если система имеет бесконечно много решений вида
y=y₀, x — любое, то программа должна вывести число 4, а затем значение
y₀.

Если любая пара чисел (x,y) является решением, то программа должна
вывести число 5.

"""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x_denominator = (b * c - a * d)
y_denominator = (a * d - c * b)


if x_denominator and y_denominator:
    x = (b * f - d * e) / x_denominator
    y = (a * f - c * e) / y_denominator
    print(2, x, y)
