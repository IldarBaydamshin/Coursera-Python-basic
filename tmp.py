def f(n):
    if n == 0:
        return n
    i = 0
    m = int((n ** .5) - i)
    print(m ** 2, end=' ')
    f(n - m ** 2)


n = 23
f(n)
