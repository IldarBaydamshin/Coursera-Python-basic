import functools

print(
    pow(
        functools.reduce(
            lambda x, y: x * y,
            list(
                map(
                    int,
                    input().split()
                )
            )
        ),
        5
    )
)
