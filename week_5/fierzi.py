"""
    Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
    друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли
    среди них пара бьющих друг друга.

    Формат ввода

    Программа получает на вход восемь пар чисел,
    каждое число от 1 до 8 - координаты 8 ферзей.

    Формат вывода
    Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

    Примеры
    Тест 1
    Входные данные:
    1 7
    2 4
    3 2
    4 8
    5 6
    6 1
    7 3
    8 5

    Вывод программы:
    NO


    Тест 2
    Входные данные:
    1 8
    2 7
    3 6
    4 5
    5 4
    6 3
    7 2
    8 1

    Вывод программы:
    YES


    Тест 3
    Входные данные:
    3 4
    8 5
    4 1
    7 3
    6 6
    1 7
    5 8
    2 2

    Вывод программы:
    YES

"""


def is_queen_attacks(h1, v1, h2, v2):
    """ This procedure calculates if the the figure attacked by the queen.
        return True or False
    """
    horizontal = h1 == h2
    vertical = v1 == v2
    diagonal = abs(h1 - h2) == abs(v1 - v2)
    return horizontal or vertical or diagonal


answer = 'NO'
queens = []
for i in range(8):
    queens.append(tuple(map(int, input().split())))

for i in range(8):
    for j in range(8):
        if i == j:
            continue
        if is_queen_attacks(*queens[i], *queens[j]):
            answer = 'YES'

print(answer)
