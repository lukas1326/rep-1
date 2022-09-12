# 1. Health check

# Ask user for their temperature.

# If the user enters below 35, then output "not too cold"

# If 35 to 37 (inclusive), output "all right"

# If the temperature  over 37, then output  "possible fever

# remember about type conversion if needed

temp = int(input('Tell me your temperature '))
if temp < 35:
    print('not too cold')
elif temp >=35 and temp <=37:
    print('all right')
else:
    print('possible fever')
    
    
# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.

# Calculate the bonus.

# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

sal = float(input('Your salary is  :')) 
period = float(input('How many years have you worked here? '))
bonus_rate=0.15
if period >=2:
    print(f'{period} years of experience,{sal} Euro salary, the bonus will be {(sal)*bonus_rate *(period-2)}')
else:
    print(f'{period} years of experience,{sal} Euro salary, no bonus(0)')