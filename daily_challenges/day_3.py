def even_in_between(start, end):
    if start < end:
        result = []
        count = 0
        for num in range (int(start),int(end)+1):
            num = list(str(num))
            for number in num:
                if int(number) % 2 == 0:
                    count += 1
                    if count == len(num):
                        result.append(''.join(num))
                        count = 0
                else:
                    count = 0
        if len(result) >= 1:
            return ', '.join(result)
        else:
            return 'no double evens'
    else:
        return 'make the first number smaller please'

print(even_in_between(int(input('start number please ')),int(input('end number please '))))