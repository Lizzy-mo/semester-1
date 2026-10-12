# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input
sequence = []
for k in range (0,L-1):
    current = k
    test = current - 1 - k
    if test >0 and (sequence.count(current - 1 +k)==0):
        next = current - 1 +k 
    elif sequence.count(current - 1 +k)==0:
        next = test
    sequence.append(next)

sequence.count
# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence