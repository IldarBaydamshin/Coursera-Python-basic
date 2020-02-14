"""
    Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
    Символы строки нумеруются, начиная с нуля.

Пример:
Тест 1
Входные данные:
Python

Вывод программы:
yton

"""

s1 = input()
s2 = ''
start = 0
for i in range(0, len(s1)):
    if not i % 3:
        end = i
        s2 += s1[start: end]
        start = end + 1

s2 += s1[start: len(s1)]
print(s2)
