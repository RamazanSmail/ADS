def sieve_of_eratosthenes(n):
    """
    Находит все простые числа до числа n включительно.

    :param n: верхняя граница диапазона
    :return: список простых чисел
    """
    if n < 2:
        return []

    # Создаем булевый список, где True означает, что число потенциально простое
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми числами

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Помечаем все кратные i как составные (непростые)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Возвращаем список чисел, которые остались простыми
    return [i for i, prime in enumerate(is_prime) if prime]


n = 50
primes = sieve_of_eratosthenes(n)
print(f"Простые числа до {n}: {primes}")