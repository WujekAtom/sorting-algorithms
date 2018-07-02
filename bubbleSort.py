# Bubble sort implementation

from random import randint

# Pseudorandom function to generate datas to sort
def randomData():
    data = []
    for i in range(1,20):
        data.append(randint(0,100))
    return data

dataToSort = randomData()

def bubbleSorting(dataIn):
    sortedData = False
    while True:
        sortedData = False
        for i in range(len(dataIn) -1):
            if dataIn[i] > dataIn[i+1]:
                # Replacing elements
                tmp = [dataIn[i], dataIn[i+1]]
                dataIn[i] = tmp[1]
                dataIn[i+1] = tmp[0]
                sortedData = True
        if sortedData == False:
            return dataIn

print(dataToSort)
print(bubbleSorting(dataToSort))