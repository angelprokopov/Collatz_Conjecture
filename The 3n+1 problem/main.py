def collatz_conjecture(n):
    while n != 1:
        print(n, end=', ')
        if n & 1:
            n = 3 * n + 1

        else:
            n = n // 2
    print(n)


collatz_conjecture(25000)
