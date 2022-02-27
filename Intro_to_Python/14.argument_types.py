"""
Program to demonstrate type of arguments
"""

# Default


def default_arg(name="Priya"):
    print(name)

# keyword argument


def keyword_arg(name):
    print(name)

# Arbitrary Argument


def arbitrary(*args):
    for i in args:
        print(i)

# Arbitrary Keyword Argument
def keyword_arbitrary():
    pass

# main
if __name__ == "__main__":
    default_arg()
    default_arg("Aditi")
    keyword_arg(name="Ram")
    arbitrary(1, 2, 3)
