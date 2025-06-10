# Create a function validate_age(age) that does the following:
# Takes age as an input.
# Raises a ValueError if the age is not a positive integer. Otherwise, it should return the age.
# Includes a docstring explaining the function's behavior and how to handle the potential ValueError.

def validate_age(age):
    """
    Validates that the age is a positive integer

    If the age is not a positive integer, raises a ValueError.
    """
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer.")
    
    return age

age = validate_age(27)
print(age)




# Create a function calculate_rectangle_area(length, width) that does the following:
# Takes length and width as inputs.
# Returns the area of the rectangle (length * width).
def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Takes the length and width as inputs and returns the area (length * width).
    """
    return length * width

length = 10
width = 8
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")




# Create a function calculate_circle_area(radius) that does the following:
# Takes the radius as input.
# Returns the area of the circle (π * radius^2).
def calculate_circle_area(radius):
    """
    Calculates the area of a circle.

    Takes the radius as input and returns the area (π * radius^2).
    """
    import math
    return math.pi * (radius ** 2)

radius = 10
circle_area = calculate_circle_area(radius)
print(f"The area of the circle is: {circle_area:.2f}")




get_area(shape, *args)
# Create a function get_area(shape, *args) that does the following:
# Takes a shape type as the first argument and additional arguments as needed for that shape.
# Returns the area of the shape based on the type:
# - "rectangle": requires length and width
# - "circle": requires radius
def get_area(shape, *args):
    """
    Calculates the area of a shape based on the type.

    Takes a shape type as the first argument and additional arguments as needed for that shape.
    Returns the area of the shape:
    - "rectangle": requires length and width
    - "circle": requires radius
    """
    if shape == "rectangle":
        if len(args) != 2:
            raise ValueError("Rectangle requires two arguments: length and width.")
        return calculate_rectangle_area(*args)
    
    elif shape == "circle":
        if len(args) != 1:
            raise ValueError("Circle requires one argument: radius.")
        return calculate_circle_area(*args)
    
    else:
        raise ValueError("Unsupported shape type. Use 'rectangle' or 'circle'.")

# Examples:
shape = "rectangle"
length = 10
width = 5
area = get_area(shape, length, width)
print(f"The area of the {shape} is: {area}")
shape = "circle"
radius = 7
area = get_area(shape, radius)
print(f"The area of the {shape} is: {area:.2f}")
