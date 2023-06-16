greeting = 'Hello'

name = input('What is your name?')

def with_name(name):
    result = f'{greeting}, {name}'
    return result

print(with_name(name))

size_input = input('How big is your house in (in square feet)?')

square_feet = int(size_input)
square_metres = (square_feet  / 10.8)

print(f'{square_feet} square feet is {square_metres:.2f} square metres')
