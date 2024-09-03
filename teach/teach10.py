print("\nEnter the names and balances of bank accounts (type: quit when done)")

accounts = []
balances = []

account_name = ""

while account_name.lower() != "quit":

    account_name = input("What is the name of this account? ")

    if account_name != "quit":
        account_balance = float(input("What is the balance? "))

        accounts.append(account_name)
        balances.append(account_balance)

print("\nAccount Information:")

total = 0

for i in range(len(accounts)):
    account = accounts[i]
    balance = balances[i]
    total += balance
    print(f"{account} - ${balance:.2f}")

print(f"\nTotal: ${total:.2f}")

count = len(balances)
average = total / count

print(f"Average: ${average:.2f}\n")