def are_letters_from_alphabet(password):
    for letter in password:
        if letter not in alphabet:
            print("Incorrect input value")
            raise ValueError

def atbash_reverse(alphabet):
    return alphabet[::-1]

def word_to_code(word, alphabet, codeAlphabet):
    codeWord = ""
    for letter in word:
        for i in range(len(alphabet)):
            if alphabet[i] == letter:
                codeWord += codeAlphabet[i]
                break
    return codeWord

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 
            'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
atbashAlphabet = atbash_reverse(alphabet=alphabet)

print(alphabet, "\n", atbashAlphabet)

wordToCode = input("input word to code: ")
are_letters_from_alphabet(wordToCode)

codedword = word_to_code(word=wordToCode, alphabet=alphabet, codeAlphabet=atbashAlphabet)
print("coded word: " + codedword)


