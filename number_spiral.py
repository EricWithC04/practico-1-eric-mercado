from math import sqrt, ceil

def number_spiral(num):
    spiral_matrix = []
    num_col_rows = ceil(sqrt(num))
    
    for i in range(num_col_rows):
        spiral_matrix.append([])
        for j in range(num_col_rows):
            spiral_matrix[i].append(0)

    lastX = 0
    lastY = 0
    max_number = 1
    decrement = False
    decrementX = False

    for i in range(num):
        spiral_matrix[lastX][lastY] = i + 1

        if lastX == 0 and lastY == 0:
            lastY += 1
        elif lastY == lastX and lastX == max_number:
            decrement = True
            if decrementX:
                lastX -= 1
                if lastX == 0:
                    decrementX = not decrementX
            else:
                lastY -= 1
        elif (lastX == 0 or lastY == 0) and decrement:
            if lastX < lastY:
                lastY += 1
            else:
                lastX += 1
            decrement = False
            max_number += 1
        elif (lastX == max_number or lastY == max_number) and not decrement:
            if lastX < lastY:
                lastX += 1
            else:
                lastY += 1
                if lastY == max_number:
                    decrementX = not decrementX
        elif decrement and decrementX:
            lastX -= 1
            if lastX == 0:
                decrementX = not decrementX
        elif decrement and not decrementX:
            lastY -= 1
    
    
    for i in spiral_matrix:
        print(i)
    return 0

assert number_spiral(36) == 0, "Error, el resultado es distinto a lo esperado"