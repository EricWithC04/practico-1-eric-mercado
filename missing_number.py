def missing_number(num, incomplete_list):
    if type(num) == float or num < 1:
        return "Error, la entrada debe ser un natural"
    
    complete_list = range(num)
    missing_numbers = []

    # Recorremos una lista completa y guardamos todos los valores que no aparezcan en la lista pasada por parametros
    for i in complete_list:
        if i + 1 not in incomplete_list:
            missing_numbers.append(i + 1)

    # En el caso de que solamente falte un numero, devolvemos ese numero, si hay más de uno, devolvemos una lista con todos los numeros faltantes
    if len(missing_numbers) == 1:
        return missing_numbers[0]
    else:
        return missing_numbers

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print("Todos los test pasaron correctamente")