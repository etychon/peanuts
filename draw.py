import random as rand

from peanuts import *

p = Peanuts()

# Family members are case sentitive

# Add family members here as a Python list
# For example:
# p.add_members(['A', 'B', 'C', 'D', 'E'])
p.add_members(['Manu', 'Barbara', 'Cyril', 'Justin', 'Mamy', 'Olivia'])

# Add directional constrains here, as a list of tuples of who can't make a gift to who
# For example we don't want A to make a gift to B, B to C, and C to B:
# p.add_constraints([('A', 'B'), ('B', 'C'), ('C', 'B')])
p.add_constraints([('Manu', 'Barbara'), ('Barbara', 'Manu'), ('Mamy', 'Manu'), ('Cyril', 'Olivia'), ('Olivia', 'Cyril')])

print("Here are the members: ", p.list_members())

print("Here are constraints: ", p.list_constraints())

# Randomly proceed to the draw
p.draw()

# Print the results
p.print_draws()
