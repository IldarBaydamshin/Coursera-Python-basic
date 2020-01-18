a = int(input())
b = int(input())
no = (a % b + 2) % (a % b + 1)
yes = (no - 1) // - 1
print('YES' * yes + 'NO' * no)
