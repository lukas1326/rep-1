# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.


sentence = input('Enter a sentence, please: ').lower().split()

temp=[]
for el in range(len(sentence)):
    m= [i for i in sentence[el]]
    temp.append(''.join(m[::-1]))
    temp[0]=temp[0].title()
result = ' '.join(temp)

#maybe I should check the uppercase...

print(result)