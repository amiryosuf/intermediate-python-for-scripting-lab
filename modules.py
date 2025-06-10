# Create a function that generates a strong password greater than 8 characters.
# Generate a random password of a specified length using the "random" module.
# The password should include at least one uppercase letter, lowercase letter, and digit.

def create_strong_password(length=10):
    """
    Generates a strong password of specified length.
    The password includes at least one uppercase letter, one lowercase letter, and one digit.
    """
    import random
    import string
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    # Ensure the password contains at least one uppercase letter, one lowercase letter, and one digit
    while not (any(c.isupper() for c in password) and
               any(c.islower() for c in password) and
               any(c.isdigit() for c in password)):
        password = ''.join(random.choice(characters) for _ in range(length))
    return password
password = create_strong_password(10)
print(f"Generated strong password: {password}")




# Create a function that calculates the difference in days between two dates and return the result.
# The function should take two strings in the format "YYYY-MM-DD" as input.
# Use the "datetime" module to convert these strings into datetime objects

def calculate_date_difference(date1, date2):
    """
    Calculates the difference in days between two dates.
    
    Takes two strings in the format "YYYY-MM-DD" as input and returns the difference in days.
    """
    from datetime import datetime
    
    # Convert strings to datetime objects
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    # Calculate the difference in days
    delta = abs((d2 - d1).days)
    
    return delta
date1 = "2023-10-01"
date2 = "2023-10-15"
days_difference = calculate_date_difference(date1, date2)
print(f"The difference in days between {date1} and {date2} is: {days_difference} days")




# Create a function that retunrs the area of a circle given the radius
# Utilize the "pi" constant from the "math" module to help calculate the area of the circle.
def calculate_circle_area(radius):
    """
    Calculates the area of a circle.
    
    Takes the radius as input and returns the area (π * radius^2).
    """
    import math
    return math.pi * (radius ** 2)
radius = 10
circle_area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")





