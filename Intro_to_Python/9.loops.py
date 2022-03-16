"""
    Program to demonstrate use of loops
    1.While
    2.Do while
    3.For

"""

# while loop
i = 1  # initialization
while i < 10:  # condition
    print(i, end="\t")
    i += 1  # update statement

print("\n")  # newline

#do while
i = 1
while True:  # Infinte loop
    print(i, end="\t")
    i += 1
    if i == 10:
        break  # exit loop

print("\n")
# range(start,stop,step) stop is excluded
for i in range(1, 10, 1):
    print(i, end="\t")


print("\n")
# for element in sequence
for char in "Python":
    print(char, end="\t")

print("\n")
# Loops can also have else blocks
i = 1
while i < 10:
    print(i, end="\t")
    i += 1
else:  # Executed when condition is false
    print("\nCompleted")

for i in range(1, 10, 1):
    print(i, end="\t")
else:
    print("\nFor Loop Completed")
