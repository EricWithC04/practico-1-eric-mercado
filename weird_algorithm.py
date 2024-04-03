def weird_algorithm(num):
    if type(num) == float or num < 1 or num > 1000000:
        return "Error, la entrada debe ser un natural menor de 1.000.000"

    list_complete = []

    # Bucle que se repetirá de forma indefinida y que se detendra al retornar el resultado final
    while True:

        list_complete.append(num)
        
        # Evaluamos si el numero es par, si lo es lo dividimos a la mitad, caso contrario se multiplica por 3 y se le suma 1
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1

        # Cuando el ultimo valor de la lista sea 1, retornamos la lista y se termina el bucle.
        if list_complete[-1] == 1:
            return list_complete

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"