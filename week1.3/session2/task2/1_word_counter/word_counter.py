# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
morelines = True
words =0
# open and read the file
#file = open("week1.3/session2/task2/1_word_counter/story.txt")

# calculate the number of words
#while morelines == True:
#    current = file.readline()
#    words = words + len(current.split())
#    if current == "\n":
#        morelines = False
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
with open("week1.3/session2/task2/1_word_counter/story.txt") as file:
    words = len(file.read().split())

# display the wordcount
print(words)
# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
