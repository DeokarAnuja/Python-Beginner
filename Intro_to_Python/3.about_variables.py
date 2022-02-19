"""
    Variables:
        Names given to computer memory locations.
        Used to store values.
        Value stored in variable is changeable.
        Type of variable is changeable
        
    Rules:
        Must start with a letter or the underscore character.
        Can only contain A-z, 0-9, and _ .
        Variable names are case-sensitive.
        The keywords cannot be used naming the variable.
"""
# variable creation and single assignment
name = 'Aditi'

# multiple assignment with same value
p = q = r = 20

# multiple assignment with different values
x, y, z = 10, "Python", 30.5

# swap variables
a, b = 10, 50
a, b = b, a
