def add(x, y):
    return x + y


result = add(x=5, y=8) # 13
print(result)


def divide(dividend, divisor):
    if divisor != 0:
        return(dividend / divisor)
    else:
        return "Can't divide by zero!"


# keyword arguments
result = divide(divisor=0, dividend=15)
print(result)
