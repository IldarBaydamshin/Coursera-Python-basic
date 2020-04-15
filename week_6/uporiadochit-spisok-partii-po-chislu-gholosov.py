"""
    Формат входных данных аналогичен предыдущей задаче.
    'siemiprotsientnyi-bar-ier.py'
    Выведите список всех партий, участвовавших в выборах, отсортировав его в
    порядке убывания количества голосов избирателей, а при равном количестве
    голосов - в лексикографическом порядке.



Примеры
Тест 1
Входные данные:
PARTIES:
Party one
Party two
Party three
VOTES:
Party one
Party two
Party three
Party two
Party three

Вывод программы:
Party three
Party two
Party one

"""

infile = open('input.txt', 'r', encoding='utf8')
infile.readline()
votes = []
total = 0
mode = 1
for line in infile:
    if line.rstrip() == 'VOTES:':
        mode = 0
    if mode:
        votes.append([0, line.strip()])
    else:
        for i in votes:
            if line.strip() == i[1]:
                i[0] -= 100
                total += 1
votes.sort()

for i in votes:
    print(i[1])

infile.close()
