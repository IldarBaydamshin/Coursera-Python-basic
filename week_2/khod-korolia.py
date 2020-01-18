h1 = int(input())
v1 = int(input())
h2 = int(input())
v2 = int(input())
if abs(h1 - h2) <= 1 and abs(v1 - v2) <= 1:
    print('YES')
else:
    print('NO')
