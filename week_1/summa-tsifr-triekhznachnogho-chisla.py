N = int(input())
n1 = N % 10
n2 = (N % 100) // 10
n3 = N // 100
print(n3 + n2 + n1)
