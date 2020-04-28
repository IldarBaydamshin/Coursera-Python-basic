import sys
print(
    min(
        filter(
            lambda x: x % 2 == 1,
            map(
                int, (
                    sys.stdin.read()).split()
            )
        )
    )
)
