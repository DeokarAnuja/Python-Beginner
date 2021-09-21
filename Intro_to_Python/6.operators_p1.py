"""
    Arithmetic operators    +,-,*,/,%,**, //
    Assignment operators    +=,-=
    Comparison operators    >,<,>=,<=,==,!=
    Logical operators       and,or,not
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
