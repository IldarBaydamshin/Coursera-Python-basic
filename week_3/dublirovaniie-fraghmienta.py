"""
    Дана строка, в которой буква h встречается как минимум два раза.
    Выведите измененную строку: повторите последовательность символов,
    заключенную между первым и последним появлением буквы h два раза (сами
    буквы h не входят в повторяемый фрагмент, т. е. их повторять не надо).

    Формат ввода
    Вводится строка.

Пример:
In the hole in the ground there lived a hobbit

In th
     e hole in the ground there lived a
     e hole in the ground there lived a
                                        hobbit

"""

st = input()
ts = st[-1::-1]
head = st[:st.find('h') + 1]
body = st[st.find('h') + 1:len(st) - 1 - ts.find('h')]
tail = st[len(st) - ts.find('h') - 1:]

print(head + body * 2 + tail)
