"""
    Conditional statements
        1.If 
        2.If else
        3.Else if
    Note:Everything other than zero and False are considered to be True.
"""
# If statement
num = int(input(f"Enter numeric value:"))
if num > 10:
    print("{num} is greater than 10")

# If Else Statement
if num < 10:
    print(f"{num} is smaller than 10")
else:
    print(f"{num} is greater than 10")

# Else if
if num > 0:
    print(f"Positive number")
elif num < 0:
    print(f"Negative number")
else:
    print(f"Zero")

# Anything other than zero and False is True
if 4-3:
    print(f"Expression 4-3 ={4-3}")

if 'A':
    print("A is also considered as True")
else:
    print("Character cannot be used")
