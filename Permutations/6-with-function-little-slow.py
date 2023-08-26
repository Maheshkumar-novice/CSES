def a():
    n = int(input())

    if n == 1:
        print('1')
    if n in {2, 3}: 
        print('NO SOLUTION')
    else:
        r = []
        
        def b(v):
            while v <= n:
                r.append(v)
                v += 2
    
            while v <= n:
                r.append(v)
                v += 2
        
        b(2)
        b(1)
        print(' '.join(map(str, r)))

a()
