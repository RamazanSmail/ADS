def simple_hash(string, base=256, prime=101):
    """Вычисляет хэш строки с использованием простого алгоритма."""
    hash_value = 0
    for char in string:
        hash_value = (hash_value * base + ord(char)) % prime
    return hash_value




def rabin_karp_hash(text, pattern, base=256, prime=101):
    """Ищет шаблон в тексте с использованием хэша Рабина-Карпа."""
    n = len(text)
    m = len(pattern)
    pattern_hash = simple_hash(pattern, base, prime)
    current_hash = simple_hash(text[:m], base, prime)

    for i in range(n - m + 1):
        # Проверяем хэш текущего окна
        if pattern_hash == current_hash:
            # Если хэши совпали, проверяем сами строки
            if text[i:i + m] == pattern:
                return i  # Возвращаем индекс совпадения

        # Пересчитываем хэш для следующего окна
        if i < n - m:
            current_hash = (
                base * (current_hash - ord(text[i]) * (base ** (m - 1))) + ord(text[i + m])
            ) % prime
            if current_hash < 0:
                current_hash += prime

    return -1  # Шаблон не найден

"""
Rabin-Karp Algorithm Explained
The Rabin-Karp algorithm is a string searching algorithm that efficiently finds a 
substring (pattern) in a larger string (text) using hashing. 
Instead of directly comparing strings, it compares their hash values, making it faster in many cases.

How the Algorithm Works
Hashing:

Compute a hash for the pattern 
�
P and the first window of text 

new_hash=(base⋅(old_hash−char_out⋅base 
m−1
 )+char_in)modprime
Best and Worst Cases
Best Case (
O(n+m)):
The hash function is well-designed, and there are few or no collisions.
The algorithm performs 
n−m+1 hash recalculations and only a few comparisons.
Worst Case (O(nm))
O(n⋅m)):
Many collisions occur (different substrings have the same hash value).
Each collision leads to a character-by-character comparison.
Example (Step-by-Step)
Text: "abracadabra"
Pattern: "cad"
Step 1: Compute the hash for "cad" (the pattern) and the first window "abr".
Step 2: The hashes don’t match — slide the window and recalculate the hash for "bra".
Step 3: The hashes match for "cad" — compare the strings character by character. A match is found!
Advantages:
Efficient for searching in large texts.
Can handle multiple patterns at once.
Disadvantages:
Performance depends on the quality of the hash function.
Hash collisions can lead to slower performance.
The Rabin-Karp algorithm works best when hash collisions are minimized, making it ideal for searching substrings in texts with minimal hash overlaps.
"""