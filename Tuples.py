# tuples are used to store multiple items in a single variable

# Creating a tuple

thisTuple = ("apple", "banana", "cherry")

# Items are ordered, unchangeable, and allow duplicate values
# Being ordered means items have a defined order
# That order will not change

# We cannot add or remove or change items after a tuple has been created

# Length of the tuple
print(len(thisTuple))

# to create a tuple with only one item a comma must be added
# Otherwise Python will not recognize it is a tuple

newTuple = ("One", )
print(type(newTuple))

# Tuples can be of any data type
# Can also contain different data types

# You can convert a tuple to a list
# Then change the things you want to change
# And convert the list back into a tuple

x = ("apple", "banana", "cherry") # Tuple
y = list(x) # Making it into a list
y[1] = "kiwi" # Making our change
x = tuple(y) # Back into a tuple

print(x)

# How to loop a Tuple

thisTuple = ("String", "Data", "Science")
for x in thisTuple:
    print(x)


# Using a while loop 
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

  # Joining Tuples
  tuple1 = ("a", "b", "c")
  tuple2 = (1, 2, 3)
  
  tuple3 = tuple1 + tuple2
  print(tuple3)

  