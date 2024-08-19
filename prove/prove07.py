print("\nWelcome to the word guessing game!")

word = "house"
guess = ""
guess_count = 0
initial_hint = ""

for i in range(len(word)):
    initial_hint += "_"

print("Your hint is:", initial_hint)

while word != guess:

    hint = ""
    guess = input("What is your guess? ")

    guess_count += 1

    if len(word) == len(guess):

        for i in range(len(word)):
            
            if word[i] == guess[i].lower():
                hint += guess[i].upper()
            elif guess[i].lower() in word:
                hint += guess[i].lower()
            else:
                hint += "_"
    
        print(f"\nYour hint is: {hint}")

    else:
        print("Sorry, the guess must have the same number of letters as the secret word.\n")            
            

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.\n")