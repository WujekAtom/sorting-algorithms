from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(1,10):
        data.append(randint(0,100))
    return data

data = [78, 51, 70, 93, 80, 34, 27, 90, 63, 44, 34, 35, 33, 41, 60, 37, 60, 60, 3]
dataRandom = randomData()
data2 = [2,9,4,3,5,6,7]
data3 = [43, 69, 8, 25, 90, 16, 0, 51, 72]
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
            # if current element is > next, then move smaller to left
            dataToSort[k] = dataToSort[k+1]
            k += 1
        dataToSort[k] = tmp
    return dataToSort


# IN PROGRESS
def insertSortBinarySelect(dataToSort):

    n = len(dataToSort) -1 # for loop, number of elements - 1
    j = len(dataToSort) - 2 # range doesn't include

    for i in range(j, -1, -1):
        # starts from before last element
        tmp = dataToSort[i]     # saving element that will be insert in proper place

        #looking for the place in array when tmp can be add
        indxP = i   # start of array when tmp will be insert
        indxK = n   # end of array when tmp will be insert
        print("Checking: %s" %tmp)
        while indxK - indxP > 1:    # while searching array has more than 1 element
            middle = (indxP + indxK) // 2   # calculate middle element in array: [1,2,3] -> el: 2

            # if tmp is bigger than middle element, than we are looking for a place
            # to insert on the right side od middle - it means we will divide array from
            # right side of the middle untill the array will contains 1 element
            print("1. %s %s" %(indxP, indxK))
            if tmp > dataToSort[middle]:
                indxP = middle
                indxK = n
                print("2. %s %s" % (indxP, indxK))
            else:
                indxK = middle
                print("3. %s %s" % (indxP, indxK))


    return dataToSort
print("Sorting:")
print(data3)
#print(insertSorting(dataRandom))

print(insertSortBinarySelect(data3))
