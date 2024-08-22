print()

friend_name = ""
friends = []

while friend_name.lower() != "end":

    friend_name = input("Type the name of a friend: ")

    if friend_name.lower() != "end":
        friends.append(friend_name)

print("\nYour friends are:")

for friend in friends:
    print(friend)

print()
