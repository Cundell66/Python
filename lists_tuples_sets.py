my_list = ['Bob', 'Rolf', 'Anne']
my_tuple = ('Bob', 'Rolf', 'Anne')
my_sets = {'Bob', 'Rolf', 'Anne'}

print(my_list[0])
print(my_tuple[1])
''' print(my_sets[2]) doesn't work because sets don't maintain their order'''

my_list[0] = 'Pete'
print(my_list)
my_list.append('Bob')
print(my_list)
# tuples are immutable and can't be changed or added to
reversed_list = my_list[::-1]
print(reversed_list)

my_list.remove('Pete')
print(my_list)

print()
print(my_sets)
my_sets.add('Peter')
print(my_sets)
