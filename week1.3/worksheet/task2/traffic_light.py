"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = {"red": 4, "red_amber": 3, "green": 5, "amber": 3}

maxtime = int(input())  # read an integer number of steps (>0)
state = "red"
state_order = ["red", "red_amber", "green", "amber"]  # cycle order
index = 0
time_in_state = 0

# Simulate the traffic light system up to time=maxtime in 1-second steps
for systime in range(maxtime + 1):
    print(f"Time {systime:03} State {state}")

    # increment the time-in-state counter
    time_in_state += 1

    # If state's duration is complete, move to the next state
    if time_in_state >= states[state]:
        index = (index + 1) % len(state_order)
        state = state_order[index]
        time_in_state = 0
