print()

can_ride = False

first_age = int(input('What is the age of the first rider? '))
first_height = float(input('What is the height of the first rider? '))

second_rider = input('Is there a second (yes/no)? ')

if second_rider.lower() == 'yes':
    second_age = int(input('What is the age of the second rider? '))
    second_height = float(input('What is the height of the second rider? '))

    if first_height >= 36 and second_height >= 36:
        
        if first_age >= 18 or second_age >= 18:
            can_ride = True

else:

    if first_age >= 18 and first_height >= 62:
        can_ride = True

if can_ride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')

print()
