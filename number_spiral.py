def number_spiral(positionX, positionY):
    spiral_matrix = []

    num_col_rows = 0

    # Identificamos cual de las coordenadas en más grande para saber la cantidad maxima de filas y columnas que deberá tener la matriz
    if positionX > positionY:
        num = positionX**2
        num_col_rows = positionX
    else:
        num = positionY**2
        num_col_rows = positionY
    
    # Creamos la matriz con los valores inicializados en 0
    for i in range(num_col_rows):
        spiral_matrix.append([])
        for j in range(num_col_rows):
            spiral_matrix[i].append(0)

    # Ultimos valores de las posiciones X e Y
    lastX = 0
    lastY = 0

    # Cada vez que se complete un area de n * n, max_number se incrementara para indicar que hay que pasar a la siguiente capa de la matriz
    max_number = 1

    # Indicamos si se está incrementando o decrementando, lo mismo si se está moviendo en X o en Y
    decrement = False
    decrementX = False

    for i in range(num):
        # En cada iteración agregamos el valor actual a su posicion correspondiente
        spiral_matrix[lastX][lastY] = i + 1

        # Alteramos uno de los valores que tenemos dependiendo de distintas condiciones

        # La primera condición se cumplirá solamente en la primera iteración, después solamente uno de los valores podrá ser 0
        if lastX == 0 and lastY == 0:
            lastY += 1
        # Si ambos llegaron a la posicion maxima en esta capa, alternamos el sentido en el que se agregan los valores
        elif lastY == lastX and lastX == max_number:
            decrement = True
            if decrementX:
                lastX -= 1
                # En el caso de que X llegue a 0, se alterna el valor para que la proxima vez sea Y la que empiece a decrementar
                if lastX == 0:
                    decrementX = not decrementX
            else:
                lastY -= 1
        # Si la secuencia estaba en orden decreciente y se llega al 0, aumentamos en 1 el valor de la coordenada contraria y empezamos a incrementar el valor
        elif (lastX == 0 or lastY == 0) and decrement:
            if lastX < lastY:
                lastY += 1
            else:
                lastX += 1
            decrement = False
            max_number += 1
        # Si la secuencia estaba en orden creciente y se llega a la posicion maxima, alternamos a orden decreciente
        elif (lastX == max_number or lastY == max_number) and not decrement:
            if lastX < lastY:
                lastX += 1
            else:
                lastY += 1
                if lastY == max_number:
                    decrementX = not decrementX
        # Si la secuencia está en orden decreciente, reducimos la X o la Y dependiendo de cual corresponda
        elif decrement and decrementX:
            lastX -= 1
            # En el caso de que X llegue a 0, se alterna el valor para que la proxima vez sea Y la que empiece a incrementar
            if lastX == 0:
                decrementX = not decrementX
        elif decrement and not decrementX:
            lastY -= 1
    
    # Retornamos el valor que está en las coordenadas indicadas, a estas se les resta 1 por que las lista empiezan en 0
    return spiral_matrix[positionY - 1][positionX - 1]

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"