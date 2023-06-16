def add(x, y):
    result = x + y + z 
    print(result)


z = 6

add(3, 5)


def say_hello(name):
    print(f'Hello,  {name}')

say_hello('Bob')


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("Can't divide by zero!")

# keyword arguments
divide(divisor=3, dividend=15)
