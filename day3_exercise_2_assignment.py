# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.

# Calculate the bonus.

# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

sal = float(input('Your salary is  :')) 
period = float(input('How many years have you been working here? '))
bonus_rate=0.15
work_years  = 2
if period >=work_years:
    print(f'{period} years of experience,{sal} Euro salary, the bonus will be {(sal)*bonus_rate *(period-work_years)}')
else:
    print(f'{period} years of experience,{sal} Euro salary, no bonus(0)')