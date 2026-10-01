"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = str(input("Where are you going to? "))

distance_miles_input = float(input("How many miles will you travel? "))
time_hours_input = float(input("How many hours will the journey take? "))
if destination or distance_miles_input or time_hours_input <=0:
    print ("one of you values is 0 or negative check them before proceeding")
else:

# TODO: calculate the average speed in miles per hour s=d/t
    speed = float(distance_miles_input//time_hours_input) #in mph
# TODO: print a summary message using an f-string
    print(f"you should travel at an average speed of{speed} miles per hour for your journey to {destination}")
# Extension: add validation for zero or negative values
    