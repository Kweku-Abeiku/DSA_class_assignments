import random

import numpy as np


def binarySearch(array, start, end, element):
    if end >= start:
        mid = start + (end - start) // 2

        if array[mid] == element:
            return mid

        elif array[mid] > element:
            return binarySearch(array, start, mid - 1, element)

        else:
            return binarySearch(array, mid + 1, end, element)
    else:
        return -1


def search(N):
    numbers = []
    for i in range(N):
        value = int(random.uniform(0, 32767))
        numbers.append(value)
    print("Unsorted array", numbers)
    numbers.sort()
    array = np.array(numbers)
    print("Sorted array", array)
    element = 'r'
    result = binarySearch(array, 0, len(array) - 1, element)
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Element is not present in array")

search(20)