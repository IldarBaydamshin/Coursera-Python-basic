def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return f(n - 2) + f(n - 1)


print(f(8))

# rec()
