"""
    Program to demonstrate use of print()
    
    print()-prints to standard output
    
    Syntax:
        print(object(s), sep=separator, end=end, file=file, flush=flush)
    
    Parameters:
        object(s)   One or more objects to be printed.
        sep         used to mention object separator. [optional] 
        end         What to print at the end. [optional]
        file        Object of file to write the output.
        flush       If True, stream is flushed without buffereing
        
    Return type:None
        
"""
from __future__ import print_function
from time import sleep

# print() without any arguments
print()

# print() with one object
print("Python 3")

# print() with more than one object
print("1", "2", "3", 4)

# print() with separator
print(1, 2, 3, sep=":")

# print() with end parameter
print(1, 2, 3, end="...\n")

# print() with sep and end parameter
print(1, 2, 3, sep=":", end=".\n")

# print() using f-string
print(f"Value of 3*2 is {3*2}")

# print() with File Parameter
print('Text from Python print()', file=open('print_out.txt', 'a'))


# print()  with flush parameter
# By default value of flush is False

# Execution will wait for 5 seconds and then output
print('Flush is set to False.Data will be buffered.', end='')
sleep(5)

# Execution will print first and then wait 5 seconds
print('Flush is set to True.Data will be forcibly printed to ouput.', end='', flush=True)
sleep(5)


print('This program demonstrate use of print()')
