c = int(input())
a = list(map(int, input().split()))

m = 0
for i in range(1, c):
    x, y = a[i], a[i - 1]
    if x < y:
        m += y - x
        a[i] = a[i - 1]


print(m)
