import math

print()

length = float(input("Enter length: "))
print(f"The area of a square with a side length of {length} is: {length ** 2}")
print(f"The area of a circle with a radius of {length} is {math.pi * length ** 2}")
print(f"The volume of a cube with a side length of {length} is: {length ** 3}")
print(f"The volume of a sphere with a radius of {length} is: {4 / 3 * math.pi * length ** 3}")

print()