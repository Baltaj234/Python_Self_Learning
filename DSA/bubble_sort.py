# Implimentation of the bubble sort algorithim in Python

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Items in the array
n = len(my_array)
# Looping through the array
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array: ", my_array)
