"""
Implementation of heapsort.
"""

from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(0,10):
        data.append(randint(0,100))
    return data

data = randomData()
data2 = [7, 5, 9, 6, 7, 8, 10]
data3 = [9,7,4,3,6,5,1,2,8,11]
data4 = [58, 54, 70, 69, 45, 24, 49, 80, 89, 10]
data5 = [69, 10, 39, 63, 11, 87, 52, 93, 16, 57]
data6 = [52, 18, 75, 29, 64, 10, 24, 25, 24, 29]

"""
buildMaxHeap method creates a complete binary tree from the list.
Parent - node that has one or two childs.

It starts checking from the last parent. When node is checked, then it checks previous parent

"""
def buildMaxHeap(dataToSort):
    tabLen = len(dataToSort)

    for i in range(tabLen, -1, -1):
        lastParent = i // 2 - 1
        if lastParent < 0:  # beacuse we are counting from zero, then lastParen may be -1, so we need to reassign
            lastParent = 0

        maxHeap(lastParent, dataToSort, tabLen)

    return dataToSort


"""
maxHeap method is checking recursively if current node's value fulfills the condition:
parentNode >= leftChild & parentNode >= rightChild
"""
def maxHeap(parentIndex, data, dataLen):
    left = parentIndex * 2 + 1      # calculate index of left child
    right = parentIndex * 2 + 2     # calculate index of right child

    # Checking if left child exist. If not, than parent is the last element.
    # Calculated index must be smaller than list's size
    if right <= dataLen:
        # Checking if right child exist and if exist, if is bigger then left
        if right != dataLen:
            if left < dataLen and data[left] < data[right]:
                bigger = right  # right child's value is bigger than left
            else:
                bigger = left   # left child's value is bigger than right
        else:
            bigger = left

        # Comparing parent with biggest of childs' value.
        # If parent is smaller than child, then replace parent and child.
        # When parent is replaced, then we will have to check if parent is bigger than new childs [if childs exist]
        if data[parentIndex] < data[bigger]:
            tmp = data[bigger]
            data[bigger] = data[parentIndex]
            data[parentIndex] = tmp

            # Calling recursively this method with the index of bigger element. This element
            # is the previous parent
            maxHeap(bigger, data, dataLen)


"""
This method sort the whole tree.
Steps:
1. Replace element[0] - the biggest element in the tree - with the element[last].
Last - this is the last element in the tree
2. Now check the tree starting from root - element[0], check if the tree is max heap. Call recursively the method maxHeap
with index of root and lenght of tree decreased of 1.
We are not checking the last element in the tree, because the last element contains element with the MAX value. This is
already sorted element.
3. Go to 1. Now the tree smaller of one, last element. Repeat steps 1 and 2 until the tree is 1-element.

"""
def sortHeap(dataToSort):
    # dataLen is decreased of 1, because the last element will not be checked because this is the place for sorted elements
    dataLen = len(dataToSort) - 1
    while dataLen >= 0:
        # Replace first element in the tree with the last element
        tmp = dataToSort[0]
        dataToSort[0] = dataToSort[dataLen]
        dataToSort[dataLen] = tmp

        # Call the method to check if after replacing values the treee is max tree [max heap]
        maxHeap(0, dataToSort, dataLen)
        dataLen = dataLen - 1


print("Before sorting")
print(data)
buildMaxHeap(data)
sortHeap(data)
print("After sorting:")
print(data)