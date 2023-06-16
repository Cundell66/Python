numbers = [1, 3, 5]
# doubled =[]

# for num in numbers:
#   doubled.append(num * 2)

doubled = [x * 2 for x in numbers]

friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = []

for friend in friends:
    if friend.startswith('S'):
        starts_s.append(friend)

print(starts_s)

starts_s2 = [friend for friend in friends if friend.startswith('S')]

print(starts_s2)

print(starts_s is starts_s2)  # False

print(starts_s[0] is starts_s2[0])  # True
