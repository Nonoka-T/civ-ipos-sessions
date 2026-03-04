def add(number1, number2):
    if not isinstance(number1, (int, float, complex)) or not isinstance(number2, (int, float, complex)):
        raise TypeError("Both number1 and number2 must be of type int or float of complex type")

    return number1 + number2
