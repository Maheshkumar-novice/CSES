n = int(input())
n = (n * (n + 1) // 2)
sum = 0

buffer = ''
for i in input():
    if i == ' ':
        sum += int(buffer)
        buffer = ''
        continue
    buffer += i

if buffer:
    sum += int(buffer)

print(n - sum)
