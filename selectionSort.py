"""
Selection sort implementation

1. Looking for the smallest element in the array
2. Replacing it with first element
3. Then looking for the next smallest element and replacing with second element.
3. Looking for smallest element and replacing it with nth element
"""

from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(0,10):
        data.append(randint(0,100))
    return data

data = randomData()
data2 = [67, 50, 69, 20, 82, 89, 97, 91, 0]

"""
Selection sort implementation
"""
def selectionSort(dataToSort):

    dataLen = len(dataToSort)

    for i in range(0, dataLen):
        tmpIndex = i                # Save index of comparing element
        tmpElem = dataToSort[i]     # Save value of comparing element
        j = i
        while j < dataLen:          # Every each iteration the subarray is decraesing of 1 element

            # looking for the index of smallest element
            # If checking element is bigger then next, then we save index of found element
            # and comparing it with the rest of elements in subarray
            if dataToSort[tmpIndex] > dataToSort[j]:
                tmpIndex = j
            j += 1
        # After finding index of the smallest element we are replacing it with the current element
        dataToSort[i] = dataToSort[tmpIndex]
        dataToSort[tmpIndex] = tmpElem
    return dataToSort

print(data)
print(selectionSort(data))
