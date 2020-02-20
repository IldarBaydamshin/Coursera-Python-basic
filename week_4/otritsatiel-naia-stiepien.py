"""
    Дано действительное положительное число a и целое число n.
    Вычислите aⁿ. Решение оформите в виде функции power(a, n).
    Стандартной функцией возведения в степерь пользоваться нельзя.

    Формат ввода
    Вводится действительное положительное число a и целое число n.

    Формат вывода
    Выведите ответ на задачу.

    Примечания
    Здесь не нужна рекурсия.

"""


def power(a, n):
    if n:
        result = a
        trigger = n + abs(n)
        n = abs(n)
        while n != 1:
            result *= a
            n -= 1

        if trigger:
            return round(result, 6)
        return round(1 / round(result, 6), 6)
    return 1


base = float(input())
exponent = int(input())
print(power(base, exponent))
