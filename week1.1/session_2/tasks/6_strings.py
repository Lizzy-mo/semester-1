# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
#makes the   whole string lowercase
print(f"Modified String 1: {user_string.lower()}")
#makes the whole string uppercase
print(f"Modified String 2: {user_string.upper()}")
#
print(f"Modified String 3: {user_string.strip()}")
# replaces all a's with @ symbols
print(f"Modified String 4: {user_string.replace('a', '@')}")
#
print(f"Modified String 5: {user_string.capitalize()}")
#makes first letter of string capitalised
print(f"Modified String 6: {user_string[::-1]}")
# makes the string one character shorter
print(f"Modified String 7: {user_string.title()}")
# makes start of words uppercase and rest lowercase
print(f"Modified String 8: {len(user_string)}")
#returns the length of the string
print(f"Modified String 9: {user_string.find('a')}")
# finds first place where a appears in the string
print(f"Modified String 10: {user_string.count('a')}")
# counts all instances of a in the string 
print(f"Modified String 11: {user_string.startswith('Hello')}")
# check if string starts with"hello world!
print(f"Modified String 12: {user_string.endswith('!')}")
#checks if string ends in "!"
print(f"Modified String 13: {user_string.isalnum()}")
#checks if string is made up of all numbers
print(f"Modified String 14: {user_string.isalpha()}")
# checks if styring is in alphabetical iordewr
print(f"Modified String 15: {user_string.isdigit()}")
# checks if string is all digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!