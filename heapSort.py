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

"""
buildMaxHeap method creates a complete binary tree from the list. 
"""
def buildMaxHeap(dataToSort):
    tabLen = len(dataToSort)

    for i in range(tabLen, -1, -1):     #
        lastParent = i // 2 - 1
        if lastParent < 0:
            lastParent = 0
        print("Last parent = %s" %lastParent)
        left = lastParent * 2 + 1
        right = lastParent *2 + 2

        maxHeap(lastParent, dataToSort)

        print(dataToSort)
    return dataToSort

"""
maxHeap method is checking rekursively if current node's value fulfills the condition:
parentNode >= leftChild & parentNode >= rightChild
"""
def maxHeap(parentIndex, data):
    left = parentIndex * 2 + 1      # calculate index of left child
    right = parentIndex * 2 + 2     # calculate index of right child

    # Checking if left child exist. If not, than parent is the last element.
    # Calculated index must be smaller than list's size
    if left < len(data):
        # Checking if right child exist and if exist, if is bigger then left
        if right < len(data) and data[left] < data[right]:
            bigger = right  # right child's value is bigger than left
        else:
            bigger = left   # left child's value is bigger than right

        # Comparing parent with biggest of childs' value.
        # If parent is smaller than child, then replace parent and child.
        # When parent is replaced, then we will have to check if parent is bigger than new childs [if childs exist]
        if data[parentIndex] < data[bigger]:
            tmp = data[bigger]
            data[bigger] = data[parentIndex]
            data[parentIndex] = tmp
            maxHeap(bigger, data)   # Calling recursively this method with the index of bigger element. This element
                                    # is the previous parent


"""
TODO: This method is finally sorting the list using heap sort way.
"""
def sortHeap(dataToSort):
    pass

print(data3)
print("\n\n")
print(buildMaxHeap(data3))
