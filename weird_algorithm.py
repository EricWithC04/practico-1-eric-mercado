def weird_algorithm(num):
    if type(num) == float or num < 1 or num > 1000000:
        return "Error, la entrada debe ser un natural menor de 1.000.000"

    list_complete = []

    while True:

        list_complete.append(num)
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1

        if list_complete[-1] == 1:
            return list_complete

numero = 6
print(weird_algorithm(numero))
assert weird_algorithm(numero) == [6, 3, 10, 5, 16, 8, 4, 2, 1], "Error, el resultado es distinto a lo esperado"