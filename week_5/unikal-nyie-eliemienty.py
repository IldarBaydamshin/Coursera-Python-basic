"""
    Дан список. Выведите те его элементы, которые встречаются в списке только
    одинраз. Элементы нужно выводить в том порядке, в котором они встречаются
    в списке.

    Формат ввода
    Вводится список чисел. Все числа списка находятся на одной строке.

"""

lst = list(map(int, input().split()))
unique = []
for i in range(len(lst)):
    qty = -1
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            qty += 1
        if qty > 0:
            break
    else:
        if qty == 0:
            unique.append(lst[i])

print(*unique)
