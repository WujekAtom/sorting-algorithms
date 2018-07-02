# Bubble sort implementation

from random import randint

# Pseudorandom function to generate datas to sort
def randomData():
    data = []
    for i in range(1,20):
        data.append(randint(0,100))
    return data

print(randomData())