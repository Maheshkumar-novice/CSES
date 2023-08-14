n = int(input())
nums = set(input().split(' '))

for i in range(1, n + 1):
    if str(i) in nums:
        continue
    print(i)
