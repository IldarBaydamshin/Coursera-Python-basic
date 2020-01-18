n = int(input())
if n % 10 == 0 or 5 <= n % 100 <= 19:
    print(n, 'korov')
elif 5 <= n % 10 <= 9:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
