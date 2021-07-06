def near(first_string, second_string):
    liststring = list(first_string)
    i = 0
    for index, letter in enumerate (liststring):
        new_list = liststring[:index] + liststring[index+1 : ]
        i += 1
        if new_list == list(second_string):
            return True
        elif i == len(first_string):
            return False
print(near(input('first string please '),input('second string please ')))