h1 = int(input())
v1 = int(input())
h2 = int(input())
v2 = int(input())
d1 = abs(v1 % 2 - h1 % 2)
d2 = abs(v2 % 2 - h2 % 2)
if abs(d1 - d2):
    print('NO')
else:
    print('YES')
