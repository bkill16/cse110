kid_price = float(input("\nWhat is the price of a kids meal? "))
kid_quantity = int(input("How many kids are there? "))
adult_price = float(input("What is the price of an adult meal? "))
adult_quantity = int(input("How many adults are there? "))
sales_tax = float(input("What is the sales tax rate? "))

subtotal = (kid_price * kid_quantity) + (adult_price * adult_quantity)
sales_tax = (subtotal * sales_tax) / 100
total = subtotal + sales_tax

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

payment_amount = float(input("\nEnter payment amount: "))
change = payment_amount - total

print(f"Change: ${change:.2f}\n")