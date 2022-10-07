import time

start = time.time()
# cache the values
cache = {n: 0 for n in range(1, 1000000)}
# initiate the values
cache[1] = 1
cache[2] = 2
# looping through the numbers
for n in range(3, 1000000):
    counter = 0
    current = n
    while n > 1:
        if n < current:
            cache[current] = cache[n] + counter
            break
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1

print(list(cache.values()).index(max(cache.values())) + 1)
print(time.time() - start)
