#Homework exercise: 

# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise
# https://github.com/ValRCS/Python_SheGoesTech_22/blob/main/Day_4_Loops/day4_exercise_3.py


end_number = int(input("Enter the last number for prime numbers list: "))

prime_numbers = []
num =2

while len(prime_numbers) <= end_number-1:
    for i in range(2, int(num**0.5)+1): # so we check only up to and including square root of n
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
    num+=1
print(prime_numbers)
