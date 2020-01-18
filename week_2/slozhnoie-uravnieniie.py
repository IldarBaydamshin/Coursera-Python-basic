"""
Решить в целых числах уравнение: (ax + b) / (cx + d) = 0
Формат ввода
Вводятся 4 числа: a,b,c,d;  c и d не равны нулю одновременно.
Формат вывода
Необходимо вывести все решения, если их число конечно,
“NO” (без кавычек),если решений нет, и
“INF” (без кавычек), если решений бесконечно много.
"""

a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = 2, -4, 7, 1
# a, b, c, d = 1, 1, 2, 2

# x = 'foo'
#
# if a == 0 and b == 0:
#     x = 'INF'
# elif a == 0 and b != 0:
#     x = 'NO'
# else:
#     x = int(-b / a)
#
# if c == 0:
#     pass
# elif c * x + d:
#     pass
# else:
#     x = 'NO'

# print(x)

if a == 0 and b == 0:
    print("INF")
elif a == 0 or a * d == b * c:
    print("NO")
elif b // a * a == b:
    print(-b // a)
else:
    print("NO")
