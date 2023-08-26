n = int(input())

from itertools import permutations

perm = permutations(list(range(1, n+1)))

for i in list(perm):
    flag = False
    for j in range(0, n):
        next_index = j + 1 if j != n -1 else None
        previous_index = j - 1 if j != 0 else None

        diff1 = None
        if next_index:
            diff1 = abs(i[next_index] - i[j])

        diff2 = None
        if previous_index:
            diff2 = abs(i[previous_index] - i[j])

        if diff1 == 1 or diff2 == 1:
            flag = True

        if flag:
            break

    if not flag:
        print(' '.join([str(k) for k in i]))
        break

    flag = False

print('NO SOLUTION')


