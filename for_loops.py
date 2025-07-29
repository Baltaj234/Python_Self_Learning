# How for loops work in Python

# creating a list
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# Looping through a string
for x in "Banana":
    print(x)

# How the break statement works in for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

# How the continue statement works in for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
