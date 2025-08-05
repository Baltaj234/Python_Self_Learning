# How to find the smallest element in an array in Python

# Define the array
my_array = [7, 12, 9, 4, 11]
#Set a minimum value
min_value = my_array[0]

# Loop through the array
# check if the next values are lower then the minimum value
for i in my_array:
    if i < min_value:
        min_value = i


print("Lowest_Value is ", min_value)

