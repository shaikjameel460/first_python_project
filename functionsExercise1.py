#problem:Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height

# Calculate area of triangle
def calculate_area(base, height):
    area = (1/2) * base * height
    return area


base = 3
height = 4
area = calculate_area(3, 4)
print("area of triangle is :", area)
