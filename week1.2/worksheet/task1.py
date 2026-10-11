# Worksheet 1.2: Task 1 Solution
import sys
# variables

score = 0
grade = "" 

try:
    score = int(input("what score did you get out of 100"))
    
    if score <=39:
        grade = "Fail"
    elif score >=40 and score <=69:
        grade = "Pass"
    else :
        grade = "Distinction"
    print(f"{score} is a {grade}")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")