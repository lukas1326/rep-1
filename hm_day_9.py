# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable


def good_bad_strings(good_one,good_two,bad_one):

    sorted_list = sorted(set(good_one)&set(good_two)-set(bad_one))
    result = ''.join(sorted_list)
    return result

print(good_bad_strings("bolabcfc", "faolb", "bcf"))