print()

print('Please enter the following information:')

print()

fname = input('First name: ')
lname = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
hair = input('Hair color: ')
eyes = input('Eye color: ')
start_month = input('Start month: ')
training = input('Completed advanced training (Yes/No)? ')

print()

print('The ID card is:')
print('--------------------------------------------------')
print(f'{lname.upper()}, {fname.capitalize()}')
print(job_title.title())
print(f'ID: {id_number}')

print()

print(email.lower())
print(phone)

print()

print(f'Hair: {hair.capitalize():25}Eyes: {eyes.capitalize()}')
print(f'Month: {start_month.capitalize():24}Training: {training.capitalize()}')
print('--------------------------------------------------')

print()