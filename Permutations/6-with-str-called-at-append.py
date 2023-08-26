def a():
    n = int(input())

    if n == 1:
        print('1')
    if n in {2, 3}: 
        print('NO SOLUTION')
    else:
        r = []
        v = 2
        while v <= n:
            r.append(str(v))
            v += 2
    
        v = 1
        while v <= n:
            r.append(str(v))
            v += 2

        print(' '.join(r))

a()
