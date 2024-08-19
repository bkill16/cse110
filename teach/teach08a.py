word = "Commitment"
favorite_letter = input("\nWhat is your favorite letter? ")

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")