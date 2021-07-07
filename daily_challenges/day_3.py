def even_in_between(start, end):
    if start < end:
        i = int(start)
        result = []
        count = 0
        while i != end:
            i = list(str(i))
            for number in i:
                if int(number) % 2 == 0:
                    count += 1
                    if count == len(i):
                        result.append(int(''.join(i)))
                        count = 0
                else:
                    count = 0
            i = int(''.join(i))
            i += 1
        if len(result) >= 1:
            return result
        else:
            return 'no double evens'
    else:
        return 'make the first number smaller please'

print(even_in_between(int(input('start number please ')),int(input('end number please '))))