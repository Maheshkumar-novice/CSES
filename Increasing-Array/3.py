def main(c, a):
    m = 0
    n = a[0]
    for i in range(1, c):
        if a[i] < n:
            m += n - a[i]
        else:
            n = a[i]

    return m

if __name__ == '__main__':
    c = int(input())
    a = list(map(int, input().split()))
    mm = main(c, a)
    print(mm)
