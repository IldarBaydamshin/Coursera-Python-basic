n = int(input())
left = (n // 10 ** 2) % 100
right = (n % 10) * 10 + ((n // 10 ** 1) % 10)
print(left - right + 1)
