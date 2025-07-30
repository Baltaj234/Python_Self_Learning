# The basics of Object-Oriented-Programming in Python

# Almost everything in python is an object

# An example of a full class below:
class Person:
# The constructor of the class that constructs the object
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Creating an object (a person) from the class
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __init__() method is called automatically every time the class is being used to create a new object
# The __str__() method controls what is returned when the class object is represented as a string
# An example of it being used in a class below:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
# Name and age are returned from the method
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



