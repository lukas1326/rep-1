# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically

import datetime


user_name = input("What is your name?  ")

user_age = input(f"How old are you, {user_name}?  ")
target_age = 100
diff_age = target_age - int(user_age)
current_year = datetime.datetime.now().year
print(f"You will be 100 after {diff_age} years.")
print(f"You will be {target_age} years old in {diff_age + current_year}.")
