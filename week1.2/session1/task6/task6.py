# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
h_Albums = ["wasteland baby!", "Hozier", "Unreal unearth unending"]
SF_Albums = ["people watching", "Hypersonic missiles", "Seventeen goinng under"]
# (keys are artist names, values are lists of album names)
artists = {
    "Hozier": h_Albums ,
    "Sam Fender": "Aire"
    
}
# Pretty-print the data structure
pprint(artists)
# Display details of one album recorded by a specific artist
