userisbn = input('enter isbn number please')
testisbn = '978-0-306-40615'
nolines = ''.join(userisbn.split('-'))
index = 0
total = 0
for num in nolines:
    if index % 2 == 0:
        total += int(num)
    else:
        total += int(num) * 3
    index += 1
check_digit = 10 - total % 10
print(userisbn + '-' + str(check_digit))
