"""
    Даны два целых числа A и B (при этом A≤B).
    Выведите все числа от A до B включительно.

    Формат ввода
    Вводятся два целых числа.


"""

a = int(input())
b = int(input())

print(*tuple(range(a, b + 1)))
