def vigenere_encrypt(text, key):
    alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = ''
    
    #размерность пароля = размерности текста
    key_expanded = ''
    while len(key_expanded) < len(text):
        key_expanded += key
    key_expanded = key_expanded[:len(text)] 
    
    #сравниваем по таблице и получаем на пересечении букву
    for t, k in zip(text, key_expanded):
        if t in alph:
            new_pos = (alph.index(t) + alph.index(k)) % len(alph)
            encrypted_text += alph[new_pos]
        else:
            encrypted_text += t

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    decrypted_text = ''

    key_expanded = ''
    while len(key_expanded) < len(encrypted_text):
        key_expanded += key
    key_expanded = key_expanded[:len(encrypted_text)]

    for e, k in zip(encrypted_text, key_expanded):
        if e in alph:
            new_pos = (alph.index(e) - alph.index(k)) % len(alph)
            decrypted_text += alph[new_pos]
        else:
            decrypted_text += e

    return decrypted_text

# Пример использования
text = "криптографиясерьезнаянаука"
password = "математика"
encrypted_text = vigenere_encrypt(text, password)
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {vigenere_decrypt(encrypted_text, password)}")
