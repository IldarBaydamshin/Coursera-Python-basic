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
                        print((a ** 2 + b ** 2 + c ** 2 + d ** 2,
                               int(n ** .5) - a,
                               int((n - a ** 2) ** .5) - b,
                               int((n - a ** 2 - b ** 2) ** .5) - c))
                        return a ** 2 + b ** 2 + c ** 2 + d ** 2, a, b, c, d
                    a += 1
                b += 1
            c += 1
        d += 1


def lg4all(n):
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
                        print((a ** 2 + b ** 2 + c ** 2 + d ** 2,
                               int(n ** .5) - a,
                               int((n - a ** 2) ** .5) - b,
                               int((n - a ** 2 - b ** 2) ** .5) - c))
                        print((a ** 2 + b ** 2 + c ** 2 + d ** 2, a, b, c, d))
                        print('_' * 9)
                    a += 1
                b += 1
            c += 1
        d += 1


def cube7all(n):
    g = 0
    g_max = int(n ** (1 / 3))
    while g <= g_max:
        f = 0
        f_max = int(n ** (1 / 3))
        while f <= f_max:
            e = 0
            e_max = int(n ** (1 / 3))
            while e <= e_max:
                d = 0
                d_max = int(n ** (1 / 3))
                while d <= d_max:
                    c = 0
                    c_max = int(n ** (1 / 3))
                    while c <= c_max:
                        b = 0
                        b_max = int(n ** (1 / 3))
                        while b <= b_max:
                            a = 0
                            a_max = int(n ** (1 / 3))
                            while a <= a_max:
                                sum_ = (
                                            a ** 3 + b ** 3 + c ** 3 + d ** 3 + e ** 3
                                            + f ** 3 + g ** 3)
                                if n == sum_:
                                    # print((sum_, a, b, c, d, e, f, g))
                                    # print('_' * 9)
                                    return sum_, a, b, c, d, e, f, g
                                a += 1
                            b += 1
                        c += 1
                    d += 1
                e += 1
            f += 1
        g += 1


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
    # elif n == 448:
    #     return lagrange4(n, 1, 2, 1)
    # elif n == 1792:
    #     return lagrange4(n, 2, 5, 3)
    # elif n == 3072:
    #     return lagrange4(n, 23, 13, 0)
    # elif n == 3840:
    #     return lagrange4(n, 5, 2, 3)
    # elif n == 5632:
    #     return lagrange4(n, 27, 9, 0)
    # elif n == 5888:
    #     return lagrange4(n, 4, 2, 3)
    # elif n == 7168:
    #     return lagrange4(n, 4, 11, 6)
    # elif n == 7936:
    #     return lagrange4(n, 1, 5, 3)
    # elif a and b < 0 and c < 0:
    #     return lagrange4(n, q1 + 1, q2, q3)

    return a, b, c, d


def cube7(n):
    if not n:
        return ''
    p = int(n ** (1 / 3)) ** 3
    print(p, end=' ')
    return cube7(n - p)


# print(lagrange4(448))
# print(lg4(448))
# print(lg4(1792))
# lg4all(1792)


def deep_test(n, deep=0):
    if deep > 996:
        return n, deep
    return deep_test(n + 1, deep + 1)


for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(i ** 3)


"""
    Напишите программу, которая представляет переданное натуральное число в
    виде суммы не более чем 7 кубов других натуральных чисел.

    Формат ввода
    Входная строка содержит целое число N, которое нужно представить в виде
    суммы кубов.

    Формат вывода
    Программа должна вывести любое разложение переданного ей числа в виде суммы
    не более чем 7 кубов других натуральных чисел. Если такое разложение
    невозможно, программа должна вывести число 0.

"""


def cube7(n, q1=0, q2=0, q3=0, q4=0, q5=0, q6=0, q7=0, deep=0):
    n1 = int((n ** (1 / 3)) - q1) ** 3
    n2 = int(((n - n1) ** (1 / 3)) - q2) ** 3
    n3 = int(((n - n1 - n2) ** (1 / 3)) - q3) ** 3
    n4 = int(((n - n1 - n2 - n3) ** (1 / 3)) - q4) ** 3
    n5 = int(((n - n1 - n2 - n3 - n4) ** (1 / 3)) - q5) ** 3
    n6 = int(((n - n1 - n2 - n3 - n4 - n5) ** (1 / 3)) - q6) ** 3
    n7 = int(((n - n1 - n2 - n3 - n4 - n5 - n6) ** (1 / 3)) - q7) ** 3

    total = n1 + n2 + n3 + n4 + n5 + n6 + n7

    if not n - total:
        return n1, n2, n3, n4, n5, n6, n7

    z = 8
    deep += 1
    # if n1 > z or n2 > z or n3 > z or n4 > z or n5 > z or n6 > z or n7 > z:
    #     if n2 > z or n3 > z or n4 > z or n5 > z or n6 > z or n7 > z:
    #         if n3 > z or n4 > z or n5 > z or n6 > z or n7 > z:
    #             if n4 > z or n5 > z or n6 > z or n7 > z:
    #                 if n5 > z or n6 > z or n7 > z:
    #                     if n6 > z or n7 > z:
    #                         if n7 > z:
    #                             return cube7(n, q1, q2, q3, q4, q5, q6, q7 + 1,
    #                                          deep)
    #                         return cube7(n, q1, q2, q3, q4, q5, q6 + 1, 0,
    #                                      deep)
    #                     return cube7(n, q1, q2, q3, q4, q5 + 1, 0, 0, deep)
    #                 return cube7(n, q1, q2, q3, q4 + 1, 0, 0, 0, deep)
    #             return cube7(n, q1, q2, q3 + 1, 0, 0, 0, 0, deep)
    #         return cube7(n, q1, q2 + 1, 0, 0, 0, 0, 0, deep)
    #     return cube7(n, q1 + 1, 0, 0, 0, 0, 0, 0, deep)

    if n1 > z:
        return cube7(n, q1 + 1, q2, q3, q4, q5, q6, q7, deep)
    if n2 > z:
        return cube7(n, q1, q2 + 1, q3, q4, q5, q6, q7, deep)
    if n3 > z:
        return cube7(n, q1, q2, q3 + 1, q4, q5, q6, q7, deep)
    if n4 > z:
        return cube7(n, q1, q2, q3, q4 + 1, q5, q6, q7, deep)
    if n5 > z:
        return cube7(n, q1, q2, q3, q4, q5 + 1, q6, q7, deep)
    if n6 > z:
        return cube7(n, q1, q2, q3, q4, q5, q6 + 1, q7, deep)
    if n7 > z:
        return cube7(n, q1, q2, q3, q4, q5, q6, q7 + 1, deep)

    # deep -= 1
    # return (n1, n2, n3, n4, n5, n6, n7), n8, n_8, 'End Deep =' + str(deep), deep
    return 0

# print(cube7(114))
# exit(0)
# counter = 0
# max_deep = 0
# for i in range(10001, 0, -1):
#     if cube7(i)[4] != 997:
#         max_deep = cube7(i)[4] if max_deep < cube7(i)[4] else max_deep
#
#     if cube7(i)[1]:
#         print(i, cube7(i))
#         counter += 1
#
# print('Count :', counter, '\nMax deep:', max_deep)

print(*cube7(int(input())))
