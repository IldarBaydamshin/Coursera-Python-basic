"""
    Дан многочлен P(x) = a[n] xⁿ+a[n-1] xⁿ⁻¹+...+a[1] x+a[0] и число x.
    Вычислите значение этого многочлена, воспользовавшись схемой Горнера:

    P(x) = (...((( a[n] x + a[n-1]) x + a[n-2]) x + a[n-3])...) x + a[0]

    Формат ввода
    Сначала программе подается на вход целое неотрицательное число n ≤ 20,
    затем действительное число x, затем следует n+1 вещественных
    чисел — коэффициенты многочлена от старшего к младшему.

    Формат вывода
    Программа должна вывести значение многочлена.

    Примечания
    При решении этой задачи нельзя использовать массивы и операцию возведения
    в степень. Программа должна иметь сложность O(n), то есть при увеличении
    количества входных данных в k раз время выполнения программы должно
    вырастать примерно в k раз.
"""

n = int(input())
x = float(input())
Px = 0
while n:
    v = x
    i = n
    while i - 1:
        v *= x
        i -= 1
    k = float(input())
    Px += k * v
    n -= 1
else:
    k = float(input())
    Px += k

print('{0:.1f}'.format(Px))