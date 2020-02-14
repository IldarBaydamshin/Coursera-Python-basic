"""
    Даны два действительных числа x и y. Проверьте, принадлежит ли точка с
    координатами (x,y) заштрихованному квадрату (включая его границу).
    Если точка принадлежит квадрату, выведите слово YES,
    иначе выведите слово NO.
    На рисунке сетка проведена с шагом 1.
    https://www.coursera.org/learn/python-osnovy-programmirovaniya/
    programming/GYhFu/prinadliezhit-li-tochka-kvadratu-1

    Решение должно содержать функцию IsPointInSquare(x, y),
    возвращающую True, если точка принадлежит квадрату
    и False, если не принадлежит.
    Основная программа должна считать координаты точки,
    вызвать функцию IsPointInSquare и в зависимости от возвращенного значения
    вывести на экран необходимое сообщение.
    Функция IsPointInSquare не должна содержать инструкцию if.


"""


def is_point_in_square(x, y):
    return abs(x) <= 1 and abs(y) <= 1


x = float(input())
y = float(input())

if is_point_in_square(x, y):
    print('YES')
else:
    print('NO')
