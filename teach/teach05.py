print()

letter = ''
sign = ''

grade_percentage = float(input('What is your grade percentage? '))
last_digit = grade_percentage % 10

if last_digit >= 7 and grade_percentage < 90 and grade_percentage > 59:
    sign = '+'
elif last_digit < 3 and grade_percentage > 59:
    sign = '-'
else:
    sign = ''

if grade_percentage >= 90:
    letter = 'A'
elif grade_percentage >= 80:
    letter = 'B'
elif grade_percentage >= 70:
    letter = 'C'
elif grade_percentage >= 60:
    letter = 'D'
else:
    letter = 'F'

print()

print(f'Letter grade: {letter}{sign}')

if grade_percentage >= 70:
    print('Congratulations! You passed the class.')
else:
    print('You did not pass the class. Better luck next time.')

print()