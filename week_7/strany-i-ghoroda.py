"""
    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.

    Формат ввода
    Программа получает на вход количество стран N. Далее идет N строк, каждая
    строка начинается с названия страны, затем идут названия городов этой
    страны. Название каждого город состоит из одного слова. В следующей строке
    записано число M, далее идут M запросов — названия каких-то M городов,
    перечисленных выше.

    Формат вывода
    Для каждого из запроса выведите название страны, в котором находится данный
    город.

Примеры

Тест 1
Входные данные:
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Вывод программы:
Ukraine
Russia
Russia


"""

cities = {}
fin = open('input.txt', 'r', encoding='utf-8')
for i in range(int(fin.readline().strip())):
    country = fin.readline().strip().split()
    for city in country[1:]:
        cities[city] = country[0]

for i in range(int(fin.readline().strip())):
    print(cities[fin.readline().strip()])

fin.close()
