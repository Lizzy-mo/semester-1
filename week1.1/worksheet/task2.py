"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
int month_save = input("how much money would you like to save each month")
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
int total = month_save*12
# print this out for the user with a suitable message.
print("the amount you will save per year is £",total,".")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
float total_interest = total *1.8
# print this out in the format £X.XX (to two decimal places).
print("the total amount of money including interest you will have saved in a year is £",total_interest)

