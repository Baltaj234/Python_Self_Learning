# A collection of conditional concepts for better control flow usage

# Elif keyword
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("b is smaller than a")


# Short hand if statement
if a > b: print("a is greater than b")

# Short hand if else statement
a = 2
b = 350
print("A") if a > b else print("B")

# The not operator
z = 33
r = 200
if not z > r:
    print("z is not greater than r")


# Nested if statements
x = 41
if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and above twenty")
    else:
        print("but not above twenty")
