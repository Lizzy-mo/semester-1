# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
file =open ("sales.csv")
morelines = True
count = 0
while morelines == True:
    current = file.readline()
    current_list = current.split(",")
    sale_day = current_list[3]
    if sale_day > previous:
        highest = sale_day
    total = total + sale_day
    if file.readline() == "\n":
        morelines = False
    previous = sale_day 
    count +=1

# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows