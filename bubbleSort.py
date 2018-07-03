# Bubble sort implementation

from random import randint

# Pseudorandom function to generate data to sort
def randomData():
    data = []
    for i in range(1,20):
        data.append(randint(0,100))
    return data

# Global variables
randomDataToSort = randomData()
dataToSort = [78, 51, 70, 93, 80, 34, 27, 90, 63, 44, 34, 35, 33, 41, 60, 37, 60, 60, 3]


# The most basic implementation of bubble sort
def bubbleSorting1(dataIn):
    sortedData = False
    gc = 0
    while True:
        sortedData = False
        for i in range(len(dataIn) -1):
            print(gc)
            if dataIn[i] > dataIn[i+1]:
                # Replacing elements
                tmp = [dataIn[i], dataIn[i+1]]
                dataIn[i] = tmp[1]
                dataIn[i+1] = tmp[0]
                sortedData = True
            gc = gc + 1
        if sortedData == False:
            return dataIn


# Implementation with decreasing half of iteration, by decreasing the loop counter
def bubbleSorting2(dataIn):
    sortedData = False
    counter = len(dataIn) -1    # for loop statement
    gc = 0
    while True:
        sortedData = False
        for i in range(counter):
            print(gc)
            if dataIn[i] > dataIn[i+1]:
                # Replacing elements
                tmp = [dataIn[i], dataIn[i+1]]
                dataIn[i] = tmp[1]
                dataIn[i+1] = tmp[0]
                sortedData = True
            gc = gc + 1
        if sortedData == False:
            return dataIn

        # Each iteration is shorter, because the biggest element move to the end in the iteration,
        # so there is no need to compare with that element.
        counter = counter - 1

print(dataToSort)
# Uncomment bubbleSorting2 and comment bubbleSorting1 to compare the difference in number of iteration
print(bubbleSorting1(dataToSort))
#print(bubbleSorting2(dataToSort))