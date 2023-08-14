n = int(input())
n = (n * (n + 1) // 2)
sum = 0
for i in input().split(' '):
     sum += int(i)
 
print(n - sum)
