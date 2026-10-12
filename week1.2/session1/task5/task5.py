# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers.update("preston","ribble")
rivers.update("cambridge","Cam")
# Display all the keys
keys = rivers.fromkeys()
print(keys)
# Display all the values
values = rivers.values()
print(values)
# Display all the key:value pairs, as tuples
print(rivers)
# Delete an entry from the rivers database
rivers.popitem()