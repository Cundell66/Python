number = 7

while True:
    user_input = input("Do you want to play? (Y/n).... ").lower()
    if user_input == "n":
        break
    user_number = int(input("Guess the mystery number: "))
    if number == user_number:
        print(f'correct, it was {number}')
    elif number - user_number in (1, -1):
        print('You were off my one')
    else:
        print(f'sorry, it was {number}')
