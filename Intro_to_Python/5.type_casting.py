"""
    Program to demonstrate type casting.

    Type casting is converting data of one type to another.

    We can use following functions for type casting:

        bool():To convert data to boolean type

        float():to convert data to float type

        int():to conver data to int type

        str():to convert data to string type

        complex():to convert data to complex type

"""
# int to boolean using bool()
x=10
print("="*30)  # str * 3  will repeat given string 3 times
print("Value \t\t Type")
print("="*30)
print(f"{x} \t\t {type(x)}")
x=bool(x)
print(f"{x} \t\t {type(x)}") #Any non zero value is considered to be True 
print("-"*30)

# int to float using float()
x=10
print(f"{x} \t\t {type(x)}")
x=float(x)
print(f"{x} \t\t {type(x)}") 

# str to int using int()
x='10'
print(f"{x} \t\t {type(x)}")
x=int(x)
print(f"{x} \t\t {type(x)}") 
print("-"*30)

# int to str using str()
x=10
print(f"{x} \t\t {type(x)}")
x=str(x)
print(f"{x} \t\t {type(x)}")
print("-"*30)

# str to complex using complex()
x='10+5j'
print(f"{x} \t\t {type(x)}")
x=complex(x)
print(f"{x} \t {type(x)}") 
print("-"*30)



