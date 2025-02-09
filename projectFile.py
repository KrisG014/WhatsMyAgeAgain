# Simple program to greet the user and calculate their age in 5 years

# Ask for user's name
name = input("What is your name? ")

# Ask for user's birth year
year = int(input("What's your birth year? "))

# Ask for user's age
age = int(input("How old are you? "))

# Calculate age in 5 years
age_in_5_years = age + 5

# Calculate age in 5 years
age_in_10_years = age + 10

# Print greeting and future age
print(f"Hello, {name}!")
print(f"In 5 years, you will be {age_in_5_years} years old.")
print(f"In 10 years, you will be {age_in_10_years} years old.")