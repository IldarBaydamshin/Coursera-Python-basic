"""
    Даны числа a, b, c, d, e.
    Подсчитайте количество таких целых чисел от 0 до 1000 (включительно),
    которые являются корнями уравнения (ax³+bx²+cx+d)/(x-e)=0,
    и выведите их количество.

    Формат ввода
    Вводятся целые числа a, b, c, d и e.

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
counter = 0

for x in range(1001):
    if not a * x ** 3 + b * x ** 2 + c * x + d and x - e:
        counter += 1

print(counter)
