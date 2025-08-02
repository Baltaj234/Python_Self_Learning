# The basics of file handling in Python

# How to open and read a file
f = open("demo.txt")
print(f.read)

# If the file is located outside project location
# You have to specify the file path like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())

# Using the with statement when opening a file
# You don't need to worry about closing the file
with open("demofile.txt") as f:
  print(f.read())

# If you are not using the with statement 
# Closing files must be done manually
f = open("demofile.txt")
print(f.readline())
f.close()

# Reading only parts of a file
# You can specify how many characters you want read to return

with open("demo.txt") as f:
  print(f.read(5))

# You can read one line using the readLine method
with open("demo.txt") as f:
  print(f.readline())

# You can also loop through a file to read it
with open("file.txt") as d:
  for x in d:
    print(x)

# Writing to an existing file
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content.")


# Overwrite existing content in the file
# The "w" will overwrite the entire file
with open("demofile.txt", "w") as f:
  f.write("Overrided the current content")


# How to create a new file
# x creates a new empty file with no content
# If the file already exists there will be an error
f = open("newFile.txt", "x")

# Deleting files
# To delete a file you must import the OS module
import os
os.remove("newFile.txt")

# Check if the file exists, then delete it if it does
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")








