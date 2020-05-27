import itertools
import operator

print(next(map(lambda res: res[0], filter(lambda res: res[1], map(lambda a: (
    ' '.join(map(str, a[0])),
    all(map(lambda b:
                  operator.xor(*map(lambda c:
                                    c in itertools.combinations(a[0], 2), b)),
                  a[1]))),
         map(lambda a: a, (lambda a, b:
                                 (dict.fromkeys(
                                     itertools.permutations(range(1, a + 1)),
                                     tuple(map(lambda i:
                                               (i[:2], i[2:]),
                                               map(lambda _:
                                                   tuple(map(int,
                                                             input().split())),
                                                   range(b))))))
                                 )(
             *map(lambda kn: int(kn), input().split())).items())))), 0))
