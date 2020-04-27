"""
    В генеалогическом древе у каждого человека, кроме родоначальника, есть
    ровно один родитель. Каждом элементу дерева сопоставляется целое
    неотрицательное число, называемое высотой. У родоначальника высота равна 0,
    у любого другого элемента высота на 1 больше, чем у его родителя.
    Вам дано генеалогическое древо, определите высоту всех его элементов.

    Формат ввода
    Программа получает на вход число элементов в генеалогическом древе N.
    Далее следует N-1 строка, задающие родителя для каждого элемента древа,
    кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

    Формат вывода
    Программа должна вывести список всех элементов древа в лексикографическом
    порядке. После вывода имени каждого элемента необходимо вывести его высоту.

    Примечания
    Эта задача имеет решение сложности O(n), но вам достаточно написать решение
    сложности O(n²) (не считая сложности обращенияк элементам словаря).
    Пример ниже соответствует приведенному древу рода Романовых.

Примеры


Тест 1
Входные данные:
9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I

Вывод программы:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2



Тест 2
Входные данные:
10
AQHFYP MKFXCLZBT
AYKOTYQ QIUKGHWCDC
IWCGKHMFM WPLHJL
MJVAURUDN QIUKGHWCDC
MKFXCLZBT IWCGKHMFM
PUTRIPYHNQ UQNGAXNP
QIUKGHWCDC WPLHJL
UQNGAXNP WPLHJL
YURTPJNR QIUKGHWCDC

Вывод программы:
AQHFYP 3
AYKOTYQ 2
IWCGKHMFM 1
MJVAURUDN 2
MKFXCLZBT 2
PUTRIPYHNQ 2
QIUKGHWCDC 1
UQNGAXNP 1
WPLHJL 0
YURTPJNR 2



Тест 3
Входные данные:
10
BFNRMLH CSZMPFXBZ
CSZMPFXBZ IHWBQDJ
FMVQTU FUXATQUGIG
FUXATQUGIG IRVAVMQKN
GNVIZ IQGIGUJZ
IHWBQDJ LACXYFQHSQ
IQGIGUJZ JMUPNYRQD
IRVAVMQKN GNVIZ
JMUPNYRQD BFNRMLH

Вывод программы:
BFNRMLH 3
CSZMPFXBZ 2
FMVQTU 9
FUXATQUGIG 8
GNVIZ 6
IHWBQDJ 1
IQGIGUJZ 5
IRVAVMQKN 7
JMUPNYRQD 4
LACXYFQHSQ 0

"""

generation = {}
tree = {}
filein = open('input.txt', 'r', encoding='utf-8')
for N in range(int(filein.readline()) - 1):
    child, parent = filein.readline().split()
    generation[child] = generation.get(child, parent)
filein.close()

parents = set(generation.values())
children = set(generation.keys())
root = (parents - children).pop()

level = 0
tree[level] = [root]

while children:
    children = {x for x in generation if generation[x] in tree[level]}
    level += 1
    for name in children:
        if tree.get(level):
            tree[level].append(name)
        else:
            tree[level] = [name]

for i in tree:
    for v in tree[i]:
        generation[v] = i

for name in sorted(generation):
    print(name, generation[name])
