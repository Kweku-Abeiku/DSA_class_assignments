import datetime
import random

import numpy as np

TimeBinary = []
TimeInterpolation = []
finalBinarytime100 = []
finalBinarytime1000 = []
finalBinarytime5000 = []
finalInterpolationTime100 = []
finalInterpolationTime1000 = []
finalInterpolationTime5000 = []

def Binary_Search(array, start, end, element):
    if end >= start:
        mid = start + (end - start) // 2

        if array[mid] == element:
            return mid

        elif array[mid] > element:
            return Binary_Search(array, start, mid - 1, element)

        else:
            return Binary_Search(array, mid + 1, end, element)
    else:
        return -1


def search(N, target):
    start_time = datetime.datetime.now()
    numbers = []
    for i in range(N):
        value = int(random.uniform(0, 32767))
        numbers.append(value)
    #    print("Unsorted array", numbers)
    numbers.sort()
    Arr = np.array(numbers)
    #    print("Sorted array", Arr)

    element = target
    result = Binary_Search(Arr, 0, len(Arr) - 1, element)
    if result != -1:
        print("Target found at Position " + str(result))
    else:
        print("Target not found")

    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = round(time_diff.total_seconds() * 1000, 2)

    #print("--- %s milliseconds ---" % execution_time)
    TimeBinary.append(execution_time)


def Interpolation_Search(N, target):
    start_time = datetime.datetime.now()
    numbers = []
    for i in range(N):
        value = int(random.uniform(0, 32767))
        numbers.append(value)
    #    print("Unsorted array", numbers)
    numbers.sort()
    Arr = np.array(numbers)
    #    print("Sorted array", Arr)

    element = target
    low = 0
    high = (len(Arr) - 1)
    while low <= high and target >= Arr[low] <= Arr[high]:
        POS = low + int(((float(high - low) / (Arr[high] - Arr[low])) * (target - Arr[low])))
        if Arr[POS] == target:
            print("Target found at Position " + str(POS))
            return POS
        if Arr[POS] < target:
            low = POS + 1
        else:
            high = POS - 1
    print("Target not found")
    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = round(time_diff.total_seconds() * 1000, 2)

    #print("--- %s milliseconds ---" % execution_time)
    TimeInterpolation.append(execution_time)

print("--------------------")
print("Binary Search")
print("--------------------")

for i in range(5):

    search(100, 1234)
    # print(TimeBinary)
    averageTimeBinary = sum(TimeBinary) / len(TimeBinary)

finalBinarytime100.append(averageTimeBinary)
print("Average time for Binary search(N=100): %s milliseconds" %round(averageTimeBinary, 3))
print("")

for i in range(5):

    search(1000, 1234)
    # print(TimeBinary)
    averageTimeBinary = sum(TimeBinary) / len(TimeBinary)

finalBinarytime1000.append(averageTimeBinary)
print("Average time for Binary search(N=1000): %s milliseconds" %round(averageTimeBinary, 3))
print("")

for i in range(5):

    search(5000, 1234)
    # print(TimeBinary)
    averageTimeBinary = sum(TimeBinary) / len(TimeBinary)

finalBinarytime5000.append(averageTimeBinary)
print("Average time for Binary search(N=5000): %s milliseconds" %round(averageTimeBinary, 3))
print("")


print("--------------------")
print("Interpolation Search")
print("--------------------")

for i in range(5):

    Interpolation_Search(100, 1234)
    # print(TimeBinary)
    averageTimeInterpolation = sum(TimeInterpolation) / len(TimeInterpolation)

finalInterpolationTime100.append(averageTimeInterpolation)
print("Average time for Interpolation search(N=100): %s milliseconds" %round(averageTimeBinary, 3))
print("")

for i in range(5):

    Interpolation_Search(1000, 1234)
    # print(TimeBinary)
    averageTimeInterpolation = sum(TimeInterpolation) / len(TimeInterpolation)

finalInterpolationTime1000.append(averageTimeInterpolation)
print("Average time for Interpolation search(N=100): %s milliseconds" %round(averageTimeBinary, 3))
print("")

for i in range(5):

    Interpolation_Search(5000, 1234)
    # print(TimeBinary)
    averageTimeInterpolation = sum(TimeInterpolation) / len(TimeInterpolation)

finalInterpolationTime5000.append(averageTimeInterpolation)
print("Average time for Interpolation search(N=100): %s milliseconds" %round(averageTimeBinary, 3))
print("")

print("RESULTS")
print("     | Binary Search | Interpolation Search |")
print("100  | %s | %s |" %(finalBinarytime100 ,finalInterpolationTime100))
print("1000  | %s | %s |" %(finalBinarytime1000 ,finalInterpolationTime1000))
print("5000  | %s | %s |" %(finalBinarytime5000 ,finalInterpolationTime5000))
