
def min_devisor(x):
    d = 2
    while x % d:
        d += 1
    return d


print(min_devisor(int(input())))

