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

super_prime = []

for i in range(1, len(primes) + 1): 
    if i in primes: #если i входит в простые числа мы его добавляем в новый список с супер простыми числами
        super_prime.append(primes[i-1]) #добавляем число под номером i-1, тоесть если 2 то мы добавяем число под индексом 1 это 3

print(super_prime[n-1])



