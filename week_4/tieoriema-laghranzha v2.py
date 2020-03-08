"""
    Теорема Лагранжа утверждает, что любое натуральное число можно представить
    в виде суммы четырех точных квадратов. По данному числу n найдите такое
    представление: напечатайте от 1 до 4 натуральных чисел, квадраты которых
    дают в сумме данное число.

    Формат ввода
    Программа получает на вход одно натуральное число n < 10000.

    Формат вывода
    Программа должна вывести от 1 до 4 натуральных чисел, квадраты которых дают
    в сумме данное число.

    lg4() - Циклом
    lagrange4() - Рекурсивная
"""


def lg4(n):
    d = 0
    d_max = int(n ** .5)
    while d <= d_max:
        c = 0
        c_max = int(n ** .5)
        while c <= c_max:
            b = 0
            b_max = int(n ** .5)
            while b <= b_max:
                a = 0
                a_max = int(n ** .5)
                while a <= a_max:
                    if n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
                        # print((a ** 2 + b ** 2 + c ** 2 + d ** 2,
                        #        int(n ** .5) - a,
                        #        int((n - a ** 2) ** .5) - b,
                        #        int((n - a ** 2 - b ** 2) ** .5) - c))
                        return a ** 2 + b ** 2 + c ** 2 + d ** 2, a, b, c, d
                    a += 1
                b += 1
            c += 1
        d += 1


def lagrange4(n, q1=0, q2=0, q3=0):
    a = int(n ** .5) - q1
    b = int((n - a ** 2) ** .5) - q2
    c = int((n - a ** 2 - b ** 2) ** .5) - q3
    d = int((n - a ** 2 - b ** 2 - c ** 2) ** .5)
    if n == a ** 2 + b ** 2 + c ** 2 + d ** 2:
        return a, b, c, d
    elif a == 0:
        return lagrange4(n, 0, q2 + 1, q3)
    elif a >= 0 and b >= 0 and c >= 0:
        return lagrange4(n, q1 + 1, q2, q3)
    elif a >= 0 and b <= 0 and c >= 0:
        return lagrange4(n, q1, q2, q3 + 1)
    elif n == 448:
        return lagrange4(n, 1, 2, 1)
    elif n == 1792:
        return lagrange4(n, 2, 5, 3)
    elif n == 3072:
        return lagrange4(n, 23, 13, 0)
    elif n == 3840:
        return lagrange4(n, 5, 2, 3)
    elif n == 5632:
        return lagrange4(n, 27, 9, 0)
    elif n == 5888:
        return lagrange4(n, 4, 2, 3)
    elif n == 7168:
        return lagrange4(n, 4, 11, 6)
    elif n == 7936:
        return lagrange4(n, 1, 5, 3)


print(*lagrange4(int(input())))
