import numpy as np

def generate_grid(k):
    grid = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            grid[i][j] = i * k + j + 1
    return grid

def encrypt_with_grid(grid, text):
    k = len(grid)
    encrypted = np.chararray((2*k, 2*k), unicode=True)
    encrypted[:] = ''

    idx = 0
    for _ in range(4):
        for i in range(k):
            for j in range(k):
                if grid[i][j] and idx < len(text):
                    encrypted[i][j] = text[idx]
                    idx += 1

        grid = np.rot90(grid)

    return encrypted

def extract_by_password(grid, password):
    order = sorted(range(len(password)), key=lambda x: password[x])
    return ''.join([''.join(grid[:, i]) for i in order])

def encrypt(text, password):
    k = int(len(text)**0.5)
    if k*k != len(text):
        raise ValueError("Length of the text should be a perfect square.")

    if len(password) != k:
        raise ValueError(f"Length of the password should be {k}.")

    grid = generate_grid(k)
    encrypted_grid = encrypt_with_grid(grid, text)
    result = extract_by_password(encrypted_grid, password)

    return result

# Пример использования
text = "нужноподписатьновыйуказда"
password = "шифрр"
print(encrypt(text, password))
