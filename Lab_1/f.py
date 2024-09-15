n = int(input())
non_primes = []
for i in range(7920):
    non_primes.append(i)
i = 2
non_primes[1] = 0

while i <= 7919:
    if non_primes[i] != 0:
        j = i + i
        while j <= 7919:
            non_primes[j] = 0

            j = j + i
    i += 1

primes = []
for i in non_primes:
    if non_primes[i] != 0:
        primes.append(i)
print(primes[n-1])
