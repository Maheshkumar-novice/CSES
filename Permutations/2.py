n = int(input())

if n in [2, 3]:
    print('NO SOLUTION')
    exit()

v = 2

while v <= n:
    print(v, end=' ')
    v += 2

v = 1

while v <= n:
    print(v, end=' ')
    v += 2

