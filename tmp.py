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
                        # print(a ** 2, b ** 2, c ** 2, d ** 2)
                        return a, b, c, d
                    a += 1
                b += 1
            c += 1
        d += 1


# print(lg4(23))

t = 0
for i in range(101):
    if lg4(i)[0]:
        print('_' * 10)
        print(i, lg4(i))
        t += 1
print('\n', 'OK', t)
