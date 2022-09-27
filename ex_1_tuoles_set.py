# 1. Min, Avg, Max

# Write a function get_min_avg_max (sequence) that returns a tuple 
# with three values, 
# the smallest, the arithmetic mean, 
# and the largest value in the string, respectively.

# Example:

# get_min_avg_max ([0,10,1,9]) -> (0,5,10)

# the incoming sequence can be a tuple or a list with numeric values.

def get_min_avg_max(number_int):
    result = (min(number_int),sum(number_int)/len(number_int),max(number_int))
    return result
print(get_min_avg_max([0,10,1,9]))
