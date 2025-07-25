# Exploring how strings work in Python

# Can be printed directly

print("This is a string!!")

# Quotes can be used inside of strings
# as long as they don't match quotes surrounding the string

print("It's alright.")
print("He is called 'Johnny'")
# Single and double quotes can both be used
print('He is called "Johnny"')

# Variable can be assigned to a multiline string.
# The triple quotes are used to indicate that it is a multiline string.

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


# In Python strings are Arrays
# Each character in the string is an element in the array
# Square brackets can be used to access elements of a string
h = "Hello"
print(h[0]) # Prints H


# We can loop through the characters in a string
# Using a for loop

for x in "banana":
    print(x) # Prints each character in the string


# Getting the length of a string
l = "Hello guys!"
print(len(l)) # Prints the length of the string

# Checking if a phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt) # Returns True if the phrase is found, False otherwise


# Using an if statement to check the same thing
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") # Prints Yes, 'free' is present.


# Check if something is not present in text
txt = "The best things in life are free!"
print("expensive" not in txt)

# Using an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

