"""
        Program to demonstrate use of input() functions

        input():
            Used to accept data from keyboard.
        Syntax:
            input(prompt)
        Parameter:
            prompt  Message to be displayed for accepting input.[optional]
        Return type: str
        Returns:
            input from user
"""
# input() without prompt
input()

# input() with prompt
input("Enter your name:")

# store input
name = input("Enter your name:")
print(f"Hello {name} !")

# check return type
print(type(name))

number = input("Enter numeric value:")
print(f"Type of numeric value is {type(number)}")

# convert str to int [Type casting]
number = int(input("Enter numeric value:"))
print(f"Type check after type casting:{type(number)}")
