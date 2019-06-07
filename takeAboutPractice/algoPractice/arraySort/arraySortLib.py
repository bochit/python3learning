"""
Default comparator
"""
def defaultCompare(a,b):
    return a<b
def desc(a,b):
    return a>b

"""
Merge sort implementation
-   O(n*log(n))
-   divide into left and right sub-lists recursively until reaches 1 or 0 elements
-   when the recursion returns back up, merge left and right array(elements), which themselves are already sorted. 
"""
def mergeSort(arr, comparator=defaultCompare):
    l = len(arr)
    if l < 2:
        return arr

    mid = l // 2

    left = mergeSort(arr[:mid], comparator)
    right = mergeSort(arr[mid:], comparator)

    return merge(left, right, comparator)


def merge(a, b, comparator):
    result, ai, bi, la, lb = [], 0, 0, len(a), len(b)

    while ai < la and bi < lb:
        if comparator(a[ai], b[bi]):
            result.append(a[ai])
            ai += 1
        else:
            result.append(b[bi])
            bi += 1

    result += a[ai:]
    result += b[bi:]

    return result

"""
Bubble sort implementation
-   O(n^2) average
-   swap adjacent elements based on comparator, until no swapping is possible
-   keeps looping until a no-swapping run happens
"""
def bubbleSort(arr, comparator=defaultCompare):
    l = len(arr)
    if l < 2:
        return arr

    while True:
        hadSwapLastRound = False
        for i in range(l-1):
            if comparator(arr[i+1],arr[i]):
                arr[i+1],arr[i] = arr[i],arr[i+1]
                hadSwapLastRound = True

        if not hadSwapLastRound:
            return arr

"""
Insert sort with linked list implementation
- O(n^2)
- using linked list here, insert elements to appropriate places.

"""
# def insertionSort(arr, comparator=defaultCompare):
#
#     def findInsertLocation(node, data):
#         # print(str(node.next.data) + "    " + str(data))
#         if node.next != None and comparator(data, node.data):
#             return True
#         else:
#             return False
#
#     linkedList = LinkedList()
#
#     for i in range(len(arr)):
#         ele = arr[i]
#         linkedList.insertBefore(ele, findInsertLocation)
#         # print(linkedList.toList())
#
#     return linkedList.toList()

"""
quickSort sort with linked list implementation
-   find a pivot, then sort other elements to lesss list and greater list
-   recursively quickSort the sub-lists. 
-   on the way up join as (less + pivot + greater)
"""
def quickSort(arr, comparator=defaultCompare):

    l = len(arr)
    if l < 2:
        return arr

    pivotIndex = l//2
    pivot = arr[pivotIndex]

    left = []
    right = []

    for ii in range(l):
        if ii != pivotIndex:
            i = arr[ii]
            if comparator(i,pivot):
                left.append(i)
            else:
                right.append(i)

    # print("left: "+ str(left))
    # print("right: " + str(right))
    return quickSort(left,comparator) + [pivot] + quickSort(right,comparator)


"""
heapSort sort
-   build a max heap as list. Parent bigger than children. parent = i, left = 2*i +1 right= 2*i+2
-   interesting fact: adding more children under a parent can slow down the algorithm
"""
def heapSort(arr, comparator=defaultCompare):
    l = len(arr)

    for i in range(l, -1, -1):
        heapify(arr, l, i, comparator)

    for i in range(l - 1, 0, -1):
        # 0 position one is the known largest, since all parents are larger than children
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0, comparator)

    return arr

def heapify(arr,n,index, comparator):
    largest = index
    li = index * 2 +1
    ri = li+1

    if li < n and comparator(arr[index], arr[li]) :
        largest = li
    if ri < n and comparator(arr[largest] , arr[ri]):
        largest = ri

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr,n,largest, comparator)

"""
Sanity test
"""
a = [8,4,7,4,7,2,67,45,8,32,6,5,8,56]
# print(mergeSort(a))
# print(bubbleSort(a))
# # print(insertionSort(a))
# print(quickSort(a))
# print(heapSort(a))

# print(quickSort(a,defaultCompare))
# print(quickSort(a,desc))