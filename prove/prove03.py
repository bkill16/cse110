print()

child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
num_of_children = int(input('How many children are there? '))
num_of_adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))

print()

subtotal = (child_price * num_of_children) + (adult_price * num_of_adults)
print(f'Subtotal: ${subtotal:.2f}')

sales_tax = (subtotal * tax_rate) / 100
print(f'Sales Tax: ${sales_tax:.2f}')

total = subtotal + sales_tax
print(f'Total: ${total:.2f}')

print()

payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total
print(f'Change: ${change:.2f}')

print()