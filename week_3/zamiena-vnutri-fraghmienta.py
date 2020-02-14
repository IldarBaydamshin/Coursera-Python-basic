"""
    Дана строка. Замените в этой строке все появления буквы h на букву H,
    кроме первого и последнего вхождения.

Пример:
Входные данные:
In the hole in the ground there lived a hobbit

Вывод программы:
In the Hole in tHe ground tHere lived a hobbit

"""

s = input()

head = s[:s.find('h') + 1]
body = s[s.find('h') + 1:s.rfind('h')].replace('h', 'H')
tail = s[s.rfind('h'):]
s = head + body + tail

print(s)
