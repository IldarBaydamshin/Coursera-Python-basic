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

delta = a * d - c * b
delta_x = e * d - f * b
delta_y = a * f - c * e

if not a and not b and not c and not d and not e and not f:
    answer = '5'
elif (not a and not b and e) or (not c and not d and f):
    answer = '0'
elif a and c and not b and not d and e / a != f / c:
    answer = '0'
elif not a and not c and b and d and e / b != f / d:
    answer = '0'

elif not b and not d and (a or c):
    if a:
        x = int((e / a) * 1000000) / 1000000
    if c:
        x = int((f / c) * 1000000) / 1000000
    answer = '3 ' + str(x)

elif not a and not c and (b or d):
    if b:
        y = int((e / b) * 1000000) / 1000000
    elif d:
        y = int((f / d) * 1000000) / 1000000
    answer = '4 ' + str(y)

elif delta:
    x = int((delta_x / delta) * 1000000) / 1000000
    y = int((delta_y / delta) * 1000000) / 1000000
    answer = '2 ' + str(x) + ' ' + str(y)

elif a * d == c * b and e * d == f * b and (b or d):
    if b:
        p = int((-a / b) * 1000000) / 1000000
        q = int((e / b) * 1000000) / 1000000
    elif d:
        p = int((-c / d) * 1000000) / 1000000
        q = int((f / d) * 1000000) / 1000000
    answer = '1 ' + str(p) + ' ' + str(q)

else:
    answer = '0'

print(answer)
