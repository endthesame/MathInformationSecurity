import math
import re

def is_pass_valid(password, columns):
    if len(password) != columns:
        print("pass len should be equal to row len")
        raise ValueError
    alphabeticValues = re.findall(r'[a-zA-Zа-яА-Я]', password)
    if len(alphabeticValues) != len(password):
        print("pass should contain only eng and ru letters")
        raise ValueError
    
def is_len_columns_valid(columns, inputString):
    if columns > len(inputString):
        print("len columns should be <= len of Input String")
        raise ValueError
    if columns <= 1:
        raise ValueError
    
def to_dict(inputString, password, columns, row):
    list_of_slices = []
    for i in range(row):
        list_of_slices.append(inputString[columns*i:columns*(i+1)])

    while len(list_of_slices[-1]) != columns:
        list_of_slices[-1]+= 'a'

    routeDict = {}

    for i in range(columns):
        stringToAppend = ""
        for j in range(row):
            stringToAppend += list_of_slices[j][i]
        routeDict[password[i]] = stringToAppend

    sorted_dict = dict(sorted(routeDict.items()))

    return sorted_dict


inputedString = input("Input string to encrypt: ")
columns = int(input("Input int value to determine the number columns: "))
password = input("Password: ").lower()

inputString = inputedString.replace(" ", "") # remove spaces
password = password.replace(" ", "") # remove spaces
password = ''.join([password[i] for i in range(len(password)-1) if password[i+1]!= password[i]]+[password[-1]]) #remove dublicates
is_len_columns_valid(columns, inputString)
is_pass_valid(password, columns)
row = math.ceil(len(inputString) / int(columns))

routeDict = to_dict(inputString, password, columns, row)

cryptogram = ""
for key in routeDict:
    cryptogram += routeDict[key]

print("начальная фраза: ", inputedString)
print("криптограмма: ", cryptogram)