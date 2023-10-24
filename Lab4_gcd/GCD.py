def euclidean_gcd(a, b):
    r0, r1, i = a, b, 1
    while True:
        ri_next = r0 % r1
        if ri_next == 0:
            d = r1
            return d
        r0, r1, i = r1, ri_next, i + 1

def binary_gcd(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a, b, g = a // 2, b // 2, 2 * g

    u, v = a, b
    while u != 0:
        while u % 2 == 0:
            u //= 2
        while v % 2 == 0:
            v //= 2
        if u >= v:
            u -= v
        else:
            v -= u
    return g * v

def extended_gcd(a, b):
    r0, r1, x0, x1, y0, y1, i = a, b, 1, 0, 0, 1, 1
    while True:
        q, ri_next = divmod(r0, r1)
        if ri_next == 0:
            return r1, x1, y1
        x_next = x0 - q * x1
        y_next = y0 - q * y1
        r0, r1, x0, x1, y0, y1, i = r1, ri_next, x1, x_next, y1, y_next, i + 1

def extended_binary_gcd(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a, b, g = a // 2, b // 2, 2 * g

    u, v, A, B, C, D = a, b, 1, 0, 0, 1
    while u != 0:
        while u % 2 == 0:
            u //= 2
            if A % 2 == 0 and B % 2 == 0:
                A, B = A // 2, B // 2
            else:
                A, B = (A + b) // 2, (B - a) // 2

        while v % 2 == 0:
            v //= 2
            if C % 2 == 0 and D % 2 == 0:
                C, D = C // 2, D // 2
            else:
                C, D = (C + b) // 2, (D - a) // 2

        if u >= v:
            u, A, B = u - v, A - C, B - D
        else:
            v, C, D = v - u, C - A, D - B

    return g * v, C, D

import math

a, b = 56, 98

print("Using Euclidean Algorithm:", euclidean_gcd(a, b))
print("Using Binary Euclidean Algorithm:", binary_gcd(a, b))
print("Using Extended Euclidean Algorithm:", extended_gcd(a, b)[0])  # Just the gcd, not x and y
print("Using Extended Binary Euclidean Algorithm:", extended_binary_gcd(a, b)[0])  # Just the gcd, not x and y
print("Using Python's built-in math.gcd:", math.gcd(a, b))
