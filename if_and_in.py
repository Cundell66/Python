movies_watched = {'The Matrix', 'Green Book', 'Hex'}
user_movie = input("Enter something you've watch recently... ")

if user_movie in movies_watched:
    print(f'Yes, I have watched {user_movie}')
else:
    print('Not seen that yet!')
    