"""This is the entry point of the program."""
#me and kevin did this together but i wanted to go through the whole process of forking it, cloning it, creating a workspace, setting up the virtualenv,
# and then commiting, and pushing changes back to my github. I also added an alternate way we could've done the project with a nested for loops instead of just one.

def create_box(height, width, character):
    box= ''
    if height < 1 or width < 1:
        return 'Error'
    for x in range(height):
        box+= character*width+'\n'
    return box
    
"""
#or we could have also done it like this, with a nested for loop like we learned in class.
def create_box(height, width, character):
    box=''
    if height < 1 or width < 1:
        return 'Error'
    for x in range(height):
        row=''
        for i in range(width):
            row+= character
        box+= row +'\n'
    return box
"""


def outline_box(height, width, character):
    full_row = character * width
    edge_row = character + ' '*(width-2) + character
    interior = ''
    
    if height < 1 or width < 1:
        return 'Error'
    for x in range(1, height-1):
        interior += edge_row+'\n'
    
    box = (full_row+'\n') + (interior) + (full_row)
    
    return box
