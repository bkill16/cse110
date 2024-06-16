grade_percentage = float(input("\nWhat is your grade percentage? "))

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

if grade_percentage % 10 < 3 and grade_percentage >= 60:
    sign = "-"
elif grade_percentage % 10 >= 7 and grade_percentage < 94 and grade_percentage >= 60:
    sign = "+"
else:
    sign = ""

print(f"\nYour letter grade is: {letter}{sign}")

if grade_percentage >= 70:
    print("Congratulations! You passed the class!\n")
else:
    print("You did not pass the class. Better luck next time.\n")