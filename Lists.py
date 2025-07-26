# How lists in Python work

# Lists are collections that are ordered and changeable
# They allow duplicate elements

# Creating a simple list
myList = ["Apple", "Banana", "Cherry"]
print(myList) 

# Lists allow duplicates
myList = ["Apple", "Banana", "Banana", "Cherry"]

# Determining list length
print(len(myList))

# Lists can be of any data type

# Lists can contain different data types
list1 = ["Apple", 34, True, 40, "Sun", 3.4]

# The data type of a list is <class 'list'> (just a list datatype)

# Accessing list items
# Lists are 0-indexed, meaning the first item is at index 0
print(myList[0]) # the first item

# Negative indexing works here too
print(myList[-1]) # the last item

# Access multiple elements
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Changing list items
thisList = ["Apple", "Banana", "Soda"]
thisList[2] = "Blackberry"
print(thisList)

# Append list items
thisList.append("Orange")

# Inserting list items
thisList.insert(1, "Grapes")

# Extending a list
# Adding a list to another list
firstList = ["Canada", "America", "Japan"]
secondList = ["France", "Germany", "Italy"]
firstList.extend(secondList)

# Any iterable object can be added using this extend method





