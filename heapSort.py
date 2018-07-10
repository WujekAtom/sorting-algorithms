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


def heapSort(dataToSort):
    tabLen = len(dataToSort)

    # for i in range(1, tabLen):
    #     j = i
    #     if j%2:
    #         k = j//2
    #     else:
    #         k = j //2 - 1
    #     tmp = dataToSort[i]
    #     print("j = %s\nk = %s\ntmp = %s" %(j,k,tmp))
    #     if k> -1:
    #         print(dataToSort[k])
    #     print("\n")

    for i in range(1, tabLen):
        j = i
        if dataToSort[j-1] < dataToSort[j*2]:   # Left node
            pass
print(data2)
heapSort(data2)
