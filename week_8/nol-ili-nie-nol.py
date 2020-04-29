import sys

print(
    not all(
        list(
            map(
                lambda x: int(sys.stdin.readline().strip()),
                range(int(sys.stdin.readline())))
        )
    )
)
