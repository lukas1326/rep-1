# Exercise
# read text from  sherlock_holmes_adventures.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305
fpath = 'sherlock_holmes_adventures.txt'
with open(fpath,encoding='utf-8') as f:
        lines = f.readlines()

def file_line_len(fpath):
    with open(fpath,encoding='utf-8') as f:
        lines = f.readlines()
    return len(lines) 


print(file_line_len(fpath)) #12304


# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace

# PS preferably use encoding = "utf-8" when reading 

def get_text_lines(fpath):
    with open(fpath,encoding='utf-8') as f:
        
        lines = [line.strip() for line in f if line.strip()]
    return lines


print(len(get_text_lines(fpath)))



# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file 

def save_lines(destpath, lines):
    with open(destpath, mode='w', encoding="utf-8") as fout:
        fout.writelines(lines)  # write all lines from list

destpath='destpath.txt'
save_lines(destpath, lines)

# 1d -> call save_lines with destpath being "pure_sherlock.txt" 
# and lines being the text lines we cleaned from 1b
destpath='pure_sherlock.txt'
lines_pure = get_text_lines(fpath)
save_lines(destpath, lines_pure)

# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, 
# clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")
def clean_punkts(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as fout:
        for line in fin:  # for each line in incoming file
            if line[0] == "\n": # if line starts with "\n" means it is is just one character line
                fout.write("*"*40+"\n")
            else:
                fout.write(line.upper()) # keeping also the newlines
# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary