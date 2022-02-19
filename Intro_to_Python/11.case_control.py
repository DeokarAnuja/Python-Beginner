"""
    match statement with case key word is used for case control.
    A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
    Like switch case
    Syntax:
        match expression:
            case pattern1:
                pattern1 block
            case pattern2:
                pattern2 block


"""

# Example with individual values
age = 30

match age:
    case 10:
        print('Age is 10')
    case 20:
        print('Age is 20')
    case 30:
        print('Age is 30')

# match with wildcard (_) like default
# If no case matches, none of the branches is executed.
# Wildcard are executed if no case matches.
match age:
    case 10:
        print('Age is 10')
    case 20:
        print('Age is 20')
    case _:
        print("Default")

# more than one value in single pattern
num = 3
match num:
    case 2 | 4 | 6:
        print("Even")
    case 3 | 5 | 7:
        print("Odd")

# Supports Unpacking
point = (20, 30)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")

# We can add an if clause to a pattern, known as a “guard”.
#  If the guard is false, match goes on to try the next case block.
point = (20, 20)
match point:
    case (x, y) if x == y:
        print(f"Y=X at {x}")
    case (x, y):
        print(f"Not on the diagonal")
