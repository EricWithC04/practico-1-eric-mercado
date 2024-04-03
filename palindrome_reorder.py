def palindrome_reorder(string):
    number_impar = 1

    # Dependiendo si la cantidad de caracteres es par o impar, podremos tener un maximo de 1 cantidad impar o ninguna
    if len(string) % 2 == 0:
        number_impar = 0
    
    counter = {}

    palindrome_left = ""
    palindrome_right = ""
    palindrome_center = ""
    
    # Contamos la cantidad de veces que se repite cada caracter
    for c in string:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    # Indentificamos si cada caracter se repite una cantidad par de veces
    for i in counter:
        if counter[i] % 2 > 0:
            number_impar -= 1

    # Identificamos que caracter se repite una cantidad impar de veces y lo guardamos para el centro
    for c in counter:
        if counter[c] % 2 == 1:
            palindrome_center = c
    
    # Empezamos con el string de la izquierda, colocamos cada caracter la mitad de veces que se repite, la otra mitad será para el string de la derecha
    for c, count in counter.items():
        for i in range(count // 2):
            palindrome_left += c

    # El string de la derecha es el mismo que el de la izquierda pero dado vuelta
    palindrome_right = palindrome_left[::-1]

    # En el caso de haber más impares de los posibles retornamos el mensaje "NO SOLUTION"
    if number_impar < 0:
        return "NO SOLUTION"
    # Caso contrario unimos la izquierda, centro y derecha y retornamos
    else:
        return palindrome_left + palindrome_center + palindrome_right

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"