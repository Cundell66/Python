x = (5, 11) # tuple
x = 5, 11 # also a tuple
x, y = 5, 11

t = 5, 11
x, y = t

student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}
for t  in student_attendance.items():
    student, attendance = t
    print(f'{student}: {attendance}')

people = [('Bob', 42, 'Mechanic'), ('James', 24, 'Artist'), ('Harry', 32, 'Lecturer')]

for name, age, profession in people:
    print(f'Name: {name}, Age: {age}, Profession: {profession}')
    

person = ('Bob', 42, 'Mechanic')
name, _, profession = person


head, *tail = [1, 2, 3, 4, 5] # splits off 1 from 2,3,4,5


