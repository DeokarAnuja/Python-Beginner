"""
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
