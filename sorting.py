# How to sort lists in Python

thisList = ["orange", "apple", "mango", "banana"]
thisList.sort()
print(thisList)

# Sorting the list numerically
numericList = [100, 50, 65, 82, 34]
numericList.sort()
print(numericList)

# Sorting the list descending
descendingList = ["Star", "Xyz", "String"]
descendingList.sort(reverse=True)
print(descendingList)

# The sort method is case sensitive
# Meaning all capital letters are sorted before lower case letters

# Performing a case-insensitive sort
thisList.sort(key = str.lower)





