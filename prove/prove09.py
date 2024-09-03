print("\nWelcome to the Shopping Cart Program!")

menu_choice = 0
items = []
prices = []

while menu_choice != 5:
    print("\nPlease select one of the following:")
    
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Calculate Total")
    print("5. Quit")

    menu_choice = int(input("Please enter an action: "))

    if menu_choice == 1:
        item_to_add = input("What item would you like to add? ")
        items.append(item_to_add)
        
        price_to_add = float(input(f"What is the price of '{item_to_add}'? "))
        prices.append(price_to_add)
        
        print(f"'{item_to_add}' has been added to the cart.")
    
    elif menu_choice == 2:
        print("The contents of the shopping cart are:")
        
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i + 1}. {item} - ${price:.2f}")

    elif menu_choice == 3:
        user_remove = int(input("Which item would you like to remove? "))
        item_to_remove = user_remove - 1
        
        if item_to_remove < len(items) and item_to_remove >= 0:
            items.pop(item_to_remove)
            prices.pop(item_to_remove)
            print("Item removed.")
        else:
            print("Error. This item doesn't exist.")

    elif menu_choice == 4:
        total = 0

        for price in prices:
            total += price

        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif menu_choice == 5:
        break

    else:
        print("Please enter a valid action.")

print("Thank you. Goodbye.\n")