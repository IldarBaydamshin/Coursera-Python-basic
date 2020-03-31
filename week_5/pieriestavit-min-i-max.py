"""
    В списке все элементы попарно различны. Поменяйте местами минимальный и
    максимальный элемент этого списка.

    Формат ввода
    Вводится список целых чисел. Все числа списка находятся на одной строке.

"""

lst = list(map(int, input().split()))
mini, maxi = (lst[0], 0), (lst[0], 0)

for i in range(len(lst)):
    if lst[i] < mini[0]:
        mini = lst[i], i
    if lst[i] > maxi[0]:
        maxi = lst[i], i
else:
    lst[mini[1]], lst[maxi[1]] = lst[maxi[1]], lst[mini[1]]

print(*lst)
