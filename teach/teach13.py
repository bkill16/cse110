import math

def compute_area_square(side):
    area = side ** 2
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = math.pi * (radius ** 2)
    return area

print("\nWelcome to the Area Calculator!")

shape = ""

while shape.lower() != "quit":

    shape = input("\nEnter your shape or type 'quit' to quit: ")

    if shape.lower() == "square":
        user_side = float(input("\nSquare Side Length: "))
        result = compute_area_square(user_side)
        print(f"The area of the square is: {result:.2f}")

    elif shape.lower() == "rectangle":
        user_length = float(input("\nRectangle Length: "))
        user_width = float(input("Rectanlge Width: "))
        result = compute_area_rectangle(user_length, user_width)
        print(f"The area of the rectangle is: {result:.2f}")

    elif shape.lower() == "circle":
        user_radius = float(input("\nCircle Radius: "))
        result = compute_area_circle(user_radius)
        print(f"The area of the cirlce is: {result:.2f}")

    elif shape.lower() == "quit":
        break

    else:
        print("\nUnable to calculate area. Please enter another shape.")

print("\nThank you. Goodbye.\n")