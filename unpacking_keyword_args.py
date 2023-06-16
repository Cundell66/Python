def named(**kwargs):
    print(kwargs)

named(name='bob', age=25)

def named2(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
named2(**details)

def named3(**kwargs):
    print(kwargs)

details = {"name": "Bob", "age": 25}
named3(**details)

def named4(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')

print_nicely(name='Bob', age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name='Bob', age=25)


"""
def post(url, data=None, json=None, **kwrgs):
    return request('post', url, data=data. json=json, **kwargs)
"""

def myfunction(**kwargs):
    print(kwargs)

myfunction(**"Bob") # Error, must be mapping
myfunction(**None) # Error, not a dictionary
