people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 9999
min_name = ""

for line in people:
    parts = line.split()

    name = parts[0]
    age = int(parts[1])

    if age < min_age:
        min_age = age
        min_name = name

print(f"\nThe youngest person is: {min_name} with an age of {min_age}\n")