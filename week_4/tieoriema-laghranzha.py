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


"""


def lg4(n, save=0, depth=0, var=1000, q=0):
    save = n if not save else save
    if not n and depth < 5:
        return depth, var

    elif not n and depth > 4:
        if var == 1530:
            return depth, var

        var = 1530 if var == 1500 else var
        var = 1500 if var == 1400 else var
        var = 1400 if var == 1300 else var
        var = 1300 if var == 1220 else var
        var = 1220 if var == 1211 else var
        var = 1211 if var == 1110 else var
        var = 1110 if var == 1010 else var
        var = 1010 if var == 1100 else var
        var = 1100 if var == 1000 else var

        return lg4(save, save, depth=0, var=var)
    elif n:
        q = 5 if var == 1530 and depth == 0 else q
        q = 3 if var == 1530 and depth == 1 else q
        q = 5 if var == 1500 and depth == 0 else q
        q = 4 if var == 1400 and depth == 0 else q
        q = 3 if var == 1300 and depth == 0 else q
        q = 2 if var == 1220 and depth < 2 else q
        q = 2 if var == 1211 and depth == 0 else q
        q = 1 if var == 1211 and 0 < depth < 3 else q
        q = 1 if var == 1110 and depth < 2 else q
        q = 1 if var == 1010 and depth == 1 else q
        q = 1 if var == 1100 and depth == 0 else q

        m = (int(n ** .5) - q) ** 2
        return lg4(n - m, save, depth + 1, var)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 23, 167, 7223]
# lg4(48)
# print()
# print(lg4(7))
for i in range(10001):
    if lg4(i)[0]:
        print('    n =', i)
        print('Depth =', lg4(i)[0])
        print('Variant', lg4(i)[1])
        print('-' * 9)
        if lg4(i)[0] > 4:
            break

print('OK')
