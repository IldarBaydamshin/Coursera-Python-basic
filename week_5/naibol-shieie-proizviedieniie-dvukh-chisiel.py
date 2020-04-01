"""
    Дан список, заполненный произвольными целыми числами.
    Найдите в этом списке два числа, произведение которых максимально.
    Выведите эти числа в порядке неубывания.

    Решение должно иметь сложность O(n), где n - размер списка.
    То есть сортировку использовать нельзя.

"""

lst = list(map(int, input().split()))
max1, max2, min1, min2 = lst[0], lst[0], lst[0], lst[0]

for i in range(len(lst)):
    if lst[i] >= max1:
        max1 = lst[i]
        if max1 > max2:
            max1, max2 = max2, max1
    if lst[i] <= min1:
        min1 = lst[i]
        if min1 < min2:
            min1, min2 = min2, min1
if min1 * min2 > max1 * max2:
    print(min2, min1)
else:
    print(max1, max2)
