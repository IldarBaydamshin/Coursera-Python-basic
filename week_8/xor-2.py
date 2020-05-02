from sys import stdin
from functools import reduce
from operator import xor

print(
    *reduce(
        lambda a, b: map(xor, a, b),
        list(
            map(
                lambda _: map(
                    int, stdin.readline().strip().split()
                ), range(
                    int(
                        stdin.readline()
                    )
                )
            )
        )
    )
)
