# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

numbers = read_numbers()
numbers.sort()
length_of_list = len(numbers)
if length_of_list == 0:
    print("hey")
    sys.exit("Error: no numbers provided")
total = 0
min = numbers[0]
max = numbers[len(numbers)-1]
for i in range (0,len(numbers)):
    current = numbers[i]
    total = total+current
mean = total/len(numbers)
median = numbers[(len(numbers))//2]
print(f"Minimum = {min}\nMaximum = {max}\nMean = {mean}\nMedian = {median}")

