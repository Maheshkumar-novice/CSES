count = int(input())
array = [int(i) for i in input().split(' ')]

moves = 0
for i in range(1, count):
    if array[i] < array[i - 1]:
        moves += array[i - 1] - array[i]
        array[i] = array[i - 1]


print(moves)
