"""
    Дана последовательность натуральных чисел, завершающаяся числом 0.
    Определите наибольшую длину монотонного фрагмента последовательности
    (то есть такого фрагмента, где все элементы либо больше предыдущего,
    либо меньше).

    Формат ввода
    Вводится последовательность целых чисел, оканчивающаяся числом 0
    (само число 0 в последовательность не входит,
    а служит как признак ее окончания).

    Формат вывода
    Выведите ответ на задачу.
"""

a = int(input())
counter = 1
maximum = 1

b = int(input())
if b and b != a:
    counter = 2
    maximum = 2
    c = int(input())
elif b == a:
    counter = 1
    c = int(input())
else:
    c = 0

while c:
    if a < b < c or a > b > c:
        counter += 1
        if maximum < counter:
            maximum = counter
    else:
        if a < b > c or a > b < c:
            counter = 2
        else:
            counter = 1
    a, b = b, c
    c = int(input())

print(maximum)
