"""
Program to demonstrate use of function

"""
# Simple function


def welcome_msg():
    print("Welcome to Python World")

# Function with parameter


def with_parameter(name):
    print("Welcome {name}")

# Function with return statement


def with_return():
    print("Inside function")
    return "Hi"

# Function with parameter and return statement


def add(a, b):
    print("Addition function")
    return a+b


# main
if __name__ == "__main__":
    welcome_msg()           # function call
    with_parameter("Aditi")
    msg = with_return()
    print(msg)
    print(f"Addition:{add(10,20)}")
