from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(1,7):
        data.append(randint(0,100))
    return data

data = [78, 51, 70, 93, 80, 34, 27, 90, 63, 44, 34, 35, 33, 41, 60, 37, 60, 60, 3]
dataRandom = randomData()

# 0. Saving 45 (before last element)
# 1. [20, 9, 45, 6] checking if 45 > 6, if yes than move 6 to left
# 2. [20, 9, 6, 45] Decreasing loop counter, save 9. If 9 >6, if yes, move 6 left
# 3. [20, 6, _ ,45] check if 9> 45, if yes, move 45 left, if not, put 9 in empty space
# 4. [20, 6, 9, 45] save 20. 20 > 6, move 6 left.
# 5. [6,_, 9, 45] 20 > 9, move 9 left
# 6. [6, 9, _ , 45] 20 >45
# 7. [6, 9, 20, 45]
def insertSorting(dataToSort):
    n = len(dataToSort) - 1  # how many index
    j = len(dataToSort) - 2 # starts from the before-last element

    for i in range(j, -1, -1):   # steps decreasing
        #print(i)   # enable to see iterator counter
        tmp = dataToSort[i]    # remember last element before sorted part of array
        k = i
        while k <n and tmp > dataToSort[k+1]:
            #print("k: %s //// k+1: %s" %(dataToSort[k], dataToSort[k+1])) # enable to see internal loop counter
            # if current element is > next, then
            dataToSort[k] = dataToSort[k+1]
            k += 1
        dataToSort[k] = tmp
    return dataToSort


# Inprogress
def insertSortBinarySelect(dataToSort):

    n = len(dataToSort) - 1
    j = len(dataToSort) - 2
    print("Len: %s\t\t before: %s" %(n,j))
    for i in range(j, -1, -1):
        tmp = dataToSort[i]
        indxP = i
        indxK = n
        print(indxP, indxK)
    return dataToSort

print(dataRandom)
#print(insertSorting(dataRandom))

insertSortBinarySelect(dataRandom)
