# Sets are used to store multiple items in a single variable

# Making a set
mySet = {"Apple", "Banana", "cherry"}

# Sets are unordered
# They are unchangeable
# They do not allow duplicate values
# Duplicate values will be ignored

# Getting the length of a set
print(len(mySet))

# Sets can be of any data type
# A set can contain different data types


# Looping through a set

thisSet = {"Stop", "Start", "Listen"}
for x in thisSet:
    print(x)


# adding an item to a set
thisSet.add("Go")

# Add elements from one set to another
thisset = {"apple", "banana", "cherry"} 
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) 

print(thisset) 

# Using the union function
# Returns a new set with all items from both sets

set1 = {"A", "B", "C"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)


