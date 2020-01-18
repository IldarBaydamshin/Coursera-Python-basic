v1 = int(input())
h1 = int(input())
v2 = int(input())
h2 = int(input())
d1 = abs(v1 % 2 - h1 % 2)
d2 = abs(v2 % 2 - h2 % 2)
if abs(d1 - d2) or h1 >= h2 or (abs(h2 - h1) < abs(v2 - v1)):
    print('NO')
else:
    print('YES')
