def fibonacci(num):
    first_num = 0
    second_num = 1
    count = 0
    while count <= int(num) -2:
        count += 1
        new_num = first_num + second_num
        first_num = second_num
        second_num = new_num
    return new_num
print(fibonacci(input('number please ')))