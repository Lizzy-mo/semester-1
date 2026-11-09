# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']
not_fishh = []
not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)

for animal in animals:
    if animal != 'goldfish':
        not_fishh.append(animal)

print(not_fishh)
# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same