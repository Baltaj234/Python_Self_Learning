# Creating a global variable

x = "Awesome"

# Creating a function with a local variable inside

def myfunction():
    x = "Fantastic"
    print("Local variable x:", x)

    
    
    
    
# Calling the function to see the output
myfunction()

# Printing another statement isolated
print("Global variable x:", x)