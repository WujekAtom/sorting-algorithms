from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(1,10):
        data.append(randint(0,100))
    return data

dataRandom = randomData()

"""
# 0. Saving 45 (before last element)
# 1. [20, 9, 45, 6] checking if 45 > 6, if yes than move 6 to left
# 2. [20, 9, 6, 45] Decreasing loop counter, save 9. If 9 >6, if yes, move 6 left
# 3. [20, 6, _ ,45] check if 9> 45, if yes, move 45 left, if not, put 9 in empty space
# 4. [20, 6, 9, 45] save 20. 20 > 6, move 6 left.
# 5. [6,_, 9, 45] 20 > 9, move 9 left
# 6. [6, 9, _ , 45] 20 >45
# 7. [6, 9, 20, 45]

"""
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


"""
# INSERT SORT WITH BINARY SEARCHING
# This method takes subarray on the right side of current element [TMP] to sort
# and is searching middle element of the subarray. When TMP is bigger than middle, then it divides the subarray
# into smaller subarray on the right side of MIDDLE element. Otherwise on the left side.
# It causes to diving the subarray into smaller subarray until it contains 1 element.
# Each time TMP is compared with MIDDLE so at the end we get the last element of subsubarray and by comparing
# TMP with this last one we find the position where TMP must be inserted.

"""
def insertSortBinarySelect(dataToSort):

    n = len(dataToSort) -1 # for loop, number of elements - 1
    j = len(dataToSort) - 2 # range doesn't include

    for i in range(j, -1, -1):
        # starts from before last element
        tmp = dataToSort[i]     # saving element that will be insert in proper place

        #looking for the place in subarray when tmp can be add
        indxP = i + 1  # start of subarray from the element on the right of element to insert [current el, so called TMP]
        indxK = n  # end of array

        while indxK - indxP >= 1:    # dividing the array until we get one-element subarray
            middle = (indxP + indxK) // 2   # calculate index of middle element in array: [1,2,3] -> el: 2

            # if TMP is bigger than MIDDLE element, than we are looking for a place
            # to insert on the right side od middle - it means we will divide array from
            # right side of the MIDDLE. Dividing through the while loop until the subarray will contains 1 element
            # We are changing indxP which is beginning of subarray to new beginning, on the right side of MIDDLE
            # Otherwise we are looking on the left of MIDDLE, so the inxdP [begigning] stay, but the end needs
            # to be change to the index of MIDDLE element

            if tmp > dataToSort[middle]:
                indxP = middle + 1
            else:
                indxK = middle
        else:

            # While loop finished dividing the array [looking for the place to insert TMP]. We have indexes of begin
            # and end of subarray. Now we are moving all elements to the left to make a place for insert TMP.
            # For example:
            # [1,7,2,3,4,5,6] -> checking the "7"element, so need to move the elements to the left:
            # [1,2,3,4,5,6,6] -> Moved. Double 6 is ok, on the last position in next step will be add "7"

            for k in range(i, indxP):
                # k<n checking if we are not out of array's range
                if k < n:
                    dataToSort[k] = dataToSort[k+1]

            # If TMP is bigger than found [last] element from subarray, then insert TMP after it...
            if tmp > dataToSort[indxP]:
                dataToSort[indxP] = tmp
            else:
                # ...otherwise before.
                dataToSort[indxP-1] = tmp
    return dataToSort


print("Sorting:")

print(dataRandom)

# Uncomment below to use regular insert or with binary search

#print(insertSorting(dataRandom))
print(insertSortBinarySelect(dataRandom))