"""
    Даны два натуральных числа n и m.

    Сократите дробь (n / m), то есть выведите два других числа p и q таких,
    что (n / m) = (p / q) и дробь (p / q) — несократимая.

    Решение оформите в виде функции ReduceFraction(n, m), получающая значения n
    и m и возвращающей кортеж из двух чисел: return p, q.

    Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).

    Формат ввода
    Вводятся два натуральных числа.

    Формат вывода
    Выведите ответ на задачу.

"""


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    return a


def reduce_fraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


p = int(input())
q = int(input())
print(*reduce_fraction(p, q))
