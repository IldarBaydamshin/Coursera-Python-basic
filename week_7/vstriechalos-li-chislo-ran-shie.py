"""
    Во входной строке записана последовательность чисел через пробел.
    Для каждого числа выведите слово YES (в отдельной строке), если это число
    ранее встречалось в последовательности или NO, если не встречалось.

    Формат ввода
    Вводится список чисел. Все числа списка находятся на одной строке.

    Формат вывода
    Выведите ответ на задачу.

Примеры

Тест 1
Входные данные:
1 2 3 2 3 4

Вывод программы:
NO
NO
NO
YES
YES
NO

"""

# lst = list(map(int, input().split()))
# st = set()
# last_len = 0
# for i in lst:
#     st.add(i)
#     if len(st) > last_len:
#         print('NO')
#         last_len += 1
#     else:
#         print('YES')


lst = list(map(int, input().split()))
st = set()
for i in lst:
    if i in st:
        print('YES')
    else:
        print('NO')
        st.add(i)
