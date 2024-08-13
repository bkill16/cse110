print()

print('Welcome to the Loan Qualification Tool. Please enter a rating from 1 to 10:')

print()

loan_size = float(input('How large is the loan? '))
credit_history = float(input('How good is your credit history? '))
income = float(input('How high is your income? '))
down_payment = float(input('How large is your down payment? '))

can_loan = False

if loan_size >= 5:
    
    if credit_history >= 7 and income >=7:
        can_loan = True;
    elif credit_history >= 7 or income >= 7:
        
        if down_payment >= 5:
            can_loan = True

else:

    if income >= 7 or down_payment >= 7:
        can_loan = True
    
    if income >= 4 and down_payment >= 4:
        can_loan = True

print()

if can_loan:
    print('Congratulations! You qualify for a loan!')
else:
    print('Sorry, you do not qualify for a loan.')

print()
