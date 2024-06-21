print("\nRate the following from 1-10:\n")

loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        can_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            can_loan = True
        else:
            can_loan = False
    else:
        can_loan = False
else:
    if credit_history < 4:
        can_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            can_loan = True
        elif income >= 4 and down_payment >= 4:
            can_loan = True
        else:
            can_loan = False

if can_loan:
    print("\nYou can have a loan!\n")
else:
    print("\nYou cannot have a loan.\n")
        