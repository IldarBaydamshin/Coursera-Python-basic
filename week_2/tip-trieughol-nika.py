"""
 Даны три стороны треугольника a,b,c.
Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов:
rectangular для прямоугольного треугольника,
acute для остроугольного треугольника,
obtuse для тупоугольного треугольника или
impossible, если треугольника с такими сторонами не существует
(считаем, что вырожденный треугольник тоже невозможен).
"""
a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))

if a >= b >= c or a >= c >= b:
    hypotenuse = a
    leg1 = b
    leg2 = c
elif b >= a >= c or b >= c >= a:
    hypotenuse = b
    leg1 = a
    leg2 = c
elif c >= a >= b or c >= b >= a:
    hypotenuse = c
    leg1 = a
    leg2 = b

left = hypotenuse ** 2
right = leg1 ** 2 + leg2 ** 2

if left * right == 0 or hypotenuse >= leg1 + leg2:
    print('impossible')  # если треугольника с такими сторонами не существует
elif left == right:
    print('rectangular')  # для прямоугольного треугольника,
elif left < right:
    print('acute')  # для остроугольного треугольника,
elif left > right:
    print('obtuse')  # для тупоугольного треугольника или
