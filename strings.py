name = "Bob"
greeting = "Hello"

def with_name(name):
    result = f'{greeting}, {name}'
    return result

print(with_name(name))

name = 'Rolf'

print(with_name(name))
