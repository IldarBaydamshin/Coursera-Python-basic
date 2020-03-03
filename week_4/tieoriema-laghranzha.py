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


def lg4(n, save=0, depth=0, key=1000, q=0):
    save = n if not save else save
    if not n and depth < 5:
        return depth, key

    elif not n and depth > 4:
        if key == 11340:
            return depth, key

        key = 11340 if key == 11160 else key
        key = 11160 if key == 11010 else key
        key = 11010 if key == 1900 else key

        key = 1900 if key == 1760 else key
        key = 1760 if key == 1710 else key
        key = 1710 if key == 1700 else key
        key = 1700 if key == 1674 else key

        key = 1674 if key == 1600 else key
        key = 1600 if key == 1553 else key
        key = 1553 if key == 1530 else key
        key = 1530 if key == 1510 else key

        key = 1510 if key == 1500 else key
        key = 1500 if key == 1443 else key
        key = 1443 if key == 1440 else key
        key = 1440 if key == 1410 else key

        key = 1410 if key == 1400 else key
        key = 1400 if key == 1330 else key
        key = 1330 if key == 1310 else key

        key = 1310 if key == 1300 else key
        key = 1300 if key == 1230 else key

        key = 1230 if key == 1220 else key
        key = 1220 if key == 1200 else key
        key = 1200 if key == 1211 else key

        key = 1211 if key == 1111 else key

        key = 1111 if key == 1120 else key
        key = 1120 if key == 1110 else key

        key = 1110 if key == 1011 else key
        key = 1011 if key == 1001 else key
        key = 1001 if key == 1010 else key
        key = 1010 if key == 1100 else key
        key = 1100 if key == 1000 else key

        return lg4(save, save, depth=0, key=key)
    elif n:

        q = 13 if key == 11340 and depth == 0 else q
        q = 4 if key == 11340 and depth == 1 else q

        q = 11 if key == 11160 and depth == 0 else q
        q = 6 if key == 11160 and depth == 1 else q
        q = 10 if key == 11010 and depth == 0 else q
        q = 1 if key == 11010 and depth == 1 else q

        q = 9 if key == 1900 and depth == 0 else q

        q = 7 if key == 1760 and depth == 0 else q
        q = 6 if key == 1760 and depth == 1 else q

        q = 7 if key == 1710 and depth == 0 else q
        q = 1 if key == 1710 and depth == 1 else q

        q = 7 if key == 1700 and depth == 0 else q

        q = 6 if key == 1674 and depth == 0 else q
        q = 7 if key == 1674 and depth == 1 else q
        q = 4 if key == 1674 and depth == 2 else q

        q = 6 if key == 1600 and depth == 0 else q
        q = 5 if key == 1553 and depth < 2 else q
        q = 3 if key == 1553 and depth == 2 else q
        q = 5 if key == 1530 and depth == 0 else q
        q = 3 if key == 1530 and depth == 1 else q

        q = 5 if key == 1510 and depth == 0 else q
        q = 1 if key == 1510 and depth == 1 else q
        q = 5 if key == 1500 and depth == 0 else q
        q = 4 if key == 1443 and depth < 2 else q
        q = 3 if key == 1443 and depth == 2 else q

        q = 4 if key == 1440 and depth < 2 else q

        q = 4 if key == 1410 and depth == 0 else q
        q = 1 if key == 1410 and depth == 1 else q

        q = 4 if key == 1400 and depth == 0 else q
        q = 3 if key == 1330 and depth < 2 else q

        q = 3 if key == 1310 and depth == 0 else q
        q = 1 if key == 1310 and depth == 1 else q
        q = 3 if key == 1300 and depth == 0 else q

        q = 2 if key == 1230 and depth == 0 else q
        q = 3 if key == 1230 and depth == 1 else q
        q = 2 if key == 1220 and depth < 2 else q
        q = 2 if key == 1211 and depth == 0 else q
        q = 1 if key == 1211 and 0 < depth < 3 else q
        q = 2 if key == 1200 and depth == 0 else q

        q = 1 if key == 1120 and depth == 0 else q
        q = 2 if key == 1120 and depth == 1 else q

        q = 1 if key == 1111 and depth < 3 else q
        q = 1 if key == 1110 and depth < 2 else q

        q = 1 if key == 1011 and 0 < depth < 3 else q
        q = 1 if key == 1001 and depth == 2 else q
        q = 1 if key == 1010 and depth == 1 else q
        q = 1 if key == 1100 and depth == 0 else q

        m = (int(n ** .5) - q) ** 2
        return lg4(n - m, save, depth + 1, key)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 23, 167, 7223]
# lg4(48)
# print()
print(lg4(704))
for i in range(10001):
    if lg4(i)[0] > 4:
        print('    n =', i)
        print('Depth =', lg4(i)[0])
        print('Variant', lg4(i)[1])
        print('-' * 9)
        # if lg4(i)[0] > 4:
        #     exit(0)

print('OK')
