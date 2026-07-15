# Personal Information Manager
# My first Python project
# Author: [Your Name Here]
# Description: Stores and displays personal information using
# variables, user input, and formatted output.

# ---------------------------------------------------------
# Welcome message
# ---------------------------------------------------------
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# ---------------------------------------------------------
# Store static information
# These are hardcoded values describing me.
# ---------------------------------------------------------
name = "Aman Kumar"          # string - my name
age = 21                     # integer - my age in years
city = "Moradabad"           # string - the city I live in
hobby = "playing guitar"     # string - my favorite hobby

# ---------------------------------------------------------
# Get user input
# We ask the user two questions and validate that they
# don't submit an empty answer.
# ---------------------------------------------------------
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ")
while favorite_food.strip() == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color.strip() == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# ---------------------------------------------------------
# Calculate age in months
# Simple math operation: multiply years by 12
# ---------------------------------------------------------
age_in_months = age * 12

# ---------------------------------------------------------
# Display all information
# Using f-strings for clean, readable formatted output
# ---------------------------------------------------------
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# ---------------------------------------------------------
# Goodbye message
# ---------------------------------------------------------
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)
