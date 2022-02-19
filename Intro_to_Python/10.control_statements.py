"""
    Program to demonstrate use of control statements
    1.break        to exit loop
    2.continue     to skip remaining part of current iteration
    3.pass         Does nothing.Can be used as placeholder

"""
# break
for i in range(1, 40, 5):
    print(i, end='\t')
    if (i == 26):
        break
print("\n")

# continue
for i in range(1, 10, 1):
    if i == 6:
        continue
    print(i, end='\t')
print("\n")

# pass
for i in range(1, 5, 1):
    pass
print(i)
