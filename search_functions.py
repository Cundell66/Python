def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Rolf Smith", "age": 24},
    {"name": "Rolf Smith", "age": 24}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))
