# procedural_examples.py
# Примеры в процедурном стиле:
# Проверка простого числа, поиск дубликатов, генерация простых чисел с помощью решета Эратосфена.

def is_prime(n):
    """Проверяет, является ли n простым числом."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n):
    """Возвращает первое простое число после n."""
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

def find_duplicates(seq):
    """Находит дубликаты в списке (элемент: количество повторов)."""
    counts = {}
    for x in seq:
        counts[x] = counts.get(x, 0) + 1
    return {k: v for k, v in counts.items() if v > 1}

def sieve(n):
    """Решето Эратосфена — возвращает список простых чисел меньше n."""
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    p = 2
    while p * p < n:
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False
        p += 1
    return [i for i, is_p in enumerate(sieve) if is_p]

# Примеры работы
if __name__ == '__main__':
    print('is_prime(17) =>', is_prime(19))
    print('is_prime(18) =>', is_prime(20))
    print('next_prime(17) =>', next_prime(17))
    print('sieve(30) =>', sieve(30))
    print('find_duplicates([1,2,2,3,4,5,4]) =>', find_duplicates([1,2,2,3,4,5,4]))
