def generate_gamma(gamma, message):
    for i in range(len(message)):
        yield gamma[i % len(gamma)], message[i]

def encrypt(gamma, message):
    encrypted_message = ""
    for g, m in generate_gamma(gamma, message):
        encrypted_message += alph[(alph.index(m) + alph.index(g) + 1) % len(alph)]
    return encrypted_message

def decrypt(gamma, encrypted_message):
    decrypted_message = ""
    for g, m in generate_gamma(gamma, encrypted_message):
        decrypted_message += alph[(alph.index(m) - alph.index(g) - 1) % len(alph)]
    return decrypted_message

alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
gamma = "гамма"
message = "приказ"

encrypted_message = encrypt(gamma, message)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt(gamma, encrypted_message)
print(f"Decrypted message: {decrypted_message}")