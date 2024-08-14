import random

play_again = ''

while play_again.lower() != 'no':

    number = random.randint(1, 100)
    guess = int(input('\nWhat is your guess? '))
    guess_count = 1

    while guess != number:

        if guess < number:
            print('Higher')
        else:
            print('Lower')

        guess_count += 1

        guess = int(input('What is your guess? '))

    print('You guessed it!')
    print(f'It took you {guess_count} guesses.\n')

    play_again = input('Would you like to play again (yes/no)? ')

print('\nThanks for playing! Goodbye.\n')