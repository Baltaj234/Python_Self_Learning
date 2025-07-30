# demonstrating how functions work in Python

# Defining a function
def my_function():
    print("Hello, World!")

# calling the function we created
my_function()


# Arguements
# Information that can be passed into a function

def refuse(name):
    print(name + " refuses.")

# calling the function with an argument
refuse("John")

# Recursive function example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)