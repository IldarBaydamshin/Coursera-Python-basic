"""
    В данном списке из n≤10⁵ целых чисел найдите три числа,произведение которых
    максимально.
    Решение должно иметь сложность O(n), где n - размер списка. То есть
    сортировку использовать нельзя.

    Выведите три искомых числа в любом порядке.

"""

lst = list(map(int, input().split()))
min1 = min2 = 10 ** 5
max1 = max2 = max3 = - min1

for i in lst:
    if min1 > i:
        min1 = i
        if min2 > min1:
            min2, min1 = min1, min2

    if max1 < i:
        if max2 < i:
            if max3 < i:
                max3, max2, max1 = i, max3, max2
            else:
                max2, max1 = i, max2
        else:
            max1 = i

if min2 * min1 * max3 > max1 * max2 * max3:
    print(min2, min1, max3)
else:
    print(max1, max2, max3)
