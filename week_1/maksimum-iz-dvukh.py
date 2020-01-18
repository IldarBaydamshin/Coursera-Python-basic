a = int(input())
b = int(input())
avg = (a + b) // 2
x = a * (a // (avg + 1))
y = b * (b // (avg + 1))
z = avg * ((a + 1) // (b + 1)) * ((b + 1) // (a + 1))
print(x + y + z)
