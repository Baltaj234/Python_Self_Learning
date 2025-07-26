# Returning a range of characters using the slice syntax

b = "Hello World"
# Get the characters from position 2 to position 5 (not included)
# The first index is 0
print(b[2:5])

# By leaving out the start index, the range will start from the 1st character
b = "Hello World"
print(b[:5])

# By leaving out the end index, the range will go to the end
b = "Hello World" 
print(b[2:])

# Using negative indexes to start the slice from the end of the string
b = "Hello World"
print(b[-5:-2])



