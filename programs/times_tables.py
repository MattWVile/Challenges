def times_table(num):
    total_count = 1
    while total_count <= int(num):
        result = []
        nested_count = 1
        while nested_count <= int(num):
            result.append(total_count * nested_count)
            nested_count += 1
        if total_count == int(num):
            return result
        else:
            print(result)
            total_count += 1
if __name__ == "__main__":
    print(times_table(input('number please ')))