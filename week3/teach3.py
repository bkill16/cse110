import math

print()

side = float(input("What is the length of a side of the square in cm? "))
square_area = side ** 2
print(f"The area of the square is: {square_area}cm^2, {square_area / 10000}m^2")

length = float(input("What is the length of the rectangle in cm? "))
width = float(input("What is the width of the rectangle in cm? "))
rectangle_area = length * width
print(f"The area of the rectangle is: {rectangle_area}cm^2, {rectangle_area / 10000}m^2")

radius = float(input("What is the radius of the circle in cm? "))
circle_area = math.pi * radius ** 2
print(f"The area of the circle is: {circle_area}cm^2, {circle_area / 10000}m^2")

print()