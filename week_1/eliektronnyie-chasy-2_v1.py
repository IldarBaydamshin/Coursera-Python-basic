v = 3601  # int(input())
ss = v % 60
mm = (v // 60) % 60
hh = (v // 3600) % 24
print(hh, '%02d' % mm, '%02d' % ss, sep=':')
