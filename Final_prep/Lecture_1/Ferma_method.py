import math

def fermat_factorization(n):
    """
    Метод Ферма для факторизации числа.
    
    :param n: число для факторизации
    :return: пара множителей (a - b, a + b)
    """
    if n % 2 == 0:
        return 2, n // 2  # Если число четное, сразу возвращаем (2, n / 2)
    
    # Начальное значение a
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n  # b^2 = a^2 - n

    while not is_perfect_square(b2):
        a += 1
        b2 = a * a - n

    # Найдено b
    b = int(math.sqrt(b2))
    return a - b, a + b

def is_perfect_square(x):
    """
    Проверяет, является ли число точным квадратом.
    """
    s = int(math.sqrt(x))
    return s * s == x

# Пример использования
n = 5959
factor1, factor2 = fermat_factorization(n)
print(f"Множители числа {n}: {factor1}, {factor2}")
