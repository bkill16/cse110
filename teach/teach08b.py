print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

play_again = "yes"

while play_again.lower() == "yes":

    n = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        if i % n == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")

    print()

    play_again = input("Would you like to play again? ")

print("\nThank you. Goodbye.\n")