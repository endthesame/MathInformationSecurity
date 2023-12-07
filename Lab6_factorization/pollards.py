def pollards_rho(n, c, f):
    a = b = c

    def rho(x):
        return f(x) % n

    while True:
        a = rho(a)
        b = rho(rho(b))
        d = gcd(abs(a - b), n)

        if 1 < d < n:
            return d
        elif d == n:
            return "Делитель не найден"

# Функция для нахождения наибольшего общего делителя (НОД)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Пример использования
N = 1359331
c = 1
f = lambda x: (x**2 + 5) % N

result = pollards_rho(N, c, f)
print("Ответ:", result)