import math
import random

def pollards_rho(n):
    """Метод Полларда rho для нахождения нетривиального делителя числа."""
    if n % 2 == 0:
        return 2
    
    # Начальные параметры
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1

    # Пока делитель не найден
    while g == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        g = math.gcd(abs(x - y), n)
    
    return g if g != n else None

# Пример использования
n = 8051
factor = pollards_rho(n)
print(f"Найденный делитель числа {n}: {factor}")
