# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = str(input("what is your name"))
age = int(input("what is your age in years"))
colour = str(input("what is your favourite colour"))
# Open a file called 'user_info.txt' for reading
file = open("user_info.txt")
# Write each piece of information to the file, each on a new line.
file.write(name)
file.write("\n")
file.write(age)
file.write("\n")
file.write(colour)
file.write("\n")

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
