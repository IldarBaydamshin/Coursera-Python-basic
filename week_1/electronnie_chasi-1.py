N = int(input())
N = N % (24 * 60)
hh = N // 60
mm = N % 60
print(hh, mm)
