"""
    Даны два целых числа A и В.
    Выведите все числа от A до B включительно, в порядке возрастания,
    если A < B, или в порядке убывания в противном случае.

    Формат ввода
    Вводятся два целых числа.

"""

a = int(input())
b = int(input())
if a <= b:
    print(*tuple(range(a, b + 1)))
else:
    print(*tuple(range(a, b - 1, -1)))
