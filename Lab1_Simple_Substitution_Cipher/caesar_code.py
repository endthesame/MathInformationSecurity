def is_key(key):
    try:
        key = int(key)
        if key > len(alphabet):
            key %= len(alphabet)
        return key
    except ValueError:
        print("key is not int")
        raise ValueError
    
def is_correct_input_word_value(word, alphabet):
    for letter in word:
        if letter not in alphabet:
            print("Incorrect input word value")
            raise ValueError
        
def unique_letters(password):
    unique = []
    for letter in password:
        if letter not in unique:
            unique.append(letter)
    return unique

def create_code_alpabet(alphabet, uniquePassLetters, key):
    codeAlphabet = []
    alphabet_without_upl = []
    for letter in alphabet:
        if letter not in uniquePassLetters:
            alphabet_without_upl.append(letter)

    codeAlphabet = alphabet_without_upl[-key:]
    codeAlphabet += uniquePassLetters
    codeAlphabet += alphabet_without_upl[:-key]
    return codeAlphabet

def word_to_code(word, alphabet, codeAlphabet):
    codeWord = ""
    for letter in word:
        for i in range(len(alphabet)):
            if alphabet[i] == letter:
                codeWord += codeAlphabet[i]
                break
    return codeWord

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
key = input("key: ")
key = is_key(key=key)
password = input("Password: ").lower()
is_correct_input_word_value(word=password, alphabet=alphabet)
uniquePassLetters = unique_letters(password=password)
codeAlphabet = create_code_alpabet(alphabet=alphabet, uniquePassLetters=uniquePassLetters, key=key)

print(alphabet)
print(codeAlphabet)

wordToCode = input("input word to code: ")
is_correct_input_word_value(wordToCode, alphabet)
codeWord = word_to_code(word=wordToCode, alphabet=alphabet, codeAlphabet=codeAlphabet)
print("new coded word: " + codeWord)