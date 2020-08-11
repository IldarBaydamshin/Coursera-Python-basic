from sys import stdin
import copy


class Matrix:

    def __init__(self, lst):
        self.lst = copy.deepcopy(lst)

    def __str__(self):
        str1 = []
        for i in range(len(self.lst)):
            str1.append('\t'.join(map(str, self.lst[i])))
        return '\n'.join(map(str, str1))

    def size(self):
        return len(self.lst), len(self.lst[0])

    def __add__(self, other):
        new_lst = []
        for row in range(self.size()[0]):
            temp_lst = []
            for item in range(self.size()[1]):
                temp_lst.append(self.lst[row][item] + other.lst[row][item])
            new_lst.append(temp_lst)
        return Matrix(new_lst)

    def __mul__(self, other):
        new_lst = []
        for row in range(self.size()[0]):
            temp_lst = []
            for item in range(self.size()[1]):
                temp_lst.append(self.lst[row][item] * other)
            new_lst.append(temp_lst)
        return Matrix(new_lst)

    __rmul__ = __mul__


exec(stdin.read())
