"""
Sortowanie przez scalanie
"""

from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(0,10):
        data.append(randint(0,100))
    return data

data = randomData()
data2 = [5,8,4,1,10,0,2,1]

def mergeSort(dataToSort, startIndex, endIndex):
    if endIndex > startIndex:
        pvL = (startIndex + endIndex) // 2   # middle element

        mergeSort(dataToSort, startIndex, pvL)   # left sublist
        if dataToSort[startIndex] > dataToSort[pvL]:
            dataToSort[startIndex], dataToSort[pvL] = dataToSort[pvL], dataToSort[startIndex] # swap elements
        print(dataToSort)
        pvR = (startIndex + endIndex) // 2
        mergeSort(dataToSort, pvR+1, endIndex)   # right sublist
        print(dataToSort)

        if dataToSort[pvR+1] > dataToSort[endIndex]:
            dataToSort[pvR + 1], dataToSort[endIndex] = dataToSort[endIndex], dataToSort[pvR+1]
        return
    else:
        return

print(data2)
mergeSort(data2, 0, len(data2)-1)
print(data2)