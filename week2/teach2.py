print()

print("Please enter the following information:")

print()

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone_num = input("Phone number: ")
job_title = input("Job title: ")
id_num = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
start_month = input("Month started: ")
advanced_training = input("Advanced training (Yes/No): ")

print()

print("The ID Card is:")
print("----------------------------------------------------------------")

print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_num}")

print()

print(f"{email.lower()}")
print(phone_num)

print()

print(f"{'Hair: ' + hair_color.capitalize():<30} Eyes: {eye_color.capitalize()}")
print(f"{'Month: ' + start_month.capitalize():<30} Training: {advanced_training.capitalize()}")

print("----------------------------------------------------------------")

print()