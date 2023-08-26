def a():
    n = int(input())

    if n == 2 or n == 3: 
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

a()
