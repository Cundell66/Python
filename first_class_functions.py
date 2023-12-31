def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Can't divide by zero")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)
