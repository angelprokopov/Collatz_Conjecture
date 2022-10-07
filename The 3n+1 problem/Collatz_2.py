def collatz(n):
    if n % 2 == 0:
        n = n // 2
        print(n)
        return n
    elif n % 2 == 1:
        n = 3 * n + 1
        print(n)
        return n


print('Enter an integer:')
n = int(input())
while n > 1:
    n = collatz(n)
