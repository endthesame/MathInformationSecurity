def is_key(key):
    try:
        key = int(key)
        return key
    except ValueError:
        print("key is not int")
        raise ValueError
    
def is_correct_pswd(password):
    for letter in password:
        if letter not in alphabet:
            print("Incorrect password")
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
#INDENT = 1 # т.к отсчет по буквам начинают не с 0, а обращаться по индексам буду именно с помощью переменной key, то к ключу будет добавлен отступ
key = input("key: ")
key = is_key(key=key)
password = input("Password: ").lower()
is_correct_pswd(password=password)
uniquePassLetters = unique_letters(password=password)
codeAlphabet = create_code_alpabet(alphabet=alphabet, uniquePassLetters=uniquePassLetters, key=key)

print(alphabet)
print(codeAlphabet)

wordToCode = input("input word to code: ")
codeWord = word_to_code(word=wordToCode, alphabet=alphabet, codeAlphabet=codeAlphabet)
print("new coded word: " + codeWord)


    



