import sys
import itertools
import operator
from pprint import pprint

fin = open('input.txt')
f1 = (lambda k, n: (
    range(1, k + 1),
    tuple(map(lambda i: (i[:2], i[2:]),
              map(lambda _: tuple(map(int, fin.readline().split())),
                  range(n)))))
      )(*map(int, fin.readline().split()))
f2 = (lambda a, b: zip(itertools.permutations(a), itertools.repeat(b)))(*f1)


print(next(f2))

