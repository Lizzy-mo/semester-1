"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
state = "red"
state_list = states.__iter__()
print (state_list)
print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
for i in range(0,maxtime):
    state_count = states.get(state)
    print_loop_count = state_count
    nxt_state = next(state_list, None) 
    while state_count >=0 and state_count != None:
        for k in range(1,print_loop_count):
            systime = systime + 1
            print(f"Time {systime:03} State {state}")
            state_count = state_count-1
            
        systime = systime + k 
    nxt_state = next(state_list, None) 
    state = nxt_state
            
    
  
    
    
    
# At the end of each step you should output the time and state using the statement on line 14