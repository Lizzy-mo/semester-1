# Week 1.3, Session 1: Task 2a
data = True
k = 2
while data:
    k = 2 * k 
    print(k)
    if k > 200:
        data = False
    

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.

# 1. Add a break statement to exit the loop if k>200

# 2. Rewrite the code to directly use the while loop instead of break.