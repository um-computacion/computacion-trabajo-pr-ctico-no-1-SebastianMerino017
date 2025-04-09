def decimal_to_roman(decimal):
    if not isinstance(decimal, int):
        raise TypeError("Input must be an integer")
    
    if decimal < 1 or decimal > 3999:
        raise ValueError("Input must be between 1 and 3999")
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    for i in range(len(values)):
        while decimal >= values[i]:
            result += symbols[i]
            decimal -= values[i]
    
    return result

# print(decimal_to_roman(17)) 