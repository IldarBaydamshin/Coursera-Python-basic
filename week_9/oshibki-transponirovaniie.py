from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, lst1, lst2):
        self.matrix1 = lst1
        self.matrix2 = lst2


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
        if self.size() != other.size():
            raise MatrixError(self, other)
        else:
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

    def transpose(self):
        temp_list = []
        for c in range(self.size()[1]):
            temp_list.append([])
            for r in range(self.size()[0]):
                temp_list[c].append(self.lst[r][c])
        self.lst = temp_list
        return self

    @staticmethod
    def transposed(x):
        return Matrix([list(i) for i in zip(*copy.deepcopy(x.lst))])


exec(stdin.read())
