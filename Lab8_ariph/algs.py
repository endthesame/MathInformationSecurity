def add_non_negative_numbers(u, v, base):
    n = max(len(u), len(v))
    u = [int(digit) for digit in u.zfill(n)][::-1]  # Преобразуем строку в список цифр, выравниваем по длине и разворачиваем
    v = [int(digit) for digit in v.zfill(n)][::-1]

    result = [0] * n
    carry = 0

    for j in range(n):
        Wj = u[j] + v[j] + carry
        result[j] = Wj % base
        carry = Wj // base

    return ''.join(map(str, result[::-1]))

def subtract_non_negative_numbers(u, v, base):
    n = max(len(u), len(v))
    u = [int(digit) for digit in u.zfill(n)][::-1]  # Преобразуем строку в список цифр, выравниваем по длине и разворачиваем
    v = [int(digit) for digit in v.zfill(n)][::-1]

    result = [0] * n
    borrow = 0

    for j in range(n):
        Wj = u[j] - v[j] - borrow
        if Wj < 0:
            Wj += base
            borrow = 1
        else:
            borrow = 0
        result[j] = Wj

    return ''.join(map(str, result[::-1]))

def multiply_non_negative_numbers(u, v):
    len_u, len_v = len(u), len(v)
    result = [0] * (len_u + len_v)

    for i in range(len_u - 1, -1, -1):
        carry = 0
        for j in range(len_v - 1, -1, -1):
            temp = int(u[i]) * int(v[j]) + carry + result[i + j + 1]
            result[i + j + 1] = temp % 10
            carry = temp // 10
        result[i] += carry

    result_str = ''.join(map(str, result))
    return result_str.lstrip('0') or '0'

def divide_large_numbers(dividend, divisor):
    # Преобразование строк в списки цифр
    dividend = [int(digit) for digit in str(dividend)]
    divisor = [int(digit) for digit in str(divisor)]

    quotient = []  # Частное
    remainder = 0  # Остаток

    for digit in dividend:
        current_dividend = remainder * 10 + digit
        current_quotient = current_dividend // divisor[0]
        remainder = current_dividend % divisor[0]
        quotient.append(current_quotient)

    # Проход по остальным разрядам
    for i in range(len(dividend) - len(divisor) + 1):
        current_quotient = quotient[i]
        current_remainder = remainder
        j = 1

        while j < len(divisor) and j + i < len(dividend):
            current_dividend = current_remainder * 10 + dividend[i + j]
            current_quotient = current_dividend // divisor[j]
            current_remainder = current_dividend % divisor[j]
            j += 1

        quotient[i] = current_quotient
        remainder = current_remainder

    # Приведение к строке
    quotient_str = ''.join(map(str, quotient)).lstrip('0') or '0'
    remainder_str = str(remainder)

    return quotient_str, remainder_str

# Пример использования
u = input("Введите первое неотрицательное число: ")
v = input("Введите второе неотрицательное число: ")
base = int(input("Введите основание системы счисления: "))

result = add_non_negative_numbers(u, v, base)
result_sub = subtract_non_negative_numbers(u, v, base)
print(f"Сумма чисел {u} и {v} в системе счисления с основанием {base} равна {result}")
print(f"Разность чисел {u} и {v} в системе счисления с основанием {base} равна {result_sub}")
print(f"Произведение чисел {u} и {v} в системе счисления с основанием {base} равно {multiply_non_negative_numbers(u, v)}")
print(f"Частное и остаток от деления чисел {u} и {v} в системе счисления с основанием {base} равны {divide_large_numbers(u, v)}")
##############################################################################################################

