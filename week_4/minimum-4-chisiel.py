"""
    Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
    которая не содержит инструкции if, а использует стандартную функцию min
    от двух чисел. Считайте четыре целых числа и выведите их минимум.

"""


def minimum(a, b, c, d):
    return min(min(a, b), min(c, d))


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(minimum(a, b, c, d))
