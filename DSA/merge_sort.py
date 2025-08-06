# An Implimentation of the merge sort algorithm in Python

def mergeSort(arr):
    # If the array has 0 or 1 elements it is already sorted
    if len(arr) <= 1:
        return arr

# Find the middle index of the array
    mid = len(arr) // 2

    # Split the array into two halves
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # Recursively call mergeSort on each half
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)


    # Merge the two sorted halves
    return merge(sortedLeft, sortedRight)

# Merges two sorted lists into one sorted list
def merge(left, right):
    # The final merged sorted list
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

# Append any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Using the methods
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
            
