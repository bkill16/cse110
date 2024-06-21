first_rider_age = int(input("\nWhat is the age of the first rider? "))
first_rider_height = float(input("What is the height of the first rider? "))

if first_rider_age >= 12 and first_rider_age < 18:
    golden_pass = input("Do you have a golden pass? (Yes/No) ")

    if golden_pass.lower() == "yes":
        first_rider_age = 18

second_rider_present = input("Is there a second rider? (Yes/No) ")

if second_rider_present.lower() == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = float(input("What is the height of the second rider? "))

    if second_rider_age >= 12 and second_rider_age < 18:
        golden_pass = input("Do you have a golden pass? (Yes/No) ")

        if golden_pass.lower() == "yes":
            second_rider_age = 18

    if first_rider_height >= 36 and second_rider_height >= 36:
        if first_rider_age >= 18 or second_rider_age >= 18:
            can_ride = True
        elif first_rider_age < 18 and second_rider_age < 18:
            if first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
                can_ride = True
            else:
                can_ride = False
        else:
            can_ride = False
    else:
        can_ride = False

    if first_rider_age < 18 and second_rider_age < 18:
        if (first_rider_age >= 16 and second_rider_age >=14) or (first_rider_age >= 14 and second_rider_age >= 16):
            can_ride = True
else:
    if first_rider_age >= 18 and first_rider_height >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride. Please be safe and have fun.\n")
else:
    print("Sorry, you may not ride.\n")