"""
    Дана база данных о продажах некоторого интернет-магазина. Каждая строка
    входного файла представляет собой запись вида

    Покупатель товар количество, где
    Покупатель — имя покупателя (строка без пробелов),
    товар — название товара (строка без пробелов),
    количество — количество приобретенных единиц товара.

    Создайте список всех покупателей, а для каждого покупателя подсчитайте
    количество приобретенных им единиц каждого вида товаров.

    Формат ввода
    Вводятся сведения о покупках в указанном формате.

    Формат вывода
    Выведите список всех покупателей в лексикографическом порядке,после имени
    каждого покупателя выведите двоеточие, затем выведите список названий всех
    приобретенных данным покупателем товаров в лексикографическом порядке,
    после названия каждого товара выведите количество единиц товара,
    приобретенных данным покупателем.Информация о каждом товаре выводится в
    отдельной строке.

Примеры

Тест 1
Входные данные:
Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5

Вывод программы:
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5



Тест 2
Входные данные:
Ivanov aaa 1
Petrov aaa 2
Sidorov aaa 3
Ivanov aaa 6
Petrov aaa 7
Sidorov aaa 8
Ivanov bbb 3
Petrov bbb 7
Sidorov aaa 345
Ivanov ccc 45
Petrov ddd 34
Ziborov eee 234
Ivanov aaa 45

Вывод программы:
Ivanov:
aaa 52
bbb 3
ccc 45
Petrov:
aaa 9
bbb 7
ddd 34
Sidorov:
aaa 356
Ziborov:
eee 234


"""

customers = {}

fin = open('input.txt', 'r', encoding='utf-8')
for line in fin:
    name, good, qty = line.strip().split()
    if name not in customers:
        customers[name] = {good: int(qty)}
    elif good not in customers[name]:
        customers[name].update({good: int(qty)})
    else:
        customers[name].update({good: customers[name].get(good) + int(qty)})
fin.close()

for name in sorted(customers):
    print(name + ':')
    for good in sorted(customers[name]):
        print(good, customers[name][good])
