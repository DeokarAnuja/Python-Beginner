"""
    Arithmetic operators    +,-,*,/,%,**, //
    Assignment operators    +=,-=
    Comparison operators    >,<,>=,<=,==,!=
    Logical operators       and,or,not
    Identity operators      is,is not
    Memebership Operators   in, not in
    Bitwise operators       &,|,~,^,>>,<<
"""

# Arithmetic operators
print(f"\n{'='*10}Arithmetic Operators{'='*10}")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(f"\n{'='*10}Result{'='*10}")
print(f"Addition : {num1+num2}")
print(f"Subtraction : {num1-num2}")
print(f"Division : {num1/num2}")
print(f"Modulo : {num1%num2}")
print(f"{num1} raised to {num2} : {num1**num2}")

# Assignment operators
print(f"\n{'='*10}Assignment operators{'='*10}")
a = 10
print(f"Value of a:{a}")
a += 10
print(f"After a+=10 :{a}")
a -= 10
print(f"After a-=10 :{a}")
a *= 10
print(f"After a*=10 :{a}")
a **= 2
print(f"After a**=2 :{a}")
a /= 10
print(f"After a/=10 :{a}")
a //= 10
print(f"After a//=10 :{a}")
a %= 10
print(f"After a%=10 :{a}")


# Comparison Operators
print(f"\n{'='*10}Comparison Operators{'='*10}")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(f"\n{'='*10}Result{'='*10}")
print(f"{num1} > {num2} : {num1>num2}")
print(f"{num1} < {num2} : {num1<num2}")
print(f"{num1} >= {num2} : {num1>=num2}")
print(f"{num1} <= {num2} : {num1<=num2}")
print(f"{num1} == {num2} : {num1==num2}")
print(f"{num1} != {num2} : {num1!=num2}")

# Logical operators
print(f"\n{'='*10}Logical Operators{'='*10}")
result = num1 >= 18 and num1 <= 65
result1 = num1 >= 18 or num1 <= 65
print(f"{num1} >= 18 and {num1} <= 65 :{result}")
print(f"{num1} >= 18 or {num1} <= 65 :{result1}")
print(f"not {num1} > 10 :{not num1>10}")

# Identity operators
# is operator compares id of the variable.
print(f"\n{'='*10}Identity Operators{'='*10}")
a = 10
b = 90
c = 10
print(f"a is a : {a is a }")
print(f"a is b : {a is b }")

# The id() function returns a unique id(memory address) for the specified object.
# The comaprison 'a is a'  is equivalent to id(a)==id(a)
print(f"id(a):{id(a)}")
print(f"id(b):{id(b)}")
print(f"id(c):{id(c)}")  # same as id(a)
c = c+10
print(f"id(c):{id(c)}")  # new id

# is not
# oppposite of is operator
print(f"a is not a : {a is not a }")
print(f"a is not b : {a is not b }")


# Membership operators
print(f"\n{'='*10}Membership operators{'='*10}")
print(f"'x' in 'xyz':{'x' in 'xyz'}")
print(f"'x' in 'xyz':{'x' not in 'xyz'}")


# Bitwise operators
a = 10
b = 2
print(f"\n{'='*10}Bitwise operators{'='*10}")
print(f"Bitwise AND: a & b = {a&b}")
print(f"Bitwise OR: a | b = {a|b}")
print(f"Bitwise NOT: ~ a = {~a}")
print(f"Bitwise XOR: a ^ b ={a^b}")
print(f"Bitwise Right shift: a >> 1 = {a>>1}")
print(f"Bitwise left shift:a << 1 = {a<<1}")
