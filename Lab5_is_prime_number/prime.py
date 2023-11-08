import random

def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True

def jacobi_symbol(a, n):
    if n % 2 == 0 or n <= 0:
        raise ValueError("n должно быть нечетным и положительным")
    a = a % n
    t = 1

    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t

        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t

        a = a % n

    if n == 1:
        return t
    else:
        return 0

def is_prime_solovay_strassen(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    def legendre(a, p):
        return pow(a, (p - 1) // 2, p)

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = legendre(a, n)
        y = jacobi_symbol(a, n)
        if x != y % n:
            return False

    return True

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    def miller_rabin_test(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True

        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True

        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin_test(a, s, d, n):
            return False

    return True


n = 23

print("тест Ферма: ")
if is_prime_fermat(n):
    print(f"{n} вероятно простое")
else:
    print(f"{n} составное")

b = 13
a = 6
symbol = jacobi_symbol(a, b)
print(f"Символ Якоби ({a}/{b}) = {symbol}")

print("тест соловэя-Штрассена: ")
if is_prime_solovay_strassen(n):
    print(f"{n} вероятно простое")
else:
    print(f"{n} составное")

print("тест Миллера-Рабина: ")
if is_prime_miller_rabin(n):
    print(f"{n} вероятно простое")
else:
    print(f"{n} составное")