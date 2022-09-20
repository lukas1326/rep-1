# # 2. Cubes

# The user enters the beginning (integer) and end number.

# The output is the entered numbers and their cubes

# For example: inputs 2 and 5 (two inputs)

# Output

# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]

start = int(input('Enter the start number: '))
end = int(input('Enter the end number: '))

[print(f'{i} cubed: {i**3}') for i in range(start,end+1)]

l = []
for i in range(start,end+1):
    l.append(i**3)
print(f'All cubes: {l}')

