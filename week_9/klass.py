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


exec(stdin.read())
