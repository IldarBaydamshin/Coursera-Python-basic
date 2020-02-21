"""
    По данным целым числам n и k (0≤k≤n) вычислите C из n по k.

    Решение оформите в виде функции C(n, k).

    Для решения используйте рекуррентное соотношение:
    C K|N = C K|N-1 + C K-1|N-1
    см по ссылке
    https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/
    QEiwQ/chislo-sochietanii

    И равенства:
    С(n, 1)=n
    C(n, n)=1

    Формат ввода
    Вводятся удовлетворяющие условию задачи числа n и k.

    Формат вывода
    Выведите ответ на задачу.

"""


def c(n, k):
    if k == 1:
        return n
    elif n == k or k == 0:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)


N = int(input())
K = int(input())
print(c(N, K))
