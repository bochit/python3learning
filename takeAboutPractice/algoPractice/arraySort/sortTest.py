from arraySortLib import mergeSort, bubbleSort, quickSort, heapSort
from sadBoyUsesLinkedList import insertionSort
import random
import time as time_  #don't override time
from BST import BST

def millis():
    return time_.time() * 1000

def runSort(func, arr, s):
    start = millis()
    print(s + ": \n" + str(func(arr)))
    end = millis()
    print("time spent: " + str(round(end-start, 4)) + " ms\n")

def runBST(arr):
    start = millis()
    bst = BST()
    bst.insertList(arr)
    print("BST to list: \n" + str(bst.toList()))
    end = millis()
    print("time spent: " + str(round(end - start, 4)) + " ms\n")

a = [(random.random()*10000 // 10) for _ in range(4000)]
print("original array: \n" + str(a) + "\n")

runSort(bubbleSort, a, "bubbleSort")

runSort(insertionSort, a, "insertionSort")

runBST(a)

runSort(heapSort, a, "heapSort")

runSort(mergeSort, a, "mergeSort")

runSort(quickSort, a, "quickSort")

runSort(sorted, a, "system function sorted")
print("so sad.")

