import random  # import random module
import numpy  # import numpy module

list1 = []  # create a first input list
list2 = []  # create a second input list


def DotProduct(N, ListA, ListB):
    # ListA = [] * N
    # ListB = [] * N
    for i in range(N):  # iterate and append to listA
        n = random.randint(1, 1000)  # generate random number to input in current list index
        ListA.append(n)  # append element
    for j in range(N):  # iterate and append to listB
        m = random.randint(1, 1000)  # generate random number to input in current list index
        ListB.append(m)  # append element

    npListA = numpy.array(ListA)  # convert to numpy array
    npListB = numpy.array(ListB)  # convert to numpy array

    result = numpy.dot(npListA, npListB)  # calculate dot product

    print("Size(N):", N)
    print("ListA:", ListA)
    print("ListB:", ListB)
    print("Results:", result)  # print results


DotProduct(10, list1, list2)  # run function with size N = 10
print("--------------------------------")
DotProduct(100, list1, list2)  # run function with size N = 100
