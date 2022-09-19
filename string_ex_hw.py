 # write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string
import string

name_one = input("Enter name one: ")
name_two = input("Enter name two: ")


if all(elem in name_two  for elem in name_one):
    words=[]
    for i in string.ascii_lowercase:
        if name_two.count(i)>0:
            words.append(str(i)+" "+str(name_two.count(i)))
    print(f"output: {','.join(words)}")
else:
     print("Not all characters are in the second string")



