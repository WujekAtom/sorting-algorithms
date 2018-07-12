"""
Implementation of quicksort algorithm
"""

from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(0,10):
        data.append(randint(0,100))
    return data

data = randomData()
data2 = [7, 2, 4, 7, 3, 1, 4, 6, 5, 8, 3, 9, 2, 6, 7, 6, 3]
data3 = [2,1,3,0,2]
data4 = [2, 5, 1, 3, 4, 0, 6, 2, 5]


"""
Quick sort implementation.
1. We define a pivot. Pivot is a reference element of the list. It can be choose randomly. I set it to middle of list.
2. Main idea is that all elements smaller than pivot must be on the left side of pivot, bigger on the ight side.
3. We set I on the beginning of the list and J at the end. We are looking for the first occurrence of bigger element
in left sublist.
On the right sublist we are looking for the smaller element than pivot.
It means that these found elements are on wrong side and need to be swap.
4. We are swaping elements until indexes miss themselve, I>J.
5. Now we have on the left side of pivot all smaller elements, on right side all bigger elements.
6. When we have this condition, we can recursively call quick sort for left and right sublist. It will divide
sublist into smaller sublist etc.
"""

def quickSort(dataToSort, startIndex, endIndex):

    # Pivot divides a list into 2 parts: left and right
    pv = (startIndex + endIndex)//2

    i = startIndex
    j = endIndex

    while i < j:

        # Searching left side of the list in the range (start, pivot)
        # We are looking for the first occurance of element bigger than pivot [if exist]
        while dataToSort[i] < dataToSort[pv]:
            i = i + 1

        # Searching right side of the list in the range (pivot, end)
        # We are looking for the first occurance of element smaller than pivot [if exist]
        while dataToSort[j] > dataToSort[pv]:
            j = j - 1

        # When we find smaller and bigger element of pivot, we need to replace them
        # Condition i<=j means that indexes doesn't miss themselves
        if i <= j:
            dataToSort[i], dataToSort[j] = dataToSort[j], dataToSort[i]
            i += 1  # after swaping proceed with next element
            j -= 1  # as above

    # Calling recursively quickSort method for left sublist and right sublist
    # Condition are for testing if the sublists has more than 1 element
    if j > startIndex:
        quickSort(dataToSort, startIndex, j)
    if i < endIndex:
        quickSort(dataToSort, i, endIndex)



print(data)
quickSort(data, 0, len(data) - 1)
print(data)

