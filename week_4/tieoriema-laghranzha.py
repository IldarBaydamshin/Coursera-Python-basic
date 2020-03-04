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
        if key == 123140:
            return depth, key

        key = 123140 if key == 12710 else key

        key = 12710 if key == 12600 else key

        key = 12600 if key == 12200 else key

        key = 12200 if key == 12100 else key

        key = 12100 if key == 12090 else key

        key = 12090 if key == 11900 else key
        key = 11900 if key == 11800 else key

        key = 11800 if key == 11700 else key
        key = 11700 if key == 11580 else key

        key = 11580 if key == 12300 else key

        key = 12300 if key == 114130 else key

        key = 114130 if key == 11420 else key

        key = 11440 if key == 11420 else key

        key = 11420 if key == 11360 else key

        key = 11360 if key == 11340 else key
        key = 11340 if key == 11300 else key

        key = 11300 if key == 11171 else key

        key = 11171 if key == 11170 else key

        key = 11170 if key == 11160 else key

        key = 11160 if key == 11110 else key

        key = 11110 if key == 11010 else key
        key = 11010 if key == 11000 else key
        key = 11000 if key == 1900 else key

        key = 1900 if key == 1800 else key
        key = 1800 if key == 1760 else key

        key = 1760 if key == 1730 else key
        key = 1730 if key == 1710 else key
        key = 1710 if key == 1700 else key
        key = 1700 if key == 1690 else key

        key = 1690 if key == 1674 else key
        key = 1674 if key == 1660 else key

        key = 1660 if key == 1610 else key

        key = 1610 if key == 1600 else key
        key = 1600 if key == 1553 else key
        key = 1553 if key == 1530 else key
        key = 1530 if key == 1510 else key

        key = 1510 if key == 1500 else key
        key = 1500 if key == 1443 else key
        key = 1443 if key == 1440 else key
        key = 1440 if key == 1416 else key

        key = 1416 if key == 14116 else key

        key = 14116 if key == 1560 else key

        key = 1560 if key == 1520 else key

        key = 1520 if key == 1410 else key

        key = 1410 if key == 1400 else key
        key = 1400 if key == 1360 else key

        key = 1360 if key == 1330 else key

        key = 1330 if key == 1310 else key

        key = 1310 if key == 1301 else key
        key = 1301 if key == 1300 else key
        key = 1300 if key == 1260 else key

        key = 1260 if key == 1253 else key

        key = 1253 if key == 1250 else key
        key = 1250 if key == 1240 else key
        key = 1240 if key == 1230 else key

        key = 1230 if key == 1220 else key
        key = 1220 if key == 1200 else key
        key = 1200 if key == 1211 else key

        key = 1211 if key == 1210 else key
        key = 1210 if key == 1153 else key

        key = 1153 if key == 1150 else key

        key = 1150 if key == 1140 else key
        key = 1140 if key == 1130 else key

        key = 1130 if key == 1120 else key
        key = 1120 if key == 1111 else key

        key = 1111 if key == 1110 else key
        key = 1110 if key == 1011 else key
        key = 1011 if key == 1001 else key
        key = 1001 if key == 1030 else key
        key = 1030 if key == 1010 else key
        key = 1010 if key == 1021 else key
        key = 1021 if key == 1100 else key

        key = 1100 if key == 1000 else key

        return lg4(save, save, depth=0, key=key)
    elif n:

        q = 27 if key == 12710 and depth == 0 else q
        q = 1 if key == 12710 and depth == 1 else q

        q = 26 if key == 12600 and depth == 0 else q
        q = 22 if key == 12200 and depth == 0 else q

        q = 21 if key == 12100 and depth == 0 else q

        q = 20 if key == 12090 and depth == 0 else q
        q = 9 if key == 12090 and depth == 1 else q

        q = 13 if key == 11300 and depth == 0 else q
        q = 23 if key == 123140 and depth == 0 else q
        q = 14 if key == 123140 and depth == 1 else q

        q = 19 if key == 11900 and depth == 0 else q

        q = 18 if key == 11800 and depth == 0 else q
        q = 17 if key == 11700 and depth == 0 else q

        q = 23 if key == 12300 and depth == 0 else q

        q = 15 if key == 11580 and depth == 0 else q
        q = 8 if key == 11580 and depth == 1 else q

        q = 14 if key == 11420 and depth == 0 else q
        q = 2 if key == 11420 and depth == 1 else q

        q = 14 if key == 11440 and depth == 0 else q
        q = 4 if key == 11440 and depth == 1 else q

        q = 14 if key == 114130 and depth == 0 else q
        q = 13 if key == 114130 and depth == 1 else q

        q = 13 if key == 11360 and depth == 0 else q
        q = 6 if key == 11360 and depth == 1 else q

        q = 13 if key == 11340 and depth == 0 else q
        q = 4 if key == 11340 and depth == 1 else q

        q = 11 if key == 11171 and depth == 0 else q
        q = 7 if key == 11171 and depth == 1 else q
        q = 1 if key == 11171 and depth == 2 else q

        q = 11 if key == 11170 and depth == 0 else q
        q = 7 if key == 11170 and depth == 1 else q

        q = 11 if key == 11160 and depth == 0 else q
        q = 6 if key == 11160 and depth == 1 else q

        q = 11 if key == 11110 and depth == 0 else q
        q = 1 if key == 11110 and depth == 1 else q

        q = 10 if key == 11010 and depth == 0 else q
        q = 1 if key == 11010 and depth == 1 else q

        q = 10 if key == 11000 and depth == 0 else q

        q = 9 if key == 1900 and depth == 0 else q

        q = 7 if key == 1760 and depth == 0 else q
        q = 6 if key == 1760 and depth == 1 else q

        q = 7 if key == 1710 and depth == 0 else q
        q = 1 if key == 1710 and depth == 1 else q

        q = 8 if key == 1800 and depth == 0 else q

        q = 7 if key == 1730 and depth == 0 else q
        q = 3 if key == 1730 and depth == 1 else q

        q = 7 if key == 1700 and depth == 0 else q

        q = 6 if key == 1690 and depth == 0 else q
        q = 9 if key == 1690 and depth == 1 else q

        q = 6 if key == 1674 and depth == 0 else q
        q = 7 if key == 1674 and depth == 1 else q
        q = 4 if key == 1674 and depth == 2 else q

        q = 6 if key == 1660 and depth == 0 else q
        q = 6 if key == 1660 and depth == 1 else q

        q = 6 if key == 1610 and depth == 0 else q
        q = 1 if key == 1610 and depth == 1 else q

        q = 6 if key == 1600 and depth == 0 else q

        q = 5 if key == 1560 and depth == 0 else q
        q = 6 if key == 1560 and depth == 1 else q

        q = 5 if key == 1553 and depth < 2 else q
        q = 3 if key == 1553 and depth == 2 else q
        q = 5 if key == 1530 and depth == 0 else q
        q = 3 if key == 1530 and depth == 1 else q

        q = 5 if key == 1520 and depth == 0 else q
        q = 2 if key == 1520 and depth == 1 else q

        q = 5 if key == 1510 and depth == 0 else q
        q = 1 if key == 1510 and depth == 1 else q
        q = 5 if key == 1500 and depth == 0 else q
        q = 4 if key == 1443 and depth < 2 else q
        q = 3 if key == 1443 and depth == 2 else q

        q = 4 if key == 1440 and depth < 2 else q

        q = 4 if key == 14116 and depth == 0 else q
        q = 11 if key == 14116 and depth == 1 else q
        q = 6 if key == 14116 and depth == 2 else q

        q = 4 if key == 1410 and depth == 0 else q
        q = 1 if key == 1410 and depth == 1 else q

        q = 4 if key == 1400 and depth == 0 else q

        q = 3 if key == 1360 and depth == 0 else q
        q = 6 if key == 1360 and depth == 1 else q

        q = 3 if key == 1330 and depth < 2 else q

        q = 3 if key == 1310 and depth == 0 else q
        q = 1 if key == 1310 and depth == 1 else q

        q = 3 if key == 1301 and depth == 0 else q
        q = 1 if key == 1301 and depth == 2 else q

        q = 3 if key == 1300 and depth == 0 else q

        q = 2 if key == 1260 and depth == 0 else q
        q = 6 if key == 1260 and depth == 1 else q

        q = 2 if key == 1253 and depth == 0 else q
        q = 5 if key == 1253 and depth == 1 else q
        q = 3 if key == 1253 and depth == 2 else q

        q = 2 if key == 1250 and depth == 0 else q
        q = 5 if key == 1250 and depth == 1 else q

        q = 2 if key == 1240 and depth == 0 else q
        q = 4 if key == 1240 and depth == 1 else q

        q = 2 if key == 1230 and depth == 0 else q
        q = 3 if key == 1230 and depth == 1 else q
        q = 2 if key == 1220 and depth < 2 else q
        q = 2 if key == 1211 and depth == 0 else q
        q = 1 if key == 1211 and 0 < depth < 3 else q

        q = 2 if key == 1210 and depth == 0 else q
        q = 1 if key == 1210 and depth == 1 else q

        q = 2 if key == 1200 and depth == 0 else q

        q = 1 if key == 1153 and depth == 0 else q
        q = 5 if key == 1153 and depth == 1 else q
        q = 3 if key == 1153 and depth == 2 else q

        q = 1 if key == 1150 and depth == 0 else q
        q = 5 if key == 1150 and depth == 1 else q

        q = 1 if key == 1140 and depth == 0 else q
        q = 4 if key == 1140 and depth == 1 else q

        q = 1 if key == 1130 and depth == 0 else q
        q = 3 if key == 1130 and depth == 1 else q

        q = 1 if key == 1120 and depth == 0 else q
        q = 2 if key == 1120 and depth == 1 else q

        q = 1 if key == 1111 and depth < 3 else q
        q = 1 if key == 1110 and depth < 2 else q

        q = 1 if key == 1011 and 0 < depth < 3 else q
        q = 1 if key == 1001 and depth == 2 else q

        q = 3 if key == 1030 and depth == 1 else q

        q = 2 if key == 1021 and depth == 1 else q
        q = 1 if key == 1021 and depth == 2 else q

        q = 1 if key == 1010 and depth == 1 else q
        q = 1 if key == 1100 and depth == 0 else q

        m = (int(n ** .5) - q) ** 2
        return lg4(n - m, save, depth + 1, key)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 23, 167, 7223]
# lg4(48)
# print()
# print(lg4(704))
t = 0
for i in range(10001):
    if lg4(i)[0] > 4:
        print()
        print('=' * 10)
        print('    n =', i)
        print('Depth =', lg4(i)[0])
        print('Variant', lg4(i)[1])
        print('-' * 9)

        relay = i
        t += 1

        print()
        n = relay
        print(n)
        print()
        a, b, c, d = 0, 0, 0, 0
        ia = 0
        a = ia ** 2
        stopper = 0
        while a <= n:
            ib = 0
            b = ib ** 2
            while b <= (n - a):
                ic = 0
                c = ic ** 2
                while c <= (n - a - b):
                    id_ = 0
                    d = id_ ** 2
                    while d <= (n - a - b - c):
                        head = a + b + c + d
                        tail = n - head
                        if tail == 0:
                            td = n - d
                            tc = td - c
                            tb = tc - b
                            print(d, c, b, a)
                            # print('tails', td, tc, tb)
                            stopper = 1
                            break
                        if stopper:
                            break
                        id_ += 1
                        d = id_ ** 2
                    if stopper:
                        break
                    ic += 1
                    c = ic ** 2
                if stopper:
                    break
                ib += 1
                b = ib ** 2
            if stopper:
                break
            ia += 1
            a = ia ** 2

        print()
        print('-' * 9, d)
        m = int(n ** .5)
        for i in range(m, 0, -1):
            if i ** 2 == d:
                print(m - i, '-', i ** 2)

        print('-' * 9, c)
        m = int(td ** .5)
        for i in range(m, 0, -1):
            if i ** 2 == c:
                print(m - i, '-', i ** 2)

        print('-' * 9, b)

        m = int(tc ** .5)
        for i in range(m, 0, -1):
            if i ** 2 == b:
                print(m - i, '-', i ** 2)

#

print()
print('OK', t)
