# Used to store data in key-value pairs

# an example of a dictionary

myCar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2021
}

# this collection is unordered (this version), changeable and does not allow duplicates


# Printing specific values of the dictionary
print(myCar["brand"])

# Duplicate values will override existing values

# Print the number of items in the dictionary

print(len(myCar))

# Dictionaries can contain any data type

# Print the data type of a dictionary
print(type(myCar))

# getting values using a different approach
x = myCar.get("year")

# Return a list of keys in the dictionary
y = myCar.keys()

# Return a tuple of items in the dictionary
z = myCar.items()

# Checking if a key exists in the dictionary
if "model" in myCar:
    print("Key exists")

# Changing an item in the dictionary
# You can add a key-value pair using this syntax as well
myCar["model"] = "F-150"

# Update an items using the update method
myCar.update({"year": 2022})

# Looping through a dictionary
# Prints all the key names
for x in myCar:
    print(x)

# Prints all the values
for x in myCar:
    print(myCar[x])

# Copying a dictionary into another dictionary
newCar = myCar.copy()
print(newCar)

# Creating a nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Create three seperate dictionaries
# Then create one that will contain the other three

# first dictionary
child1 = {
    "name" : "Emil",
    "year" : 2004
}

# Second dictionary
child2 = {
    "name": "Tobias",
    "year": 2007
}

# Third dictionary
child3 = {
    "name": "Linus",
    "year": 2011
}

# Creating the final dictionary
theFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# Accessing items in the nested dictionary
print(theFamily["child1"]["year"])















