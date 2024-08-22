print("\nEnter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum = sum + number

print(f"The sum is: {sum}")

average = sum / len(numbers)

print(f"The average is: {average}")

max = max(numbers)

print(f"The largest number is: {max}")

print()