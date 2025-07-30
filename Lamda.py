# How Lamda Functions work in Python

# Can take any number of arguments
# But only have one expression

# Add 10 to argument a, and return the result
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5,2))

x = lambda a, b, c: a + b + c
print(x(10, 10, 10))

# Why use lamda functions?
# You can use them as anonymous functions inside other functions
def myfunc(n):
  return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:
myDoubler = myfunc(2)
print(myDoubler(11))

# Use lambda functions when an anonymous function is required for a short period of time



