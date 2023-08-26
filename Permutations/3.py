def a():
    n = int(input())

    if n in {2, 3}: 
        print('NO SOLUTION')
        exit()

    def b(v):
        while v <= n:
            print(v, end=' ')
            v += 2
    b(2)
    b(1)

a()
