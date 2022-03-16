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
    print(f"Type of arbitrary argument:{type(args)}")
    for i in args:
        print(i)

# Arbitrary Keyword Argument
def keyword_arbitrary(**kwargs):
    print(f"Type of keyword arbitrary argument:{type(kwargs)}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

# main
if __name__ == "__main__":
    default_arg()
    default_arg("Aditi")
    keyword_arg(name="Ram")
    arbitrary(1, 2, 3)
    keyword_arbitrary(s1="John",s2="Aditi",s3="Alex")
