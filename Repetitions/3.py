p = ''
m = 0
c = 0

for i in input():
    if p != i:
        m = max(m, c)
        c = 0

    c += 1
    p = i


print(max(m, c))
