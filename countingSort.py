from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(0,10):
        data.append(randint(0,20))
    return data

data = randomData()


"""
Counting sort implementation.

To sort we are counting occurrence of each element in the list.
For example:
[3,6,1,5,2,1,3]
Element with value 1: 2
Element with value 2: 1
Element with value 3: 1
Element with value 4: 0
Element with value 5: 1
Element with value 6: 1



"""


# Main method. Hard to write good comment for this code ;) Sorry if you don't know what I mean ;)
def countingSort(dataToSort):

    # Declare empty list of size of possible max value. randomdData() generates numbers between 0 - 20
    countingList = [0]*21

    # For each value from dataToSort, we increase the value in countList at the index equal value from dataToSort
    for i in dataToSort:
        countingList[i] += 1
    gc = 0  # Global Counter for tracing last put element to dataToSort
    for j in range(0, len(countingList)-1):
        if countingList[j]!=0:  # element doesn't exist
            for k in range(0, countingList[j]): # how many elements put to dataToSort
                dataToSort[gc] = j  # j is the index for countingList and element for dataToSort
                gc += 1


print(data)
countingSort(data)
print(data)

