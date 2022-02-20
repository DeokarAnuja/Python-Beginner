"""
    Program to demonstrate use of index and slicing using str object
"""

mystr = "PythonProgramming"

# Indexing
print(mystr[0])  # zero based index
print(mystr[-1])  # negative index


# slicing
# [start:stop:step]
print(mystr[0:6:1])
print(mystr[-1:-8:-1])

print(mystr[-1:5:-1])


# reverse string
print(mystr[::-1])
