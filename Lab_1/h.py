import math
n = int(input())
f = True

for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        f = False

if f and n != 1:
    print('YES')
else:
    print('NO')