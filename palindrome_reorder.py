def palindrome_reorder(string):
    number_impar = 1

    if len(string) % 2 == 0:
        number_impar = 0
    
    counter = {}

    palindrome_left = ""
    palindrome_right = ""
    palindrome_center = ""
    
    for c in string:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for i in counter:
        if counter[i] % 2 > 0:
            number_impar -= 1

    for c in counter:
        if counter[c] % 2 == 1:
            palindrome_center = c
    
    for c, count in counter.items():
        for i in range(count // 2):
            palindrome_left += c

    palindrome_right = palindrome_left[::-1]

    if number_impar < 0:
        return "NO SOLUTION"
    else:
        return palindrome_left + palindrome_center + palindrome_right

print(palindrome_reorder("nnnneeuuq"))