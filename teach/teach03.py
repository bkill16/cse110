import math

print()

square_length = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {square_length ** 2}')
rectangle_length = float(input('What is the length of the rectangle? '))
rectangle_width = float(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is: {rectangle_length * rectangle_width}')
radius = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {math.pi * radius ** 2}')

print()