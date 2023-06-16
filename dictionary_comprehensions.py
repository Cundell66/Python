users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'bob123'),
    (2, 'Jose', 'long4assword'),
    (3, 'username', '1234')
]

username_mapping = {user[1]: user for user in users}

print(username_mapping['Bob'])

username_input = input('Enter Your Username: ')
password_input = input('and your password: ')

_, username, password = username_mapping[username_input]

if password_input == password:
    print('Your details are correct!')
else:
    print('Your details are incorrect')
