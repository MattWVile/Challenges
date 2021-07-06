firststring = input('first string please ')
secondstring = input('second string please ')
liststring = list(firststring)
for index, letter in enumerate (liststring):
    print(letter)
    print(index)
    // remove index, turn to string, compare against secondstring