"""
    Найдите наибольшее значение в списке и индекс последнего элемента,
    который имеет данное значение за один проход по списку,
    не модифицируя этот список и не используя дополнительного списка.

    Выведите два значения.

"""

maximum = 0
index = 0
counter = -1
for value in list(map(int, input().split())):
    counter += 1
    if maximum <= value:
        maximum = value
        index = counter
print(maximum, index)
