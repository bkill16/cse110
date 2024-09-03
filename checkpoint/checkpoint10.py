print("\nPlease enter the items of the shopping list (type: quit to finish):")

list_item = ""
items = []

while list_item.lower() != "quit":
    list_item = input("Item: ")

    if list_item.lower() != "quit":
        items.append(list_item)

print("\nThe shopping list with indexes is:")

for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")

item_to_change = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

items[item_to_change] = new_item

print("\nThe shopping list with indexes is:")

for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")

print()