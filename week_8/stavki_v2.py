import sys
import itertools
import operator
from pprint import pprint

fin = open('input.txt')
# f1 = map(lambda kn: int(kn), fin.readline().split())
# f2 = tuple(zip(*((lambda x, y: (
#     tuple(itertools.permutations(range(1, x + 1))),
#     tuple(itertools.repeat(
#         tuple(itertools.chain(
#             *map(lambda _: map(int, fin.readline().split()), range(y)))),
#         len(tuple(itertools.permutations(range(x))))))))(*f1))))

f1 = map(lambda kn: int(kn), fin.readline().split())
f2 = tuple(zip(*((lambda x, y: (
    tuple(itertools.permutations(range(1, x + 1))),
    tuple(itertools.repeat(
            tuple(map(lambda i: (i[:2], i[2:]), map(lambda _: tuple(map(int, fin.readline().split())), range(y)))),
        len(tuple(itertools.permutations(range(x))))
    ))))(*f1))))

pprint(f2)
