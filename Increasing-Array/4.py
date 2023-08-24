def main():
    c = int(input())
    a = list(map(int, input().split()))

    m = 0
    n = a[0]

    for i in range(1, c):
        if a[i] < n:
            m += n - a[i]
        else:
            n = a[i]

    print(m)

main()
