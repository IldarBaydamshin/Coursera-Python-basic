"""
    Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
    Если таких слов несколько, выведите то, которое меньше в лексикографическом
    порядке.

    Формат ввода
    Вводится текст.

    Формат вывода
    Выведите ответ на задачу.

Примеры

Тест 1
Входные данные:
apple orange banana banana orange

Вывод программы:
banana



Тест 2
Входные данные:
oh you touch my tralala mmm my ding ding dong

Вывод программы:
ding



Тест 3
Входные данные:
q w e r t y u i o p
a s d f g h j k l
z x c v b n m

Вывод программы:
a

"""

fin = open('input.txt', 'r', encoding='utf-8')
words = {}
for word in fin.read().strip().split():
    words[word] = words.get(word, 0) + 1
fin.close()
maximum = max(words.values())
max_words = []

for i in words:
    if words[i] == maximum:
        max_words.append(i)
print(min(max_words))
