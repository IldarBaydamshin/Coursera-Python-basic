"""
    Процентная ставка по вкладу составляет P процентов годовых, которые
    прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
    Определите размер вклада через год. При решении этой задачи нельзя
    пользоваться условными инструкциями и циклами.

    Формат ввода
    Программа получает на вход целые числа P, X, Y.

    Формат вывода
    Программа должна вывести два числа: величину вклада через год в рублях и
    копейках. Дробная часть копеек отбрасывается.
"""

P, X, Y = int(input()), int(input()), int(input())

base = X * 100 + Y
percents = (base / 100) * P
deposit = base + percents

x = int(deposit // 100)
y = int(deposit - x * 100)

print(x, y)
