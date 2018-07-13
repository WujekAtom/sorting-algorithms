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

    if endIndex > startIndex:   # checking if we have one-element list

        pvL = (startIndex + endIndex) // 2  # middle element
        pvR = ((startIndex + endIndex) // 2) + 1    # middle+1 element

        mergeSort(dataToSort,startIndex, pvL)   # call mergeSort for left list
        mergeSort(dataToSort, pvR, endIndex)    # call mergeSort for right list

        # after calling aboves mergerSorts merthod we have now sublist that needs to be sort and merg into one
        merge(dataToSort,startIndex, pvL, pvR, endIndex)

"""
Merge gets two (sub)list and original data list.
First starts at index s1 and ends at e1. Lets call it LEFT
Second starts at index s2 and ends at e2. Lest call it RIGHT
"""
def merge(dataToMerg, s1, e1, s2, e2):

    index1 = s1
    index2 = s2
    tmp = []    # temporary list to save result of sorting
    while index1 <= e1 and index2 <= e2:    # checking if we have elements in LEFT and RIGHT list
        if dataToMerg[index1] < dataToMerg[index2]: # add smaller element to tmp
            tmp.append(dataToMerg[index1])
            index1 += 1                     # increase index of the left list, because one element has been added to tmp
        else:
            tmp.append(dataToMerg[index2])  # smaller element is from RIGHT list, so add it to tmp
            index2 += 1                     # and increase index of right list, because one element has been added to tmp

    if index1 <= e1:    # left list is longer, we assign left elements to tmp
        while index1 <= e1: # loop through elements and add to tmp
            tmp.append(dataToMerg[index1])
            index1 += 1
    if index2 <= e2:    # right list is longer, we assign left elements to tmp
        while index2 <= e2:
            tmp.append(dataToMerg[index2])
            index2 += 1

    # now we have to put elements from tmp to original list
    j = s1  # start at the beginning of sublist
    for i in tmp:
        dataToMerg[j] = i
        j += 1


print(data)
mergeSort(data, 0, len(data)-1)
print(data)