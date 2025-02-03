import math

# Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius**2

# Example usage
radius = 5
area = calculate_area(radius)

print("The area of a circle with radius {} is: {:.2f}".format(radius, area))
