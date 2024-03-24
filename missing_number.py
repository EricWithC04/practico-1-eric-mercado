def missing_number(num, incomplete_list):
    if type(num) == float or num < 1:
        return "Error, la entrada debe ser un natural"
    
    complete_list = range(num)
    missing_numbers = []

    for i in complete_list:
        if i + 1 not in incomplete_list:
            missing_numbers.append(i + 1)

    if len(missing_numbers) == 1:
        return missing_numbers[0]
    else:
        return missing_numbers

print(missing_number(6, [1, 2, 4, 5, 6]))
assert missing_number(6, [1, 2, 4, 5, 6]) == 3, "Error, el resultado es diferente"