# In Python an iterator is an object that contains a countable number of values
# You can traverse through all of an iterators values

# Lists, tuples, dictionaries, and sets are all iterable objects
# They define the __iter__() method which returns an iterator object

# Return an iterator from a tuple, and print each value:
myTuple = ("apple", "banana", "cherry")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# For loops can be used to iterate too

